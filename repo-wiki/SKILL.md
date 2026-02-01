---
name: scraped-wiki-generator
description: Generate a complete, professional multi-page project wiki for the current repository, using a bundled template derived from a scraped product wiki. Output language and page titles/filenames must match the user's query language. Output goes to ./.open_docs.
---

# Scraped Wiki Generator

Generate a multi-page Markdown wiki for the **current repository**, using a built-in wiki template derived from a scraped product wiki.

You do **not** need the scraped JSON at runtime: the template structure is bundled in this skill under `references/`.

## Non-negotiables

- **Grounding**: All factual technical content must come from the **current repo** (code/config/docs). Do not invent modules, features, commands, or paths.
- **Language**: Output language must match the user's query language (auto-detect). If the user explicitly requests a language, that overrides auto-detection.
- **No language handoff**: Do **not** write pages that defer content to another language (e.g. “see English page for details”). The page content itself must be written fully in the target language; keep technical tokens unchanged (paths/commands/identifiers/env vars).
- **Professional completeness**: Follow the template page set and section checklists to produce a complete, professional wiki (overview → architecture → user guide → developer guide → reference → advanced topics).
- **Style mimic (not copying)**: Mimic the template’s **structure, tone, and section patterns**. Do not copy third‑party paragraphs verbatim unless the user confirms they have rights to do so.
- **Output location**: Always write Markdown pages to `./.open_docs` in the current project.

If the user asks to reproduce third‑party content verbatim and you are not sure they have rights to do so, refuse to copy verbatim and produce an original, repo-grounded wiki that matches the style/structure.

## Template references (bundled)

- Template page set + per-page section checklist: `references/wiki-template.md`
- Scraped JSON format (optional, only if you want to refresh/compare): `references/wiki-json-format.md`

## Output

- Output directory: `./.open_docs`
- Always create `./.open_docs/index.md` linking to all pages in order.
- Create one Markdown file per page.

## Workflow

1) **Determine target language**

- Detect from the user's query (e.g., Chinese query → Chinese output; English query → English output).
- If ambiguous/mixed, ask a single clarification question.

2) **Plan the wiki using the bundled template**

- Use `references/wiki-template.md` as the canonical structure (pages + required sections).
- Ensure page titles and filenames follow the user's query language, per `references/wiki-template.md`.
- If the repo clearly lacks a concept (e.g., no API, no CLI), keep the page but mark the relevant sections as "Not found in repo" / "Not applicable".

3) **Collect repo evidence**

- Read the minimum set of authoritative files per page and keep a per-page "Relevant source files" list:
  - top-level docs (`README*`, `docs/`, `CHANGELOG*`)
  - manifests (`pyproject.toml`, `package.json`, etc.)
  - entry points / CLI (`src/`, `scripts/`, `bin/`)
  - configuration files and examples
  - CI/CD (`.github/workflows`, pipelines) if present

4) **Write `.open_docs` Markdown files following the template**

- Keep page order stable (follow the template `id` order).
- File naming: prefix with the template `id` to keep ordering (e.g., `1-概述.md`, `2-架构设计.md`).
- Ensure internal links in `index.md` point to the generated filenames.
- Include a "Relevant source files" block (prefer the `<details><summary>...</summary> ... </details>` style used in the template).

## Optional helper script (deterministic dump)

Use this when you want to scaffold `./.open_docs` (page files + index) from the **built-in template** (no JSON required), then fill in content based on the current repo:

`python .codex/skills/scraped-wiki-generator/scripts/scaffold_open_docs.py --query "<user query>"`

If you have a scraped JSON page plan (optional), pass `--input <path-to-json>` to extract the page list (the wiki content is still written from the current repo).

This script scaffolds filenames and `index.md`; it does not copy third‑party paragraphs.
