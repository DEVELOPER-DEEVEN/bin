# Architecture: DataPulse & RAG

## DataPulse (Data Quality)
- **Core:** `DriftDetector` (KS Test, Chi-Square), `Monitor` (Expectations), `DataPulse` (Main Facade).
- **Validators:** `CheckType`, `ValidationResult`.
- **Status:** Solid foundation. The `DriftMethod` enum suggests extensibility.

## Inverse-RAG (Research)
- **Concept:** Inquiry-based System.
- **Components:**
  - `UserSimulator`: Simulates a user to train the system. (Clever).
  - `BeliefState` & `BeliefManager`: Bayesian-style state tracking?
  - `ProfileEvaluator`: The scorer.
- **Key Insight:** This isn't just "Search & Retrieve." It's a **Conversation State Machine**. It tries to understand the *user's belief* before retrieving.

## Synthesis
We have:
1. **ALIEN:** The Body (Execution).
2. **DataPulse:** The Eyes (Monitoring).
3. **Inverse-RAG:** The Mind (Belief/State).

## The Mega-Project
If we combine `ALIEN`'s agents with `Inverse-RAG`'s belief tracking, we get an agent that **knows what it doesn't know** and asks clarifying questions before acting.
