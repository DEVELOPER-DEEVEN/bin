# DevX Strategy & Roadmap

## Mission
Establish Deeven Seru as a top-tier Systems & AI engineer via visible, high-impact open-source PRs on major frameworks.

## Operating Principles (CRITICAL UPDATE)
- **STRICT MANDATE:** You will not move to any new projects or tasks until ALL previous PRs have successful CI checks.
- **CI FIRST:** Every run must start by checking the status of all open PRs using `gh pr checks`.
- **DEBUG & FIX:** If checks are failing, you must analyze the logs, fix the code, and re-push until they are GREEN.
- **WAIT FOR SUCCESS:** You are authorized to idle or wait if a check is in progress. Do not context switch.

## PRIORITY INTERRUPT (Action Required)
**HIGH PRIORITY TARGET:** `googleapis/mcp-toolbox-sdk-java`
- **Issue #1:** https://github.com/googleapis/mcp-toolbox-sdk-java/issues/1
- **Direct Order:** Assign to self. Analyze immediately. Fix/Implement as requested.
- **Status:** **NEW**.

## Open PR Queue
### 1. AutoGPT (Significant-Gravitas/AutoGPT)
- **PR #12028:** [fix(blocks): allow falsy entries in AddToListBlock](https://github.com/Significant-Gravitas/AutoGPT/pull/12028)
- **PR #12048:** [Handle errors in Jina ExtractWebsiteContentBlock](https://github.com/Significant-Gravitas/AutoGPT/pull/12048)
- **PR #12027:** [ci: target pyright at Python 3.13](https://github.com/Significant-Gravitas/AutoGPT/pull/12027)

### 2. LangChain (langchain-ai/langchain)
- **PR #35115:** [fix: handle self kwarg in StructuredTool inputs](https://github.com/langchain-ai/langchain/pull/35115)
- **PR #35114:** [fix: filter duplicates in BaseChatMemory list_messages](https://github.com/langchain-ai/langchain/pull/35114)
- **PR #35112:** [fix: handle empty input in MultiPromptChain](https://github.com/langchain-ai/langchain/pull/35112)

## Daily Rhythm
1. **PRIORITY:** Check/Work on `googleapis/mcp-toolbox-sdk-java/issues/1`.
2. Check CI status for all PRs listed above.
3. Fix all red checks.
4. Verify fixes.
5. Report status.
