
import numpy as np

from matplotlib.pyplot import *
import numpy as np
class Classifier:
    def __init__(self, max_k=9):
        self.__dots = []
        self.__max_k = max_k

    def fit(self, data):
        centerd, radius = [], np.zeros(self.__max_k, np.float32)
        for k in range(1, self.__max_k):
            _, distance_group, data_type = self.__fit_k_means(data, k)
            type_distance = np.min(distance_group, axis=0)
            centerd.append(_)
            for idx in range(k):
                type_data_idx = np.where(data_type == idx)
                radius[k] += np.max(type_distance[type_data_idx])
            radius[k] = np.sqrt(radius[k]) * k
        best_k = np.argmax(radius[:self.__max_k-1] - radius[1:])
        self.__dots = centerd[best_k]

    def predict(self, data):
        distance_group = []
        for dot in self.__dots:
            distance_group.append(self.__calc_distance(dot, data))
        return np.argmin(distance_group, axis=0)

    # 该函数用于计算当k指定时的k均值中心点
    def __fit_k_means(self, data, k):
        data_size, distance_group = len(data), []# 随机选取第一个中心点
        centerd = [data[np.random.randint(0, data_size, dtype=np.int)]]
        distance_group.append(self.__calc_distance(centerd[0], data))
        for counter in range(k):
            farpoint= np.argmax(np.min(distance_group, axis=0))
            distance_group.append(self.__calc_distance(data[farpoint], data))
            centerd.append(data[farpoint])
        data_type = np.argmin(distance_group, axis=0)
        # 标准k均值算法步骤，迭代更新各中心点坐标，最大迭代次数50
        for repeat_times in range(50):
            updated= np.copy(centerd)
            for idx in range(len(centerd)):
                updated[idx] = np.average(data[np.where(data_type == idx)], axis=0)
            # 如果更新以后和更新之前的差距小于临界值，则停止迭代
            if np.max(np.linalg.norm(updated - centerd, axis=0) < 0.1):
                break
            distance_group=[]
            centerd =updated
            for dot in centerd:
                # 按照新的中心点坐标更新各点到中心点距离
                distance_group.append(self.__calc_distance(dot, data))
                data_type = np.argmin(distance_group, axis=0)
        return centerd, distance_group, data_type

    @staticmethod
    # 计算各点到中心点的欧氏距离
    def __calc_distance(central_dot, data):
        distance = []
        for this_dot in data:
            distance.append(np.linalg.norm(central_dot - this_dot))
        return distance




if __name__ == '__main__':
    print('正在初始化聚类器')
    data_file = open('melon.txt')
    color_list = ['pink', 'green', 'gray', 'purple',  'orange','red', 'blue', 'black','white']
    data_lines, data = data_file.readlines(), []
    data_type_count = np.zeros(4, np.int)
    for line in data_lines:
        raw_data = line.split('\t')
        data_type_count[int(raw_data[0]) - 1] += 1
        data.append(np.array(raw_data[1:], np.float32))
    classifier = Classifier(max_k=9)
    for n in range(3):#2,3,4
        data_n_types = np.array(data[:np.sum(data_type_count[:n+2])], np.float32)
        print('正在对 %d 类的数据进行聚类...' % (n + 2), end='')
        np.random.shuffle(data_n_types)
        classifier.fit(data_n_types)
        label_n_types = classifier.predict(data_n_types)
        for i in range(9):
            # 最大的可能种类为9种
            type_i_in_n = data_n_types[np.where(label_n_types == i)]
            #print(data.length)
            scatter(type_i_in_n[:, 0], type_i_in_n[:, 1], c = color_list[i], s=20)
        show()
    data_file.close()