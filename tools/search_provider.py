from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain.agents import Tool

_serper = GoogleSerperAPIWrapper()


class SearchProvider:
    def get_tools(self):
        return [
            Tool(
                name="search",
                func=_serper.run,
                description="Use this tool when you want to get the results of an online web search",
            )
        ]