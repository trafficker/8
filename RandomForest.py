from sklearn.tree import DecisionTreeRegressor
import numpy as np
class RandomForest:
    def __init__(self):
        self.__trees = []

    def fit(self, data, label, tree_count=100):
        data_size = len(label)
        for idx in range(tree_count):
            # 抽取训练数据的1/4为样本，使用SkLearn中的决策树进行训练
            sample_idx = np.random.randint(0, data_size, data_size // 4, np.int)
            sample_data, sample_label = data[sample_idx], label[sample_idx]
            tree = DecisionTreeRegressor()
            tree.fit(sample_data, sample_label)
            self.__trees.append(tree)

    def predict(self, data):
        data_size = len(data)
        result = np.zeros([data_size], np.int)
        for tree in self.__trees:
            # 投票操作，将票数累计
            result += tree.predict(data).astype(np.int)
        # 票数过半的为正样本，否则为负样本
        pos = np.where(result >= data_size // 2)
        neg = np.where(result < data_size // 2)
        result[pos], result[neg] = 1, 0
        return result