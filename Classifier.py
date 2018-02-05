import numpy as np


class Classifier:
    def __init__(self, max_k=9):
        self.__dots = []
        self.__max_k = max_k

    # noinspection PyTypeChecker
    def fit(self, data):
        central_dots, radius = [], np.zeros(self.__max_k, np.float32)
        # 寻找最佳的k值，k值范围在1到max_k之间
        for k in range(1, self.__max_k):
            _, distance_group, data_type = self.__fit_k_means(data, k)
            type_distance = np.min(distance_group, axis=0)
            central_dots.append(_)
            # 计算各个簇的半径（中心点到簇中最远的点的距离）之和
            for idx in range(k):
                type_data_idx = np.where(data_type == idx)
                radius[k] += np.max(type_distance[type_data_idx])
            # 加权求和，k用于抑制
            radius[k] = np.sqrt(radius[k]) * k
        # 交叉相减，得出半径之和下降最快的k值，并认定为最佳k值
        best_k = np.argmax(radius[:self.__max_k-1] - radius[1:])
        self.__dots = central_dots[best_k]

    def predict(self, data):
        distance_group = []
        for dot in self.__dots:
            distance_group.append(self.__calc_distance(dot, data))
        return np.argmin(distance_group, axis=0)

    # 该函数用于计算当k指定时的k均值中心点
    def __fit_k_means(self, data, k):
        data_size, distance_group = len(data), []
        # 随机选取第一个中心点
        central_dots = [data[np.random.randint(0, data_size, dtype=np.int)]]
        distance_group.append(self.__calc_distance(central_dots[0], data))
        for counter in range(k):
            # 设当前已经有了k个中心点，则每个点都会被分配到一个中心点
            # 寻找距离其中心点距离最远的点，将其分割出来作为新的中心点
            # 重复上述步骤k-1次，即可得到k个中心点
            farthest_dot = np.argmax(np.min(distance_group, axis=0))
            distance_group.append(self.__calc_distance(data[farthest_dot], data))
            central_dots.append(data[farthest_dot])
        data_type = np.argmin(distance_group, axis=0)
        # 标准k均值算法步骤，迭代更新各中心点坐标，最大迭代次数50
        for repeat_times in range(50):
            new_dots = np.copy(central_dots)
            for idx in range(len(central_dots)):
                new_dots[idx] = np.average(data[np.where(data_type == idx)], axis=0)
            # 如果更新以后和更新之前的差距小于临界值，则停止迭代
            if np.max(np.linalg.norm(new_dots - central_dots, axis=0) < 0.1):
                break
            distance_group.clear()
            central_dots = new_dots
            for dot in central_dots:
                # 按照新的中心点坐标更新各点到中心点距离
                distance_group.append(self.__calc_distance(dot, data))
                data_type = np.argmin(distance_group, axis=0)
        return central_dots, distance_group, data_type

    @staticmethod
    # 计算各点到中心点的欧氏距离
    def __calc_distance(central_dot, data):
        distance = []
        for this_dot in data:
            distance.append(np.linalg.norm(central_dot - this_dot))
        return distance