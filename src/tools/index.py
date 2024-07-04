from langchain_core.tools import tool
from ..utils.date import get_date

@tool
def get_current_date() -> str:
    "Get the current date."
    return get_date()

base_tools = [get_current_date]
base_tools_map = {
    "get_current_date": get_current_date
}

