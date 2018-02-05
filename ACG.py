from numpy import *
import numpy as np
A=1.00*random.rand(1000,1000) #随机定义A
X=1.00*np.ones((1000,1))     #定义初始全1的X
b=1.00*np.dot(A,X)      #生成b
def ACG(beta=1000000):
    l=0.00
    xs=X
    x0=2.00*np.ones((1000,1)) #定义初始x
    y0=x0  #定义初始y
    xs=x0  #初始化x
    ys=y0  #初始化y
    yq=y0
    count=0  #迭代计数
    for i in range (1000):
        l=(1+np.sqrt(1+4*l**2))/2  #定义拉姆达
        lj=(1+np.sqrt(1+4*l**2))/2  #更新拉姆达
        gama=(1-l)/lj   #得到伽马值
        w=(np.dot(np.transpose(np.dot(np.transpose(A),A)),xs)-np.dot(np.transpose(A),b))/beta #实时梯度
        print("x的更新后的值:")
        print(xs)
        ys=xs-w   #更新y的值
        xq=xs     #保留这次x值，为下次迭代判断使用
        xs=(1-gama)*ys+gama*yq  #根据公式，更新x的值
        yq=ys      # 保留这次y值，为下次迭代时作为先前值使用
        count+=1
        if(np.linalg.norm(xs-xq)<=0.001):
            break
        if beta==0:  #分母beta不可为0
            break
        if gama>0:   #伽马不能大于0
            break
        if np.linalg.norm(np.dot(np.dot(np.transpose(A), A), xs) - np.dot(np.transpose(A), b))<0.001:
             #终止条件，梯度二范数小于0.01
           break
    print("FInal!!!!")
    print(xs) #输出结果最优点
    print("迭代次数:%d"%count)
if __name__=="__main__":
    print("Start ACG!")
    ACG(200000) #开始测试
