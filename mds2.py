import numpy as np
import matplotlib.pyplot as plt

def mds(T,k):
    T = np.asarray(T)
    TSquare = T**2
    totalMean = np.mean(TSquare)
    columnMean = np.mean(TSquare, axis = 0)
    rowMean = np.mean(TSquare, axis = 1)
    re = np.zeros(TSquare.shape)
    for i in range(re.shape[0]):
        for j in range(re.shape[1]):
            re[i][j] = -0.5*(TSquare[i][j] - rowMean[i] - columnMean[j]+totalMean)
    eigVal,eigVec = np.linalg.eig(re)
    X = np.dot(eigVec[:,:k],np.sqrt(np.diag(eigVal[:k])))

    return X


D = [[0.0,1260.0,176.0,1962.0,701.3,939.1,2331.4,464.5],
[1260.0,0.0,1270.9,1800.0,1404.7,693.5,2599.2,1018.0],
[176.0,1270.0,0.0,1873.3,520.1,928.1,2182.4,405.4],
[1962.0,1800.0,1873.3,0.0,1482.9,1193.6,860.6,1503.2],
[701.0,1404.7,520.1,1482.9,0.0,855.7,1663.4,437.7],
[939.1,693.5,928.1,1193.6,855.7,0.0,1933.4,564.9],
[2331.4,2599.2,2782.4,860.6,1663.4,1933.4,0.0,1931.1],
[464.5,1018.0,405.4,1503.2,437.7,564.9,1931.1,0.0]]

label = ['上海','北京','浙江','四川','江西','河南','云南','安徽']
X = mds(D,2)
plt.plot(X[:,0],X[:,1],'*')
for i in range(X.shape[0]):
    plt.text(X[i,0]+ 25,X[i,1]-25,label[i],fontproperties='SimHei')
plt.show()