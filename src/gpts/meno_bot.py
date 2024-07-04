from core import CoreToolChat
from ..tools.memo import memo_tools, memo_tools_map


tools = memo_tools
tools_map = memo_tools_map

class MemoBot(CoreToolChat):
    def __init__(self):
        model="gpt-3.5-turbo"
        system_message = """You are an excellent memo assistant."""
        super().__init__(model=model, system_message=system_message, tools=tools, tools_map=tools_map)
