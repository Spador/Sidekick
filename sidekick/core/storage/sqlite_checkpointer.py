from langgraph.checkpoint.memory import MemorySaver


def build_memory_checkpointer() -> MemorySaver:
    """
    Returns the default in-memory checkpointer used by LangGraph.
    """
    return MemorySaver()