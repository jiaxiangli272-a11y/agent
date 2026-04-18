import os
from dotenv import load_dotenv
from Executor.ToolExecutor import ToolExecutor
from tools.search import search

# 1. 获取当前脚本 (tooTest.py) 所在的绝对路径目录
current_dir = os.path.dirname(os.path.abspath(__file__))
# 2. 拼接出 .env 文件的绝对路径
env_path = os.path.join(current_dir, '.env')

# 3. 强制加载该路径下的 .env 文件，并允许覆盖已有的环境变量
load_dotenv(dotenv_path=env_path, override=True)

if __name__ == "__main__":
    # 初始化工具执行器
    executor = ToolExecutor()

    # 注册搜索工具
    search_description = "一个网页搜索工具"
    executor.register("Search", search_description, search)

    # 智能体调用
    print("\n--- 执行 Action: Search['英伟达最新的GPU型号是什么'] ---")
    tool_name = "Search"
    tool_input = "英伟达最新的GPU型号是什么"
    tool_function = executor.getTool(tool_name)

    if tool_function is None:
        print("发生错误,没有此工具")
    else:
        # 这里会执行 tools/search.py 里面的 search 函数
        observant = tool_function(query=tool_input)
        print(observant)