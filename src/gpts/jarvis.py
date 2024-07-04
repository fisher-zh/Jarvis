from langchain_core.tools import tool

from langchain.pydantic_v1 import BaseModel, Field
from .core import CoreToolChat
from .system_bot import SystemBot
from .meno_bot import MemoBot


@tool
def system_bot(requirements: str) -> str:
    """Execute tasks on the system according to the requirements and return the results."""
    bot = SystemBot()
    result = bot.q(requirements)
    return result.content


class MemoBotInput(BaseModel):
    requirements: str = Field(description="Clearly describe the requirements for the memorandum, and the execution time of the memorandum items is mandatory.")

@tool("memo_bot", args_schema=MemoBotInput)
def memo_bot(requirements: str) -> str:
    """According to the requirements: Create, Read, Update, and Delete Memorandum."""
    bot = MemoBot()
    result = bot.q(requirements)
    return result.content



tools = [system_bot, memo_bot]
tools_map = {
    **{
        "system_bot": system_bot,
        "memo_bot": memo_bot
    }
}

class Jarvis(CoreToolChat):
    def __init__(self, model="gpt-3.5-turbo"):
        system_message = "You are a helpful assistant."
        super().__init__(model=model, system_message=system_message, tools=tools, tools_map=tools_map)
    
