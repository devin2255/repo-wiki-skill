# Wiki Template (bundled)

This template is derived from a scraped product wiki and is bundled so the skill can produce a **complete, professional** project wiki even when the scraped JSON is not available at runtime.

## Core conventions

- Output directory: `./.open_docs`
- One page per file, plus `./.open_docs/index.md`
- Use the page ordering by `id`
- Every page includes a “Relevant source files” block (prefer the `<details>` style)
- Prefer diagrams (Mermaid) for architecture and flows
- If something is not present in the repo, write: “Not found in repo” / “Not applicable”

## Localization rules (must follow)

- The **page filename** and the page **H1 title** must match the user’s query language.
- The **section headings** should also be in the user’s language.
- Keep all technical tokens unchanged: file paths, command names, flags, env var names, identifiers.
- Do not defer content to another language (no “see English page for details”); write the page content fully in the target language.

### Canonical page titles (by language)

Use these titles for filenames/H1 (fallback to English only if the language is unsupported):

| id | English | 中文 |
|---:|---|---|
| 1 | Overview | 概述 |
| 1.1 | Quick Start | 快速开始 |
| 1.2 | Installation | 安装 |
| 1.3 | Key Concepts | 核心概念 |
| 2 | Architecture | 架构设计 |
| 2.1 | CLI System | CLI 系统 |
| 2.2 | Configuration System | 配置系统 |
| 2.3 | Environment Variable Management | 环境变量管理 |
| 2.4 | Protocol Translation Proxy | 协议转换代理 |
| 2.5 | Model Selection and IP Detection | 模型选择与 IP 检测 |
| 3 | User Guide | 用户指南 |
| 3.1 | Commands Reference | 命令参考 |
| 3.2 | Configuration Files | 配置文件 |
| 3.3 | Environment Variables | 环境变量 |
| 3.4 | Model Provider Setup | 模型/Provider 配置 |
| 3.5 | Troubleshooting | 故障排查 |
| 4 | Developer Guide | 开发者指南 |
| 4.1 | Project Structure | 项目结构 |
| 4.2 | Development Setup | 开发环境搭建 |
| 4.3 | Testing | 测试 |
| 4.4 | Code Style and Conventions | 代码风格与约定 |
| 4.5 | Contributing Guidelines | 贡献指南 |
| 5 | Reference | 参考 |
| 5.1 | CLI Module API | CLI 模块 API |
| 5.2 | Config Module API | 配置模块 API |
| 5.3 | Proxy Module API | 代理模块 API |
| 5.4 | Environment Module API | 环境模块 API |
| 5.5 | Configuration Schema | 配置 Schema |
| 6 | Advanced Topics | 高级主题 |
| 6.1 | Custom Proxy Configurations | 自定义代理配置 |
| 6.2 | Protocol Translation Details | 协议转换细节 |
| 6.3 | Windows Registry Integration | Windows 注册表集成 |
| 6.4 | Multi-Environment Deployments | 多环境部署 |

## Page set (canonical)

### 1. Overview

- `1 Overview`
  - Purpose and Scope
  - What is this project?
  - Core Capabilities (table with “Capability / Description / Where in code/config”)
  - System Architecture (Mermaid component diagram)
  - Key Components and Execution Flow (Mermaid sequence diagram)
  - Configuration Hierarchy (sources + precedence)
  - When to Use This Tool
- `1.1 Quick Start`
  - Prerequisites
  - Installation Steps (minimal)
  - Basic Usage (examples)
  - First Run Example
  - Common First-Time Issues
- `1.2 Installation`
  - Prerequisites
  - Installation Methods
  - Verify Installation
  - Troubleshooting
- `1.3 Key Concepts`
  - Core concepts / terminology
  - Data/control flow conceptually
  - Configuration priority/override model (if applicable)

### 2. Architecture

- `2 Architecture`
  - System Overview (diagram)
  - Architectural Layers
  - Execution Flow (sequence diagram)
  - Configuration/Data Flow
  - Key Design Patterns / Decisions
  - Inter-Component Dependencies
- `2.1 CLI System` (if there is CLI)
  - Entry points
  - Command routing
  - Typical command flows
  - Integration points (config, env, services)
- `2.2 Configuration System`
  - Configuration sources & precedence
  - File format/schema
  - Merge/override logic
  - Defaults and resolution rules
- `2.3 Environment Variable Management` (if applicable)
  - Persistence mechanism (OS-level if any)
  - Variable naming & meaning
  - Refresh/reload behavior
- `2.4 Protocol Translation Proxy` (if applicable)
  - Architecture & lifecycle
  - Request/response mapping
  - Streaming handling
  - Error handling / retries
  - Security: auth, key handling
- `2.5 Model Selection and IP Detection` (if applicable)
  - Detection flow
  - Selection logic
  - Configuration integration

### 3. User Guide

- `3 User Guide`
  - Getting Started
  - Core workflows
  - Common scenarios
  - Proxy / integration behavior (if any)
  - Next steps
- `3.1 Commands Reference`
  - Command syntax overview
  - Per-command docs: purpose, args, examples, outputs
  - Exit codes & errors
- `3.2 Configuration Files`
  - Location / discovery
  - Structure (with examples)
  - Overrides
  - Validation rules
- `3.3 Environment Variables`
  - Priority hierarchy
  - Input vs runtime output variables
  - Best practices & troubleshooting
- `3.4 Model Provider Setup` (or “Integrations Setup”)
  - Prereqs
  - Provider/integration configuration
  - Verification checklist
  - Common patterns
- `3.5 Troubleshooting`
  - Install issues
  - Permissions
  - Runtime / networking
  - Common errors
  - Debug commands / logging

### 4. Developer Guide

- `4 Developer Guide`
  - Dev workflow overview
  - Module architecture
  - Key dev areas
  - Testing strategy
  - Contribution workflow
- `4.1 Project Structure`
  - Repo layout
  - Entry points and bootstrapping
  - Module dependencies map (diagram optional)
- `4.2 Development Setup`
  - Prereqs
  - Local install steps
  - Common dev commands
  - Environment setup
- `4.3 Testing`
  - Test types & how to run
  - Fixtures/test data
  - CI notes if present
- `4.4 Code Style and Conventions`
  - Language/runtime standards
  - Naming conventions
  - Error handling patterns
  - Project-specific patterns
- `4.5 Contributing Guidelines`
  - Contribution types
  - PR checklist
  - Code review expectations

### 5. Reference

- `5 Reference`
  - Module dependencies
  - Key constants/defaults
  - Data flow chains
  - Error handling patterns
- `5.1 CLI Module API` (if applicable)
- `5.2 Config Module API` (if applicable)
- `5.3 Proxy Module API` (if applicable)
- `5.4 Environment Module API` (if applicable)
- `5.5 Configuration Schema`
  - Schema diagram
  - Field descriptions
  - Example config
  - Validation rules

### 6. Advanced Topics

- `6 Advanced Topics`
  - Advanced configuration patterns
  - Deep-dive architecture details
  - Fallback strategies
  - Recommendations for advanced users
- `6.1 Custom Proxy Configurations` (if applicable)
- `6.2 Protocol Translation Details` (if applicable)
- `6.3 Windows Registry Integration` (or platform-specific persistence) (if applicable)
- `6.4 Multi-Environment Deployments`
  - Environment-specific configs
  - Secrets management
  - Deployment workflows
  - Best practices

## “Relevant source files” block (preferred)

Use this pattern (adapt language as needed):

```md
<details>
<summary>Relevant source files</summary>

- `path/to/file1`
- `path/to/file2`

</details>
```
