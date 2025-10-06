from langchain_experimental.tools import PythonREPLTool


class PythonReplProvider:
    def get_tools(self):
        python_repl = PythonREPLTool()
        return [python_repl]