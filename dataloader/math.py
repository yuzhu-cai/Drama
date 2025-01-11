import json

class MATHDataLoader:
    def __init__(self, subset_path="./data/MATH_test_subset/MATH_test_subset.json"):
        self.subset_path = subset_path
        # 加载子集数据
        with open(subset_path, "r", encoding="utf-8") as f:
            self.subset = json.load(f)

    def __len__(self):
        return len(self.subset)

    def __getitem__(self, idx):
        return self.subset[idx]

    def get_all_samples(self):
        return self.subset

    def filter_by_type(self, type_name):
        return [sample for sample in self.subset if sample["type"] == type_name]

# 使用示例
if __name__ == "__main__":
    # 初始化 DataLoader
    dataloader = MATHDataLoader(subset_path="./data/MATH_test_subset/MATH_test_subset.json")

    # 获取子集中的样本数量
    print("Total samples in subset:", len(dataloader))

    # 获取第一个样本
    sample = dataloader[0]
    print("First sample:")
    print("Problem:", sample["problem"])
    print("Solution:", sample["solution"])
    print("Type:", sample["type"])

    # 获取所有样本
    all_samples = dataloader.get_all_samples()
    print("Total samples:", len(all_samples))

    # 过滤特定类别的样本
    algebra_samples = dataloader.filter_by_type("algebra")
    print("Algebra samples:", len(algebra_samples))