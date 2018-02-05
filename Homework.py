import numpy as np
from matplotlib.pyplot import *
from numpy import *
A=random.rand(1000,1000)
#print(A)
X=np.ones((1000,1))
b=1.00*np.dot(A,X)
a=0.0002
x0=np.ones((1000,1))*1.3
f0=np.dot(A,x0)-b
xk1=x0
H=[]
S=[]
xks=x0*3
#print(A**2)
f01 = np.dot(np.dot(A,A), xk1 ) - np.dot(A,b)
f0s=np.zeros(f01.shape)
for i in range (1000):
 f01 = np.dot(np.dot(np.transpose(A),A), xk1) - np.dot(np.transpose(A),b)
 f0=np.dot(A,xk1)-b
 #f01=0.5*np.dot(A**2,xk1**2)-np.dot(np.dot(A,b),xk1)+b**2
 f0s=f01
 xk2=xk1-a*f01
 xks=xk1
 xk1=xk2
   #print(f01)
#f0=0.5*np.linalg.norm(A*x0,b)

 #H.append(xk2)
 #S.append(0.5*np.linalg.norm(A*xk2-b))
print("end")
print(xk2)
#for i in range(15):
 #scatter(H[:,0:2], S[:], c="red", s=20)