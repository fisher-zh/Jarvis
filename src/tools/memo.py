from langchain_core.tools import tool
from langchain.pydantic_v1 import BaseModel, Field
from typing import Optional
import json
from ..utils.memo import add_memo as utils_add_memo, query_memo as utils_query_memo
from .date import get_current_date

descriptions = {
    "content": "Memo Contents",
    "execute": "The date the memo was executed, in the format YYYY-MM-DD"
}

class AddMemoInput(BaseModel):
    content: str = Field(description=descriptions["content"])
    execute: str = Field(description=descriptions["execute"])
    tips: Optional[str] = Field(None, description="Memo Tips, Not required")

@tool("add_memo", args_schema=AddMemoInput)
def add_memo(content: str, execute: str, tips: Optional[str] = None) -> str:
    "Add a memo."
    utils_add_memo(content, execute, tips)
    return "add memo success"


class QueryMemoInput(BaseModel):
    content: str = Field(None, description=descriptions["content"])
    execute: str = Field(None, description=descriptions["execute"])

@tool("query_memo", args_schema=QueryMemoInput)
def query_memo(content: Optional[str] = None, execute: Optional[str] = None) -> str:
    "Query memos and return a list of matching memos in a string"
    result = utils_query_memo(content=content, execute=execute)
    return json.dumps(result)


memo_tools = [get_current_date, add_memo, query_memo]
memo_tools_map = {
    "get_current_date": get_current_date,
    "add_memo": add_memo,
    "query_memo": query_memo,
}

