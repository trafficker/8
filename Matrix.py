import numpy as np
from numpy import random
from numpy import linalg
y=[]
for i in range(1,101):
    y.append(i)
z=np.matrix(y,np.float32)
x=z.T  #generate a vector x=(1.,2.,...,100.)^T
M=10*random.rand(100,100)
L=np.eye(100,100) #generate identity matrix
A=M+L   #generate A
b=A*x   #generate b
#s,f=np.linalg.eig(k)特征值分解
U=np.zeros((100,100))
#解Ax=b，先进行LU分解
for i in range(0,100):
        if(i==0):
            L[0,0]=1 #L对角线上全为1
            for j in range(100):
                U[i,j]=A[i,j]

        else:
            for j in range(0,i):  #计算L[i][j]
                temp=A[i,j]
                p=0
                while j>=1 and p<j:
                    temp=temp-L[i,p]*U[p,j]
                    p=p+1
                L[i,j]=temp/U[j,j]
            # lij=(aij-Σ(k=1,j-1)lik*ukj)/ujj
            for j in range(i,100):  #计算U[i][j]
                    temp=A[i,j]
                    p=0
                    while(p<j):
                      temp=temp-L[i,p]*U[p,j]
                      p=p+1
                    U[i,j]=temp
                # uij=aij-Σ(k=1,j-1)lik*ukj
#print(A)
#print(L.dot(U))
y = np.linalg.solve(L, b) #解Ly=b方程
x2=np.linalg.solve(U,y)   #解UX=Y方程
print("Previous x:")
print(x)#原来的x值
print("\n")
print("Later x:")
print(x2)#后得的x值
print(" DONE ")
c=np.matrix(([1,2,3],[4,5,6]));
print(np.sum(c))








