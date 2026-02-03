# Repo Wiki

Claude Code 技能：基于仓库分析生成完整、多页面的项目 Wiki。

## 概述

该技能使用结构化模板为任意仓库生成专业的多页面 Markdown Wiki。它会分析当前仓库的代码、配置和文档，并根据你的语言偏好生成有依据、准确的文档内容。

## 特性

- **多语言支持**：可根据请求自动识别语言（英语、中文、日语、韩语、俄语）
- **结构化输出**：按专业模板结构生成 Wiki 页面
- **基于仓库内容**：所有内容来自仓库中的实际代码与文件
- **专业完整性**：覆盖概览、架构、用户指南、开发者指南、参考与高级主题

## 安装

这是一个可用于多种客户端的技能，请放到对应目录：

```bash
mkdir -p ~/.claude/skills/repo-wiki
cp -r repo-wiki/* ~/.claude/skills/repo-wiki/
mkdir -p ~/.codex/skills/repo-wiki
cp -r repo-wiki/* ~/.codex/skills/repo-wiki/
mkdir -p ~/.opencode/skill/repo-wiki
cp -r repo-wiki/* ~/.opencode/skill/repo-wiki/
```

## 使用方法

安装后，在支持的客户端中调用该技能（Claude Code/Codex/OpenCode）：

```
/repo-wiki 为这个项目生成中文文档
```

或使用英文：

```
/repo-wiki Generate documentation for this project
```

### 辅助脚本

使用安装路径中的 scaffold 脚本创建 Wiki 结构：

```bash
python <skill_dir>/scripts/scaffold_open_docs.py --query "生成中文文档"
```

## 输出结构

该技能会在 `./.open_docs/` 中生成文档：

- `index.md` - Wiki 索引（包含所有页面链接）
- `1-Overview.md` - 项目概览
- `2-Architecture.md` - 系统架构
- `3-User-Guide.md` - 用户文档
- `4-Developer-Guide.md` - 开发者文档
- `5-Reference.md` - API 参考
- `6-Advanced-Topics.md` - 高级用法

## 文件结构

```
repo-wiki/
├── SKILL.md                      # 技能定义与流程
├── scripts/
│   └── scaffold_open_docs.py     # 用于生成结构的辅助脚本
├── references/
│   ├── wiki-template.md          # 模板页面结构
│   └── wiki-json-format.md       # JSON 格式参考
└── README.md                     # 本文件
```

## 运行要求

- Python 3.8+
- 支持的客户端（Claude Code / Codex / OpenCode）

## 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件。

## 贡献

欢迎贡献！请提交 issue 或 pull request。
