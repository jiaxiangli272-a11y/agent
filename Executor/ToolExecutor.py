from typing import Dict, Any


class ToolExecutor:
    def __init__(self):
        self.tools:Dict[str,Dict[str,Any]]={}
    def register(self, tool):
'''
向工具箱中注入一个工具
'''


