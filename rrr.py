import numpy as np
import RandomForest


if __name__ == '__main__':
    file = open('wine.data')
    data_str = file.readlines()
    np.random.shuffle(data_str)
    file.close()
    # 读取数据并进行预处理
    value = np.ndarray([len(data_str), 13], np.float32)
    label = np.ndarray([len(data_str)], np.int32)
    for outer_idx in range(len(data_str)):
        data = data_str[outer_idx].strip('\n').split(',')
        value[outer_idx] = data[1:]
        label[outer_idx] = data[0]
    # 由于数据较为简单，生成数量为30的小森林
    # 使用100条数据进行训练，30条数据进行验证
    forest = RandomForest.RandomForest()
    forest.fit(value[:100], label[:100], 30)
    result = forest.predict(value[100:])
    print(result)
    print(label)
    err_count = len(np.where(label[100:] != result))
    print('共测试 30 条样本，其中错误 %d 条，准确率 %.2f%%'
          % (err_count, (30.0 - err_count)* 100 / 30), end='\r')
