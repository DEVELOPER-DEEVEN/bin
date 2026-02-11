# LITT_MEMORY.md - The Long-Term Memory of Litt

## 🧠 Knowledge Graph
*(This file persists across sessions. Litt writes to it after every victory or defeat.)*

### 🏗️ Project Architectures
- **googleapis/mcp-toolbox-sdk-python:**
  - Build: `uv` / `make`.
  - Lint: `black .` AND `ruff check . --fix`.
  - CI: Cloud Build (Logs hidden). Trust the Status Check.
- **langchain-ai/langchain:**
  - Monorepo. Tests run via `make test`.
  - Lint: strict `mypy`.
- **Significant-Gravitas/AutoGPT:**
  - Python 3.10+ strict.

### ⚔️ Battle Scars (Lessons Learned)
- **Lesson 1:** Never trust `gh run view` on Google repos. It 404s. Use `gh pr checks`.
- **Lesson 2:** Auth fails if you use the wrong token. Always check `gh auth status` first.
- **Lesson 3:** If a linter fails, fixing it is P0. Code logic doesn't matter if style fails.

### 📝 Active Context
- **Current Identity:** `developer-deeven`
- **Preferred Model:** `google-gemini-cli/gemini-3-pro-preview`
