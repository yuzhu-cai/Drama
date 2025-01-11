from datasets import load_dataset

class HumanEvalDataLoader:
    def __init__(self, dataset_name="./data/HumanEval", split="test"):
        self.dataset = load_dataset(dataset_name, split=split)

    def __len__(self):
        return len(self.dataset)

    def __getitem__(self, idx):
        sample = self.dataset[idx]
        return {
            "task_id": sample["task_id"],
            "prompt": sample["prompt"],
            "canonical_solution": sample["canonical_solution"],
            "test": sample["test"],
        }

    def get_all_samples(self):
        return [self.__getitem__(i) for i in range(len(self))]

# 使用示例
if __name__ == "__main__":
    # 初始化 DataLoader
    dataloader = HumanEvalDataLoader()

    # 获取数据集中的第一个样本
    sample = dataloader[0]
    print("Task ID:", sample["task_id"])
    print("Prompt:", sample["prompt"])
    print("Canonical Solution:", sample["canonical_solution"])
    print("Test Cases:", sample["test"])

    # 获取数据集中的所有样本
    all_samples = dataloader.get_all_samples()
    print(f"Total samples: {len(all_samples)}")