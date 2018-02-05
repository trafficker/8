import numpy as np
import random
from numpy import *
import numpy as np
import matplotlib.pyplot as plt
import random
A=np.random.rand(10,10)
X=np.ones((10,1))
b=1.00*np.dot(A,X)
def goldsteinsearch(f,df,d,x,alpham,rho,t):

    flag=0

    a=0
    b=alpham
    #fk=0.5*np.dot(np.dot(A,A),np.dot(x,x))-np.dot(np.dot(A,x),b)
    fk=np.dot(0.5*np.abs(np.dot(A,x)-b),np.transpose(np.abs(np.dot(A,x)-b)))
   #gk=df(x)
    gk=np.dot(np.dot(A,A),x)-np.dot(A,b)
    phi0=fk
    d=-gk
    dphi0=np.dot(gk,d)

    alpha=b*random.uniform(0,1)

    while(flag==0):
        newfk=f(x+alpha*d)
        phi=newfk
       # print(phi.shape)
       # print(phi0.shape)
       # print(dphi0.shape)
        if(np.linalg.norm(phi-phi0)<=np.linalg.norm(rho*alpha*dphi0)):
            if(np.linalg.norm(phi-phi0)>=np.linalg.norm(1-rho)*alpha*dphi0):
                flag=1
            else:
                a=alpha
                b=b
                if(b<alpham):
                    alpha=(a+b)/2
                else:
                    alpha=t*alpha
        else:
            a=a
            b=alpha
            alpha=(a+b)/2
    return alpha


def rosenbrock(x):
  # return 0.5*np.dot(np.dot(A,A),np.dot(x,x))-np.dot(np.dot(A,x),b)
     return  np.dot(0.5 * np.abs(np.dot(A, x) - b), np.abs(np.dot(A, x) - b))
def jacobian(x):
    return np.dot(np.dot(A,A),x)-np.dot(A,b)





def steepest(x0):

    print('初始点为:')
    #print(x0,'\n')
    imax = 100
    W=np.zeros((imax,10))
    i = 0
    x = x0
    grad = jacobian(x)
    delta = sum(grad**2)  # 初始误差

    print("开始计算！")
    while i<imax and delta>10**(-5):
        p = -jacobian(x)
        x0=x
        alpha = goldsteinsearch(rosenbrock,jacobian,p,x,1,0.1,2)
        x = x + alpha*p
        W[i] = np.transpose(x)
        grad = jacobian(x)
        delta = sum(grad**2)
        i=i+1

    print("迭代次数为:",i)
    print("近似最优解为:")
    print(x,'\n')
    W=W[0:i]  # 记录迭代点
    return W

x0 =X*0.3
W=steepest(x0)

#plt.plot(W[:],'g*',W[:]) # 画出迭代点收敛的轨迹
#plt.show()