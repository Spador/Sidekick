from langchain_community.utilities.wikipedia import WikipediaAPIWrapper
from langchain_community.tools.wikipedia.tool import WikipediaQueryRun


class WikipediaProvider:
    def get_tools(self):
        wikipedia = WikipediaAPIWrapper()
        return [WikipediaQueryRun(api_wrapper=wikipedia)]