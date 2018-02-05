from matplotlib.pyplot import *
import numpy as np
import Classifier


if __name__ == '__main__':
    print('正在初始化聚类器')
    data_file = open('melon.txt')
    color_list = ['red', 'blue', 'green', 'black', 'pink', 'orange', 'purple', 'gray', 'gold']
    data_lines, data = data_file.readlines(), []
    data_type_count = np.zeros([4], np.int)
    for line in data_lines:
        raw_data = line.split('\t')
        data_type_count[int(raw_data[0]) - 1] += 1
        data.append(np.array(raw_data[1:], np.float32))
    cls = Classifier.Classifier(max_k=9)
    for n in range(3):#2,3,4
        data_n_types = np.array(data[:np.sum(data_type_count[:n+2])], np.float32)
        print('正在对 %d 种类型的数据进行聚类...' % (n + 2), end='')
        np.random.shuffle(data_n_types)
        cls.fit(data_n_types)
        label_n_types = cls.predict(data_n_types)
        for i in range(9):
            # 最大的可能种类为9种，所以用不同颜色绘制出不同种类下的样本点
            type_i_in_n = data_n_types[np.where(label_n_types == i)]
            scatter(type_i_in_n[:, 0], type_i_in_n[:, 1], c=color_list[i], s=20)
        print('完毕')
        show()
    data_file.close()