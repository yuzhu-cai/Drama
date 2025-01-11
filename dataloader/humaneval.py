import json

class HumanEvalDataLoader:
    def __init__(self, dataset_name="./data/HumanEval/HumanEval.jsonl"):
        self.dataset = []
        with open(dataset_name, "r", encoding="utf-8") as f:
            for line in f:
                data = json.loads(line)
                self.dataset.append(data)

    def __len__(self):
        return len(self.dataset)

    def __getitem__(self, idx):
        return self.dataset[idx]

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
    print("Entry Point:", sample["entry_point"])

    # 获取数据集中的所有样本
    all_samples = dataloader.get_all_samples()
    print(f"Total samples: {len(all_samples)}")