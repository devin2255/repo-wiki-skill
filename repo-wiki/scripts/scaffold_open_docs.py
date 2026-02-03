import argparse
import json
import os
import re
import sys
from pathlib import Path
from typing import Dict, List, NamedTuple, Optional, Tuple


INVALID_FILENAME_RE = re.compile(r'[<>:"/\\|?*\x00-\x1f]')


class PagePlan(NamedTuple):
    page_id: str
    title: str


TEMPLATE_PAGE_IDS: Tuple[str, ...] = (
    "1",
    "1.1",
    "1.2",
    "1.3",
    "2",
    "2.1",
    "2.2",
    "2.3",
    "2.4",
    "2.5",
    "3",
    "3.1",
    "3.2",
    "3.3",
    "3.4",
    "3.5",
    "4",
    "4.1",
    "4.2",
    "4.3",
    "4.4",
    "4.5",
    "5",
    "5.1",
    "5.2",
    "5.3",
    "5.4",
    "5.5",
    "6",
    "6.1",
    "6.2",
    "6.3",
    "6.4",
)


PAGE_TITLES: Dict[str, Dict[str, str]] = {
    "en": {
        "1": "Overview",
        "1.1": "Quick Start",
        "1.2": "Installation",
        "1.3": "Key Concepts",
        "2": "Architecture",
        "2.1": "CLI System",
        "2.2": "Configuration System",
        "2.3": "Environment Variable Management",
        "2.4": "Protocol Translation Proxy",
        "2.5": "Model Selection and IP Detection",
        "3": "User Guide",
        "3.1": "Commands Reference",
        "3.2": "Configuration Files",
        "3.3": "Environment Variables",
        "3.4": "Model Provider Setup",
        "3.5": "Troubleshooting",
        "4": "Developer Guide",
        "4.1": "Project Structure",
        "4.2": "Development Setup",
        "4.3": "Testing",
        "4.4": "Code Style and Conventions",
        "4.5": "Contributing Guidelines",
        "5": "Reference",
        "5.1": "CLI Module API",
        "5.2": "Config Module API",
        "5.3": "Proxy Module API",
        "5.4": "Environment Module API",
        "5.5": "Configuration Schema",
        "6": "Advanced Topics",
        "6.1": "Custom Proxy Configurations",
        "6.2": "Protocol Translation Details",
        "6.3": "Windows Registry Integration",
        "6.4": "Multi-Environment Deployments",
    },
    "zh": {
        "1": "概述",
        "1.1": "快速开始",
        "1.2": "安装",
        "1.3": "核心概念",
        "2": "架构设计",
        "2.1": "CLI 系统",
        "2.2": "配置系统",
        "2.3": "环境变量管理",
        "2.4": "协议转换代理",
        "2.5": "模型选择与 IP 检测",
        "3": "用户指南",
        "3.1": "命令参考",
        "3.2": "配置文件",
        "3.3": "环境变量",
        "3.4": "模型/Provider 配置",
        "3.5": "故障排查",
        "4": "开发者指南",
        "4.1": "项目结构",
        "4.2": "开发环境搭建",
        "4.3": "测试",
        "4.4": "代码风格与约定",
        "4.5": "贡献指南",
        "5": "参考",
        "5.1": "CLI 模块 API",
        "5.2": "配置模块 API",
        "5.3": "代理模块 API",
        "5.4": "环境模块 API",
        "5.5": "配置 Schema",
        "6": "高级主题",
        "6.1": "自定义代理配置",
        "6.2": "协议转换细节",
        "6.3": "Windows 注册表集成",
        "6.4": "多环境部署",
    },
}


UI_TEXT: Dict[str, Dict[str, str]] = {
    "en": {
        "index_title": "Wiki Index",
        "nav_label": "Navigation",
        "nav_index": "Wiki Index",
        "nav_prev": "Previous",
        "nav_next": "Next",
        "relevant_files_summary": "Relevant source files",
        "scaffold_note_1": "Scaffold generated from the bundled wiki template.",
        "scaffold_note_2": "Fill this page with content grounded in the current repository, following the template checklists.",
        "relevant_files_placeholder": "- `path/to/file`",
    },
    "zh": {
        "index_title": "Wiki 目录",
        "nav_label": "导航",
        "nav_index": "Wiki 目录",
        "nav_prev": "上一页",
        "nav_next": "下一页",
        "relevant_files_summary": "相关源码文件",
        "scaffold_note_1": "此页为模板脚手架自动生成。",
        "scaffold_note_2": "请基于当前仓库的代码/配置/文档补全内容，并遵循模板清单。",
        "relevant_files_placeholder": "- `path/to/file`",
    },
}


def detect_language_from_query(query: str) -> str:
    q = query or ""
    if any("\u3040" <= ch <= "\u30ff" for ch in q):
        return "ja"
    if any("\uac00" <= ch <= "\ud7af" for ch in q):
        return "ko"
    if any("\u4e00" <= ch <= "\u9fff" for ch in q):
        return "zh"
    if any("\u0400" <= ch <= "\u04ff" for ch in q):
        return "ru"
    return "en"


def parse_page_id(page_id: str) -> Tuple[int, ...]:
    parts = (page_id or "").strip().split(".")
    result: List[int] = []
    for part in parts:
        try:
            result.append(int(part))
        except ValueError:
            result.append(10**9)
    return tuple(result)


def safe_filename(name: str, max_len: int = 120) -> str:
    name = (name or "").strip()
    name = INVALID_FILENAME_RE.sub("-", name)
    name = re.sub(r"\s+", " ", name).strip()
    name = name.replace(" ", "-")
    name = re.sub(r"-{2,}", "-", name).strip("-")
    if not name:
        name = "page"
    return name[:max_len]


def _select_wiki_bundle(wikis: Dict[str, object], lang: str) -> Tuple[str, Dict[str, object]]:
    if lang in wikis:
        return lang, wikis[lang]  # type: ignore[return-value]
    base = (lang or "").split("-")[0]
    if base and base in wikis:
        return base, wikis[base]  # type: ignore[return-value]
    first = next(iter(wikis.keys()))
    return first, wikis[first]  # type: ignore[return-value]


def load_page_plans(input_path: Path, lang: str) -> Tuple[str, List["PagePlan"]]:
    data = json.loads(input_path.read_text(encoding="utf-8"))
    wiki = data.get("wiki") or {}
    wikis = wiki.get("wikis") or {}
    if not isinstance(wikis, dict) or not wikis:
        raise ValueError("Invalid JSON: missing wiki.wikis")

    chosen_lang, bundle = _select_wiki_bundle(wikis, lang=lang)
    pages_raw = bundle.get("pages") or []

    plans: List[PagePlan] = []
    for item in pages_raw:
        plan = (item or {}).get("page_plan") or {}
        page_id = str(plan.get("id") or "").strip()
        title = str(plan.get("title") or "").strip()
        if page_id or title:
            plans.append(PagePlan(page_id=page_id, title=title))

    plans.sort(key=lambda p: parse_page_id(p.page_id))
    return chosen_lang, plans


def default_page_plans(lang: str) -> Tuple[str, List[PagePlan]]:
    base = (lang or "").split("-")[0]
    titles = PAGE_TITLES.get(lang) or PAGE_TITLES.get(base) or PAGE_TITLES["en"]
    plans = [PagePlan(pid, titles.get(pid, PAGE_TITLES["en"].get(pid, pid))) for pid in TEMPLATE_PAGE_IDS]
    return lang, plans


def localize_page_plans(plans: List[PagePlan], lang: str) -> List[PagePlan]:
    base = (lang or "").split("-")[0]
    titles = PAGE_TITLES.get(lang) or PAGE_TITLES.get(base) or PAGE_TITLES["en"]
    localized: List[PagePlan] = []
    for plan in plans:
        title = titles.get(plan.page_id) or plan.title or PAGE_TITLES["en"].get(plan.page_id) or plan.page_id
        localized.append(PagePlan(page_id=plan.page_id, title=title))
    localized.sort(key=lambda p: parse_page_id(p.page_id))
    return localized


def plan_to_filename(plan: PagePlan) -> str:
    prefix = safe_filename((plan.page_id or "page").replace(".", "-"))
    title = safe_filename(plan.title or plan.page_id or "Untitled")
    return f"{prefix}-{title}.md"


def build_nav_line(plans: List[PagePlan], index: int, ui: Dict[str, str]) -> str:
    parts: List[str] = []
    parts.append(f"[{ui['nav_index']}](index.md)")
    if index > 0:
        prev_plan = plans[index - 1]
        prev_title = prev_plan.title or prev_plan.page_id or "Untitled"
        prev_file = plan_to_filename(prev_plan)
        parts.append(f"{ui['nav_prev']}: [{prev_title}]({prev_file})")
    if index + 1 < len(plans):
        next_plan = plans[index + 1]
        next_title = next_plan.title or next_plan.page_id or "Untitled"
        next_file = plan_to_filename(next_plan)
        parts.append(f"{ui['nav_next']}: [{next_title}]({next_file})")
    return f"**{ui['nav_label']}**: " + " | ".join(parts)


def write_scaffold(output_dir: Path, plans: List[PagePlan], force: bool, lang: str) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)

    base = (lang or "").split("-")[0]
    ui = UI_TEXT.get(lang) or UI_TEXT.get(base) or UI_TEXT["en"]

    index_lines = [f"# {ui['index_title']}", ""]
    for idx, plan in enumerate(plans):
        title = plan.title or plan.page_id or "Untitled"
        filename = plan_to_filename(plan)
        index_lines.append(f"- [{title}]({filename})")

        out_path = output_dir / filename
        if out_path.exists() and not force:
            continue
        nav_line = build_nav_line(plans=plans, index=idx, ui=ui)
        out_path.write_text(
            "\n".join(
                [
                    f"# {title}",
                    "",
                    nav_line,
                    "",
                    f"> {ui['scaffold_note_1']}",
                    f"> {ui['scaffold_note_2']}",
                    "",
                    "<details>",
                    f"<summary>{ui['relevant_files_summary']}</summary>",
                    "",
                    ui["relevant_files_placeholder"],
                    "",
                    "</details>",
                ]
            )
            + "\n",
            encoding="utf-8",
        )

    (output_dir / "index.md").write_text("\n".join(index_lines).rstrip() + "\n", encoding="utf-8")


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        description="Scaffold .open_docs using the repo-wiki template or a scraped wiki JSON page plan (no paragraph copying)."
    )
    parser.add_argument(
        "--input",
        default="",
        help="Optional path to scraped wiki JSON (used only to extract page list). If omitted, uses bundled repo-wiki template page list.",
    )
    parser.add_argument(
        "--output",
        default=".open_docs",
        help="Output directory for Markdown scaffold (default: ./.open_docs)",
    )
    parser.add_argument(
        "--lang",
        default="auto",
        help="Language code to select from JSON (e.g. en, zh). Use 'auto' to detect from --query.",
    )
    parser.add_argument(
        "--query",
        default="",
        help="User query used for language auto-detection (only when --lang=auto).",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing page files (index.md is always overwritten).",
    )

    args = parser.parse_args(argv)

    lang = args.lang
    if lang == "auto":
        lang = detect_language_from_query(args.query)

    if args.input:
        input_path = Path(args.input)
        if input_path.exists():
            chosen_lang, plans = load_page_plans(input_path=input_path, lang=lang)
            plans = localize_page_plans(plans, lang=lang)
        else:
            chosen_lang, plans = default_page_plans(lang=lang)
            sys.stderr.write(f"Input JSON not found, using bundled template: {input_path}\n")
    else:
        chosen_lang, plans = default_page_plans(lang=lang)
    write_scaffold(output_dir=Path(args.output), plans=plans, force=bool(args.force), lang=lang)

    sys.stderr.write(
        f"Scaffolded {len(plans)} pages in {os.fspath(Path(args.output).resolve())} (template lang: {chosen_lang}, target: {lang})\n"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
