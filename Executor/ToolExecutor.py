from typing import Dict, Any


class ToolExecutor:
    def __init__(self):
        self.tools:Dict[str,Dict[str,Any]]={}
    def register(self, name: str, description: str, func: callable):
        '''
        向工具箱中注入一个工具
        '''
        if name in self.tools:
            print('工具已经存在')
        self.tools[name] = {"description":description, "func":func}
        print(f"工具{name}已经注册")
    def getTool(self, name: str):
        return self.tools[name].get("func")
    def getAvailableTools(self):
        return "\n".join([
            f"-name{name}:{info['description']}" for name, info in self.tools.items()
        ])



