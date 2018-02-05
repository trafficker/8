import numpy as np
from numpy import *
A=random.rand(1000,1000) #随机初始化A
X=np.ones((1000,1))    #定义全1矩阵X
b=1.00*np.dot(A,X)    #生成相应的b

def CG():  #梯度下降法函数
    decay=0.09
    x_init = 2*np.ones((1000,1)) #初始化矩阵
    x_iteration = np.zeros((1000,1))#中间过程矩阵
    Iter= 0 #迭代次数
    while Iter <= 500:
        #print(x_init.shape)
        det=(np.dot(np.dot(np.transpose(A),A),x_init) -  np.dot(np.transpose(A),b)) #计算实时梯度
        deta=np.dot(A,det) #计算梯度乘以海森矩阵
        a1=(np.dot(np.transpose(det),det))/(np.dot(np.transpose(deta),deta)) #得到实时步长
        x_iteration = x_init - a1*(np.dot(np.dot(np.transpose(A),A),x_init) -  np.dot(np.transpose(A),b)) #迭代更新x
        x_init = x_iteration #更新x值
        Iter += 1 #迭代次数加1
        if np.linalg.norm(np.dot(np.dot(np.transpose(A),A),x_init) -  np.dot(np.transpose(A),b))<=0.01:
            #中止条件为梯度二范数小于0.01
            break
    print(x_init)




if __name__=='__main__':
    print ("最佳点为:")
    CG() #开始测试
    print("end")