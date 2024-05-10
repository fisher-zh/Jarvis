from langchain_core.tools import tool
from langchain.tools.render import render_text_description
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_openai import ChatOpenAI
from operator import itemgetter


@tool
def multiply(first_int: int, second_int: int) -> int:
    """Multiply two integers together."""
    return first_int * second_int


@tool
def add(first_int: int, second_int: int) -> int:
    "Add two integers."
    return first_int + second_int


@tool
def exponentiate(base: int, exponent: int) -> int:
    "Exponentiate the base to the exponent power."
    return base**exponent


tools = [add, exponentiate, multiply]


def tool_chain(model_output):
    tool_map = {tool.name: tool for tool in tools}
    chosen_tool = tool_map[model_output["name"]]
    return itemgetter("arguments") | chosen_tool


class Jarvis:
    def __init__(self, model="gpt-3.5-turbo"):
        rendered_tools = render_text_description(tools)
        system_prompt = f"""You are an assistant that has access to the following set of tools. Here are the names and descriptions for each tool:

        {rendered_tools}

        Given the user input, return the name and input of the tool to use. Return your response as a JSON blob with 'name' and 'arguments' keys."""

        prompt = ChatPromptTemplate.from_messages(
            [("system", system_prompt), ("user", "{input}")]
        )

        model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
        self.chain = prompt | model | JsonOutputParser() | tool_chain
    
    def question(self, user_input):
        res = self.chain.invoke({"input": user_input})
        return res

