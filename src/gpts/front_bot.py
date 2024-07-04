
from .core import CoreChat

class FrontUnitTestBot(CoreChat):
    def __init__(self):
        model="gpt-3.5-turbo"
        system_message = """你是一个前端专家"""
        super().__init__(model=model, system_message=system_message)
