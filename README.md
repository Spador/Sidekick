# Sidekick

🌱 **Your personal co-worker for tool-augmented problem solving.**

Sidekick is an autonomous teammate that combines LangGraph routing with a curated toolbox—browser automation, search, file I/O, Python execution, and push notifications—to help you ship results faster. It keeps iterating until it meets the success criteria you set or surfaces the clarifications it needs.

## Overview
- **Personalised workflows:** Every run starts with your success criteria, which are reinforced inside the agent’s system prompt so the assistant knows when it is done.
- **Evaluator loop:** A second model audits each draft reply. If it spots gaps, the worker receives structured feedback and continues improving instead of stopping early.
- **Session awareness:** A unique `sidekick_id` and LangGraph’s checkpointing keep the conversation coherent within a session. Swap in a persistent backend to resume across restarts.
- **Real-world reach:** From Playwright-powered browsing to push notifications via Pushover, Sidekick reaches beyond text generation to act on your behalf.

## Quick Summary
Sidekick launches a Gradio chat interface where you describe the task and define success. The agent plans, calls tools through LangChain integrations, evaluates its own work, and keeps iterating until it satisfies your criteria or asks you for input. The project is structured for easy extension—drop in new tool providers or upgrade the checkpointer to make it even more personal.

## Architecture
```
Gradio UI ──▶ Sidekick Core (LangGraph)
             ├─ Worker (ChatOpenAI + tools)
             ├─ Tool Node (LangChain ToolNode)
             └─ Evaluator (ChatOpenAI structured output)
```
- **Worker node:** `ChatOpenAI` (`gpt-4o-mini`) bound to the toolset assembled in `sidekick_tools.py`.
- **Tool node:** Executes any tool calls emitted by the worker via LangChain’s `ToolNode`.
- **Evaluator node:** Another `ChatOpenAI` instance returning `EvaluatorOutput` to decide whether the success criteria are met or user input is required.
- **Checkpointing:** Currently uses `MemorySaver`; the repo ships with a SQLite stub so you can persist conversations with minimal changes.

## Toolbelt
All tools are collected in `sidekick_tools.py` and provided via dedicated classes under `tools/`:
- **Browser automation (`PlaywrightProvider`):** Full Playwright toolkit for real Chromium browsing (non-headless by default).
- **File management (`FileProvider`):** Read/write/list files inside the `sandbox/` directory safely.
- **Push notifications (`PushProvider`):** `send_push_notification` powered by Pushover—great for nudging yourself when a run completes.
- **Web search (`SearchProvider`):** Live search via Google Serper API.
- **Knowledge lookup (`WikipediaProvider`):** `WikipediaQueryRun` for quick encyclopedic context.
- **On-the-fly coding (`PythonReplProvider`):** Execute Python snippets for numerical work or quick data wrangling.

Add your own providers by following the same pattern—implement `get_tools()` (or `get_tools_async()` for async providers) and register them in `sidekick_tools.py`.

## Getting Started

### 1. Clone and install
```bash
uv sync  # or pip install -r requirements.txt
```
Dependencies require Python 3.12+.

### 2. Configure environment
Create a `.env` file (or export environment variables) with the credentials you plan to use:
```
OPENAI_API_KEY=...
SERPER_API_KEY=...
PUSHOVER_TOKEN=...
PUSHOVER_USER=...
```
Any missing credential simply disables that capability.

### 3. Launch the app
```bash
python app.py
```
Gradio opens a local interface (launches Playwright’s Chromium browser as needed). Enter your task and success criteria, then hit **Go!**

## Personalising Sidekick
- **Success templates:** Preload default success criteria in `app.py` to match your workflows.
- **Tool customisation:** Add knowledge bases, ticketing systems, CRMs, or any internal API by creating new providers.
- **Persistence:** Replace `MemorySaver` with a SQLite or cloud-backed checkpointer to persist multi-session projects.
- **Automation style:** Adjust `PlaywrightProvider` to run headless, go through proxies, or control different browsers.

## Development Notes
- Project targeting: defined in `pyproject.toml` with modern LangChain/LangGraph integrations.
- Notebook `test.ipynb` is included for ad-hoc experiments.
- The `sandbox/` directory is the safe workspace for file operations triggered by the agent.

## Acknowledgements
- **LangGraph** for the graph-based agent orchestration pattern.
- **LangChain** community toolkits for ready-made integrations.
- **OpenAI** for GPT-4o mini access powering both worker and evaluator models.
- **Playwright** for robust browser automation.
- **Gradio** for the rapid UI scaffold.

If you extend Sidekick or plug it into your own operations stack, we’d love to hear how you made it even more personal.
