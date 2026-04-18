import HelloAgent
from Executor.ToolExecutor import ToolExecutor

# ReAct 提示词模板
REACT_PROMPT_TEMPLATE = """
请注意，你是一个有能力调用外部工具的智能助手。

可用工具如下:
{tools}

请严格按照以下格式进行回应:

Thought: 你的思考过程，用于分析问题、拆解任务和规划下一步行动。
Action: 你决定采取的行动，必须是以下格式之一:
- `{{tool_name}}[{{tool_input}}]`:调用一个可用工具。
- `Finish[最终答案]`:当你认为已经获得最终答案时。
- 当你收集到足够的信息，能够回答用户的最终问题时，你必须在Action:字段后使用 Finish[最终答案] 来输出最终答案。

现在，请开始解决以下问题:
Question: {question}
History: {history}
"""

class ReactAgent:
    def __init__(self,llm_client:HelloAgent,tool_excutor:ToolExecutor,max_steps=5):
        self.llm_client = llm_client
        self.tool_excutor = tool_excutor
        self.max_steps = max_steps
        self.history=[]
    def run(self,question:str):
        '''
        运行一个React智能体来回答一个问题
        '''
        self.history=[]
        current_step = 0
        while current_step < self.max_steps:
            print(f"----第{current_step}----")
            # 获取可用工具
            tools = ToolExecutor.getAvailableTools()
            history_str="\n".join(self.history)
            # 格式化提示词
            prompt = REACT_PROMPT_TEMPLATE.format(tools=tools, question=question, history=history_str)
            # 调用llm进行思考
            message=[{"role":"user","content":prompt}]
            response = self.llm_client.think(message)
            if response is None:
                print('大模型没有输出')
