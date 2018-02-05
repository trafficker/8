import numpy as np
import matplotlib as plt
idots=[]
def getdistance(n,dat):
    distance=[]
    for i in dat:
        distance.append(np.linalg.norm(n-i))
    return distance
def k_means(data,k):
    datalen=len(data)
    distanceset=[]
    points=[data[np.random.randint(0,datalen,dtype=np.int)]]
    distanceset.append(getdistance(points[0],data))
    for i in range(k-1):
        fardot=np.argmax(np.min(distanceset,axis=0))
        distanceset.append(getdistance(data[fardot],data))
        points.append(data[fardot])
    data_type = np.argmin(distanceset,axis=0)
    for time in range(50):
        updatepoints = np.copy(points)
        for idx in range(len(points)):
            updatepoints[idx] = np.average(data[np.where(data_type == idx)], axis=0)
        if np.max(np.linalg.norm(updatepoints-points,axis=0)<0.1):
                break

        points=updatepoints
        distanceset=[]
        for p in points:
            distanceset.append(getdistance(p,data))
            data_type=np.argmin(distanceset,axis=0)
    print(len(data_type))
    return points,distanceset,data_type

def better (data):
    centerd=[]
    radius=np.zeros(9,np.float32)
    for k in range(1,9):
        dot,distanceset,data_type=k_means(data,k)
        centerd.append(dot)
        typedistance=np.min(distanceset,axis=0)
        for i in range(k):
         radius[k]+=np.max(typedistance[np.where(data_type==i)])
        radius[k] = np.sqrt(radius[k]) * k
    best_k = np.argmax(radius[:9- 1] - radius[1:])
    idots = centerd[best_k]

def predict(data):
        distance_group = []
        for dot in idots:
            distance_group.append(getdistance(dot, data))
        return np.argmin(distance_group, axis=0)


if __name__ == '__main__':
    print('正在构建聚类器')
    data_file = open('melon.txt')
    data_lines, data = data_file.readlines(), []
    data_type_count = np.zeros([4], np.int)
    for line in data_lines:
        raw_data = line.split('\t')
        data_type_count[int(raw_data[0]) - 1] += 1
        data.append(np.array(raw_data[1:], np.float32))
    for n in range(3):

        data_n_types = np.array(data[:np.sum(data_type_count[:n+2])], np.float32)
        print('正对 %d 种类型的数据聚类...' % (n + 2), end='')
        np.random.shuffle(data_n_types)
        better(data_n_types)
        label_n_types = predict(data_n_types)
        for i in range(9):

            type_i_in_n = data_n_types[np.where(label_n_types == i)]
    data_file.close()