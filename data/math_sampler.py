import os
import json
import random
from collections import defaultdict

class MATHTestSubsetSampler:
    def __init__(self, data_dir="./data/MATH", subset_size=196, split="test"):
        """
        初始化 MATHTestSubsetSampler 类。

        Args:
            data_dir (str): 数据集根目录，默认为 "./data/MATH"。
            subset_size (int): 子集大小，默认为 196。
            split (str): 数据集划分，默认为 "test"。
        """
        self.data_dir = data_dir
        self.subset_size = subset_size
        self.split = split
        # 加载数据集
        self.dataset = self.load_dataset()

    def load_dataset(self):
        """
        加载数据集。

        Returns:
            list: 包含所有样本的列表，每个样本是一个字典。
        """
        dataset = []
        split_dir = os.path.join(self.data_dir, self.split)
        # 遍历每个类别文件夹
        for category in os.listdir(split_dir):
            category_dir = os.path.join(split_dir, category)
            if not os.path.isdir(category_dir):
                continue
            # 遍历类别文件夹中的每个文件
            for file_name in os.listdir(category_dir):
                file_path = os.path.join(category_dir, file_name)
                if not file_name.endswith(".json"):
                    continue
                # 加载 JSON 文件
                with open(file_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    data["type"] = category  # 添加类别信息
                    dataset.append(data)
        return dataset

    def calculate_type_distribution(self):
        """
        计算数据集中每个问题类型的分布。

        Returns:
            dict: 每个问题类型的分布（比例）。
        """
        type_count = defaultdict(int)
        for sample in self.dataset:
            type_count[sample["type"]] += 1
        total_samples = len(self.dataset)
        type_distribution = {k: v / total_samples for k, v in type_count.items()}
        return type_distribution

    def sample_subset(self):
        """
        按照原始分布采样一个子集。

        Returns:
            list: 采样得到的子集。
        """
        type_distribution = self.calculate_type_distribution()
        subset = []
        for q_type, proportion in type_distribution.items():
            # 计算当前类型需要采样的数量
            num_samples = round(self.subset_size * proportion)
            # 过滤当前类型的样本
            type_samples = [sample for sample in self.dataset if sample["type"] == q_type]
            # 随机采样
            subset.extend(random.sample(type_samples, num_samples))
        # 如果子集大小不等于目标大小（由于四舍五入），调整
        if len(subset) != self.subset_size:
            subset = random.sample(subset, self.subset_size)
        return subset

    def save_subset(self, subset, output_dir="./data/MATH_test_subset"):
        """
        保存采样得到的子集。

        Args:
            subset (list): 采样得到的子集。
            output_dir (str): 子集保存路径，默认为 "./data/MATH_test_subset"。
        """
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        # 保存为 JSON 文件
        output_path = os.path.join(output_dir, "MATH_test_subset.json")
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(subset, f, ensure_ascii=False, indent=4)
        print(f"Test subset saved to {output_path}")

# 使用示例
if __name__ == "__main__":
    # 初始化采样器
    sampler = MATHTestSubsetSampler(data_dir="./data/MATH", subset_size=196, split="test")

    # 采样子集
    subset = sampler.sample_subset()

    # 保存子集
    sampler.save_subset(subset, output_dir="./data/MATH_test_subset")

    # 打印子集中的问题类型分布
    type_count = defaultdict(int)
    for sample in subset:
        type_count[sample["type"]] += 1
    print("Test subset type distribution:", dict(type_count))