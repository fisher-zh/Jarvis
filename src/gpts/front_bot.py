
from ..core import CoreChat

class Jarvis(CoreChat):
    def __init__(self):
        model="gpt-3.5-turbo"
        system_message = """"""
        super().__init__(model=model, system_message=system_message)
