import numpy as np
def em_algorithm(data, validnum, total, ep=1e-5):
    # validnum为数据中有效的样本数
    #total为样本总数，ep为收敛精度
    valid_data = data[0:validnum]
    avg = np.sum(valid_data) / total  #avg为隐变量的均值，theta为隐变量的方差
    theta = np.sum(np.square(valid_data)) / total - avg
    while True:
        s1 = np.sum(valid_data) + avg * (total  - validnum)
        s2 = np.sum(np.square(valid_data)) + (avg * avg + theta) * (total  - validnum)
        new_avg = s1 / total
        new_theta = s2 / total  - new_avg * new_avg
        if new_avg - avg <= ep and new_theta - theta <= ep:
            break
        else:
            avg, theta = new_avg, new_theta
    return avg, theta


def generation(dtype1, dtype2, dtype3,latent_idx):
    # build NAIVE bayesian
    avg, var = [], []
    for idx in range(latent_idx):

        dim_type1, dim_type2, dim_type3 = dtype1[:, idx], dtype2[:, idx], dtype3[:,idx] # dim_type1 和 dim_type2 表示多维数据中的一维
        avg.append([np.average(dim_type1), np.average(dim_type2), np.average(dim_type3)])
        var.append([np.var(dim_type1), np.var(dim_type2), np.var(dim_type3)])

    em_avg_type1, em_var_type1 = em_algorithm(dtype1[:40, #用EM算法估计缺失值均值和方差
                                 latent_idx], 20, 40)
    em_avg_type2, em_var_type2 = em_algorithm(dtype2[:40,
                                 latent_idx], 20, 40)
    em_avg_type3, em_var_type3 = em_algorithm(dtype3[:40,
                                 latent_idx], 20, 40)
    avg.append([em_avg_type1, em_avg_type2, em_avg_type3]) # 估计得到均值和方差加入到数组
    var.append([em_var_type1, em_var_type2, em_avg_type3])
    return avg, var


def calc_gaussian(x, avg, var):
    # 高斯分布函数
    t = 1.0 / np.sqrt(2 * np.pi * var)
    return t * np.exp(-np.square(x - avg) / (2.0 * var))


if __name__ == '__main__':
    data_str = open('iris.data').readlines()
    data_type1 = np.ndarray([50, 4])
    data_type2 = np.ndarray([50, 4])
    data_type3 = np.ndarray([50, 4])
    for idx in range(50):
        data_type1[idx] = data_str[idx].strip('\n').split(',')[0:4]
    for idx in range(50, 100):
        data_type2[idx - 50] = data_str[idx].strip('\n').split(',')[0:4]
    for idx in range(100, 150):
        data_type3[idx - 100] = data_str[idx].strip('\n').split(',')[0:4]
    a, v = generation(data_type1[:40], data_type2[:40], data_type3[:40], 3)


    # 构造测试数据集
    data_test = np.concatenate((data_type1[40:], data_type2[40:], data_type3[40:]))
    correct_times = 0
    for data_idx in range(len(data_test)):
        data = data_test[data_idx]
        val_type1, val_type2,val_type3 = 1/3,1/3, 1/3
        for idx in range(4):
            # 朴素贝叶斯计算
            val_type1 *= calc_gaussian(data[idx], a[idx][0], v[idx][0])
            val_type2 *= calc_gaussian(data[idx], a[idx][1], v[idx][1])
            val_type3 *= calc_gaussian(data[idx], a[idx][2], v[idx][2])
        # 前10条数据为类型1，中间10条数据为类型2，后10条为类型3
        if val_type1 > val_type2 and val_type1 > val_type3 and data_idx < 10:
            correct_times += 1
        elif val_type1 < val_type2 and val_type2 > val_type3 and 20 > data_idx >= 10:
            correct_times += 1
        elif val_type3 > val_type2 and val_type3 > val_type1 and data_idx >= 20:
            correct_times += 1
        print("N0%2d, Iris_setosa: %f, Iris_versicolor: %f, Iris_virginica: %f"
              % (data_idx + 1, val_type1, val_type2,val_type3))
    print("Accuracy: %.1f%%" % (correct_times * 100/30))