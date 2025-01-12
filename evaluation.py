import os
from tqdm import tqdm

from agents.base_agent import BaseAgent
from config.prompts import eval_math_prompts
from dataloader import humaneval_dataloader
from dataloader import math_dataloader
from utils.executor_utils import evaluate_functional_correctness

def eval(mode: str, test_path: str):
    if mode == "code":
        cnt = 0
        for sample in tqdm(humaneval_dataloader):
            idx = sample['task_id'].split('/')[-1]
            with open(os.path.join(test_path, f'{idx}.py'), 'r') as file:
                completion = file.read()
            if evaluate_functional_correctness(sample, completion) == "passed":
                cnt += 1
        return cnt / 164
    if mode == "math":
        cnt = 0
        EvalAgent = BaseAgent()
        for sample in tqdm(math_dataloader):
            idx = sample['id']
            with open(os.path.join(test_path, f'{idx}.txt'), 'r') as file:
                generated_answer = file.read()
            eval_prompt = eval_math_prompts.format(groundtruth_answer=sample['solution'], generated_answer=generated_answer)
            judge = EvalAgent.chat(eval_prompt)
            if 'ANSWER_CORRECT' in judge:
                cnt += 1
        return cnt / 196

if __name__ == "__main__":
    # HumanEval 0.8658536585365854
    # pass_at_1 = eval(mode="code", test_path='results/gpt-4o-mini/HumanEval')
    # print(pass_at_1)

    # MATH 0.7551020408163265
    acc = eval(mode="math", test_path='results/gpt-4o-mini/Math')
    print(acc)
