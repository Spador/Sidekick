from abc import ABC, abstractmethod
from typing import List, Any


class AsyncToolProvider(ABC):
    @abstractmethod
    async def get_tools_async(self) -> List[Any]:
        ...


class ToolProvider(ABC):
    @abstractmethod
    def get_tools(self) -> List[Any]:
        ...