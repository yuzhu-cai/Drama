from utils import DefaultLLM
from utils.llm_call import OpenAILLM

class BaseAgent:
    def __init__(
            self,
            llm: OpenAILLM = DefaultLLM
    ):
        self.llm = llm
    
    def chat(self, query):
        return self.llm.call(query)