import ast
from utils.llm_call import OpenAILLM
from agents.base_agent import BaseAgent
from config.prompts import math_system, code_system, orginzer_system, work_template
from utils.parse import extract_json

class MathAgent(BaseAgent):
    def __init__(
            self, 
            llm: OpenAILLM
    ):
        super().__init__(llm)


class CodeAgent(BaseAgent):
    def __init__(
            self, 
            llm: OpenAILLM
    ):
        super().__init__(llm)


class Organizer(BaseAgent):
    def __init__(
            self, 
            llm: OpenAILLM
    ):
        super().__init__(llm)

    def chat_mt(self, messages: list):
        return self.llm.mt_call(messages)

class Drama:
    def __init__(self):
        self.math_llm = OpenAILLM(system_prompt=math_system)
        self.code_llm = OpenAILLM(system_prompt=code_system)
        self.organizer_llm = OpenAILLM(system_prompt=orginzer_system)
        
        self.math_agent = MathAgent(self.math_llm)
        self.code_agent = CodeAgent(self.code_llm)
        self.organizer_agent = Organizer(self.organizer_llm)

    def run(self, query: str):
        instruct = work_template.format(query=query)
        json_str = extract_json(self.organizer_agent.chat(instruct))
        workflow = ast.literal_eval(json_str)

        subtasks = workflow['tasks']
        if workflow['type'] == 'code':
            messages = []
            for subtask in subtasks:
                messages.append({"role": "user", "content": subtask})
                completion = self.code_agent.chat(subtask)
                messages.append({"role": "assistant", "content": completion})
            messages.append({"role": "user", "content": f"Based on the completed subtasks from the code agent, synthesize the results and provide a comprehensive solution to the original query:\n {query}.\n Ensure the solution is clear, accurate, and addresses all aspects of the problem."})
            res = self.organizer_agent.chat_mt(messages)
        if workflow['type'] == 'math':
            messages = []
            for subtask in subtasks:
                messages.append({"role": "user", "content": subtask})
                completion = self.math_agent.chat(subtask)
                messages.append({"role": "assistant", "content": completion})
            messages.append({"role": "user", "content": f"Based on the completed subtasks from the math agent, synthesize the results and provide a comprehensive solution to the original query:\n {query}.\n Ensure the solution is clear, accurate, and addresses all aspects of the problem."})
            res = self.organizer_agent.chat_mt(messages)
        return res



if __name__ == "__main__":
    query = "from typing import List\n\n\ndef below_zero(operations: List[int]) -> bool:\n    \"\"\" You're given a list of deposit and withdrawal operations on a bank account that starts with\n    zero balance. Your task is to detect if at any point the balance of account fallls below zero, and\n    at that point function should return True. Otherwise it should return False.\n    >>> below_zero([1, 2, 3])\n    False\n    >>> below_zero([1, 2, -4, 5])\n    True\n    \"\"\"\n"
    drama = Drama()
    res = drama.run(query)
    print(res)