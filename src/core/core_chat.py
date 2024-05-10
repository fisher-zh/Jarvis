from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage


class CoreChat:
    def __init__(self, system_message, model="gpt-3.5-turbo"):
        self.chat = ChatOpenAI(model=model)
        self.system_message = system_message

    def question(self, content):
        res = self.chat.invoke([
            SystemMessage(content=self.system_message),
            HumanMessage(content=content)
        ])
        return res.content
