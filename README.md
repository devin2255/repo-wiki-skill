# Repo Wiki

A Claude Code skill for generating comprehensive, multi-page project wikis from repository analysis.

## Overview

This skill generates professional, multi-page Markdown wikis for any repository using a structured template approach. It analyzes the current repository's code, configuration, and documentation to produce grounded, accurate documentation in your preferred language.

## Features

- **Multi-language support**: Automatically detects language from query (English, Chinese, Japanese, Korean, Russian)
- **Structured output**: Generates wiki pages following a professional template structure
- **Repository-grounded**: All content is based on actual code and files in your repository
- **Professional completeness**: Covers overview, architecture, user guide, developer guide, reference, and advanced topics

## Installation

这是一个可用于多种客户端的技能，请放到对应目录：

```bash
mkdir -p ~/.claude/skills/repo-wiki
cp -r repo-wiki/* ~/.claude/skills/repo-wiki/
mkdir -p ~/.codex/skills/repo-wiki
cp -r repo-wiki/* ~/.codex/skills/repo-wiki/
mkdir -p ~/.opencode/skill/repo-wiki
cp -r repo-wiki/* ~/.opencode/skill/repo-wiki/
```

## Usage

Once installed, invoke the skill in your client (Claude Code/Codex/OpenCode):

```
/repo-wiki 为这个项目生成中文文档
```

Or in English:

```
/repo-wiki Generate documentation for this project
```

### Helper Script

Use the scaffold script from the installed path to create the wiki structure:

```bash
python <skill_dir>/scripts/scaffold_open_docs.py --query "生成中文文档"
```

## Output Structure

The skill generates documentation in `./.open_docs/`:

- `index.md` - Wiki index with links to all pages
- `1-Overview.md` - Project overview
- `2-Architecture.md` - System architecture
- `3-User-Guide.md` - User documentation
- `4-Developer-Guide.md` - Developer documentation
- `5-Reference.md` - API reference
- `6-Advanced-Topics.md` - Advanced usage

## File Structure

```
repo-wiki/
├── SKILL.md                      # Skill definition and workflow
├── scripts/
│   └── scaffold_open_docs.py     # Helper script for scaffolding
├── references/
│   ├── wiki-template.md          # Template page structure
│   └── wiki-json-format.md       # JSON format reference
└── README.md                     # This file
```

## Requirements

- Python 3.8+
- A supported client (Claude Code, Codex, OpenCode)

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.
