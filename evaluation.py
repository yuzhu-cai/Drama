import os
from tqdm import tqdm

from dataloader import humaneval_dataloader
from dataloader import math_dataloader
from utils.executor_utils import function_with_timeout


def evaluate_functional_correctness(
    sample: dict,
    completion: str,
    timeout: int = 5,
):
    try:
        code = ("from typing import *\n" if "from typing import *" not in completion else "") + \
            completion + "\n" + sample['test'] + \
            "\n" + f"check({sample['entry_point']})"
        function_with_timeout(
            exec,
            (code, globals()),
            timeout
        )
        return "passed"
    except Exception as e:
        return f"failed: {e}"

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
        pass


if __name__ == "__main__":
    # HumanEval
    pass_at_1 = eval(mode="code", test_path='results/gpt-4o-mini/HumanEval')
    print(pass_at_1)