# Sidekick — Your Personal Co-Worker

Sidekick is a LangGraph-powered autonomous teammate that blends tool-augmented reasoning with a personalised feedback cycle. It is designed to feel like a dedicated co-worker that keeps iterating on a task until it either satisfies your success criteria or surfaces the questions it needs answered.

## Why Sidekick Feels Personal
- **Success criteria first:** Every run is anchored on the success criteria you provide. The assistant keeps those guardrails in its system prompt so it can tailor its work and know when to stop.
- **Evaluator feedback loop:** A separate evaluator model inspects each draft answer, comparing it with your criteria. If the bar is missed, the worker receives the evaluator’s feedback and continues improving instead of giving up.
- **Session memory:** Each UI session is tagged with a unique `sidekick_id`. LangGraph’s checkpointer (currently in-memory) keeps the conversation and tool traces tied to your session so the agent stays in context while you iterate.
- **Push nudges:** With Pushover credentials, the `send_push_notification` tool lets Sidekick tap you on the shoulder when it finishes a milestone or needs you urgently.

## High-Level Architecture
1. **Gradio front-end (`app.py`):** Provides the Sidekick chat interface with fields for both your request and success criteria.
2. **Core orchestrator (`sidekick/core/sidekick_core.py`):** Builds a LangGraph state machine with three major nodes:
   - `worker`: a `ChatOpenAI` model bound to the toolset.
   - `tools`: a LangChain `ToolNode` that executes any tool call emitted by the worker.
   - `evaluator`: a second `ChatOpenAI` model producing structured `EvaluatorOutput` that decides if success criteria are met or if more user input is required.
3. **Routing logic:** The graph loops between worker → tools → evaluator until either the evaluator declares success or needs clarification from you, finishing the run.
4. **Storage (`sidekick/core/storage`):** Currently uses LangGraph’s `MemorySaver`, but the project ships with a SQLite database scaffold so you can swap in persistent checkpoints when needed.

## Tooling Arsenal
All tools are registered in `sidekick_tools.py` and come from dedicated providers under `tools/`:

| Provider | Tool(s) | What it enables |
| --- | --- | --- |
| `PlaywrightProvider` | Full Playwright browser toolkit | Real browser automation for scraping, form filling, and complex web navigation. |
| `FileProvider` | LangChain File Management Toolkit (rooted at `sandbox/`) | Read, list, and write files safely inside the sandbox directory. |
| `PushProvider` | `send_push_notification` (Pushover) | Send yourself instant push alerts straight from the agent. |
| `SearchProvider` | `search` (Google Serper API) | Run live web searches and pull fresh results into the conversation. |
| `WikipediaProvider` | `WikipediaQueryRun` | Summarise or deep-dive into Wikipedia topics without leaving Sidekick. |
| `PythonReplProvider` | `PythonREPLTool` | Spin up on-the-fly Python snippets for analysis, calculations, or data wrangling. |

Each tool is described for the model and can be extended by dropping new providers into the `tools/` package.

## Concepts and Technologies
- **LangGraph** orchestrates the recurrent workflow and success-evaluator loop.
- **LangChain** toolkits supply high-level integrations for browsing, search, file I/O, and Python execution.
- **OpenAI GPT-4o mini** models provide both the worker intelligence and the evaluator’s structured judgements.
- **Playwright** gives the agent a real Chromium browser (launched non-headless by default) for reliable automation.
- **Gradio** delivers an easy local UI, complete with lifecycle hooks to initialise and clean up browser resources.
- **Dotenv configuration** loads API keys (Serper, Pushover, OpenAI, etc.) so you can personalise the toolbelt to your own accounts.

## Typical Flow
1. You open the Gradio UI, describe the task, and spell out the success criteria.
2. Sidekick’s worker model plans the next step—calling tools whenever it needs outside context.
3. After each assistant reply, the evaluator inspects the draft against your success criteria.
4. If the bar isn’t met, the worker receives the evaluator’s feedback and keeps going; otherwise it wraps up with a confident, criteria-aware answer or a precise question back to you.

## Extending Sidekick
- Add more providers in `tools/` to expand the agent’s abilities (e.g., calendar APIs, data warehouses, custom knowledge bases).
- Swap `MemorySaver` for a persistent LangGraph checkpointer to resume work across sessions.
- Adjust `PlaywrightProvider` to run headless in production or route through a proxy for geo-specific browsing.
- Tailor the UI in `app.py`—for example, preloading task templates or wiring it into a larger productivity dashboard.

With this architecture, Sidekick becomes more than a chatbot—it’s a personal operations partner that remembers what “done” looks like for you and won’t stop iterating until it gets there.
