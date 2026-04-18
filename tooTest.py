from Executor.ToolExecutor import ToolExecutor
from tools.search import search

if __name__ == "__main__":
    # 初始化工具执行器
    executor = ToolExecutor()

    # 注册搜索工具
    search_description="一个网页搜索工具"
    executor.register("Search", search_description,search)

    # 智能体调用
    print("\n--- 执行 Action: Search['英伟达最新的GPU型号是什么'] ---")
    tool_name = "Search"
    tool_input = "英伟达最新的GPU型号是什么"
    tool_function = executor.getTool(tool_name)
    if tool_function is None:
        print("发生错误,没有此工具")
    else:
        observant = tool_function(tool_input)
        print(observant)