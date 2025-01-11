from datasets import load_dataset

class HumanEvalDataLoader:
    def __init__(self, dataset_name="./data/HumanEval", split="test"):
        """
        初始化 HumanEvalDataLoader 类。

        Args:
            dataset_name (str): Hugging Face 上的数据集名称，默认为 "./data/HumanEval"。
            split (str): 数据集的划分，默认为 "test"。
        """
        self.dataset = load_dataset(dataset_name, split=split)

    def __len__(self):
        """
        返回数据集的样本数量。
        """
        return len(self.dataset)

    def __getitem__(self, idx):
        """
        根据索引获取数据集中的一个样本。

        Args:
            idx (int): 样本的索引。

        Returns:
            dict: 包含任务 ID、提示、规范化和测试用例的字典。
        """
        sample = self.dataset[idx]
        return {
            "task_id": sample["task_id"],
            "prompt": sample["prompt"],
            "canonical_solution": sample["canonical_solution"],
            "test": sample["test"],
        }

    def get_all_samples(self):
        """
        获取数据集中的所有样本。

        Returns:
            list: 包含所有样本的列表，每个样本是一个字典。
        """
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