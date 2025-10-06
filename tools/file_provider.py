from langchain_community.agent_toolkits import FileManagementToolkit


class FileProvider:
    def get_tools(self):
        toolkit = FileManagementToolkit(root_dir="sandbox")
        return toolkit.get_tools()