from core import CoreToolChat
import subprocess
from langchain_core.tools import tool

@tool
def run_shell(command:str) -> str:
    """Run shell."""
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error executing command: {e.stderr}"


tools = [run_shell]
tools_map = {
    "run_shell": run_shell
}

class SystemBot(CoreToolChat):
    def __init__(self):
        model="gpt-3.5-turbo"
        system_message = """You are a shell expert, completing tasks by executing various shell commands"""
        super().__init__(model=model, system_message=system_message, tools=tools, tools_map=tools_map)
