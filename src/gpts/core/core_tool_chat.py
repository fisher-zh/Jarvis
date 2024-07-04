from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage ,ToolMessage

class CoreToolChat:
    def __init__(self, system_message, tools, tools_map, model="gpt-3.5-turbo"):

        llm = ChatOpenAI(model=model, temperature=0)
        self.system_message = system_message
        self.llm_with_tools = llm.bind_tools(tools)
        self.tools_map = tools_map
    

    def chain_tool_call(self, messages):
        ai_msg = self.llm_with_tools.invoke(messages)
        messages.append(ai_msg)
        print(ai_msg)
        if (ai_msg.tool_calls):
            for tool_call in ai_msg.tool_calls:
                selected_tool = self.tools_map[tool_call["name"].lower()]
                tool_output = selected_tool.invoke(tool_call["args"])
                messages.append(ToolMessage(tool_output, tool_call_id=tool_call["id"]))
            return self.chain_tool_call(messages)
        else:
            return ai_msg

    # question
    def q(self, query):
        messages = [
            SystemMessage(content=self.system_message),
            HumanMessage(query)
        ]
        result = self.chain_tool_call(messages)
        return result
        

