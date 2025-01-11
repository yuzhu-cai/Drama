import os
from tqdm import tqdm

from agents.base_agent import BaseAgent
from dataloader import humaneval_dataloader, math_dataloader
from utils.parse import extract_python_code

def infer_single_agent(mode: str):
    Agent = BaseAgent()
    if mode == "code":
        for sample in tqdm(humaneval_dataloader):
            response = Agent.chat(sample['prompt'])
            code = extract_python_code(response)
            with open(f'results/gpt-4o-mini/{sample["task_id"]}.py', 'w') as file:
                file.write(code)
    if mode == "math":
        for sample in tqdm(math_dataloader):
            response = Agent.chat(sample['problem'])
            with open(f'results/gpt-4o-mini/Math/{sample["id"]}.txt', 'w') as file:
                file.write(response)


if __name__ == "__main__":
    # single agent: gpt-4o-mini
    # Humaneval
    # infer_single_agent(mode="code")
    # MATH
    infer_single_agent(mode="math")
