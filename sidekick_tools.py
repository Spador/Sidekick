from tools.playwright_provider import PlaywrightProvider
from tools.file_provider import FileProvider
from tools.push_provider import PushProvider
from tools.search_provider import SearchProvider
from tools.wikipedia_provider import WikipediaProvider
from tools.python_repl_provider import PythonReplProvider


# Preserve original API
async def playwright_tools():
    provider = PlaywrightProvider()
    tools, browser, playwright = await provider.playwright_tools()
    return tools, browser, playwright


async def other_tools():
    tools = []
    tools += FileProvider().get_tools()
    tools += PushProvider().get_tools()
    tools += SearchProvider().get_tools()
    tools += PythonReplProvider().get_tools()
    tools += WikipediaProvider().get_tools()
    return tools