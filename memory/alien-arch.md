# Architecture: ALIEN Project

## Core Components
- **Record Processor:** Parses `PSRRecord` and `DemonstrationRecord`. This is the input ingestion layer.
- **Learner:** Includes `DocumentsIndexer`, `XMLLoader`, `JsonLoader`. This is the knowledge base ingestion.
- **Dataflow (The Brain):**
  - `WindowsAppEnv`: The environment wrapper (Simulated or Real).
  - `ExecuteFlow`: The main loop.
  - `ExecuteAgent`: The actor.
  - `ExecuteEvalAgent`: The critic/evaluator.

## Key Insight
The system separates **Demonstration Learning** (watching you) from **Execution** (doing it).
It uses a `ChooseTemplateFlow` -> `PrefillFlow` -> `ExecuteFlow` pipeline.

## Status
- **Code Quality:** High. Structure is modular (Agents vs. Flows).
- **Gap:** No explicit "Memory" persistence layer seen yet beyond basic indexing.
