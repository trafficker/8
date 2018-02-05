import numpy as np
A = np.zeros((100, 100))
for i in range(100): #generate A
    for j in range(100):
        if (i == j):
            A[i, j] = 2
        if (abs(i - j) == 1):
            A[i, j] = A[j, i] = -1
b = np.ones((100, 1))  #generate b
print("Conjugate Gradient x:")
#A=np.array([[9,18,9,-27],[18,45,0,-45],[9,0,126,9],[-27,-45,9,135]])
#b=np.array([[1],[2],[16],[8]])
x=np.zeros((100,1)) # 初始值x0
r=b-np.dot(A,x)
p=r  #p0=r0
#while np.linalg.norm(np.dot(A, x) - b) / np.linalg.norm(b) >= 10 ** -6:
for i in range(100):
    r1=r
    a=np.dot(r.T,r)/np.dot(p.T,np.dot(A,p))
    x = x + a * p    #x(k+1)=x(k)+a(k)*p(k)
    r=b-np.dot(A,x)  #r(k+1)=b-A*x(k+1)
    q = np.linalg.norm(np.dot(A, x) - b) / np.linalg.norm(b)
    if q<10**-6:
        break
    else:
        beta=np.linalg.norm(r)**2/np.linalg.norm(r1)**2
        p=r+beta*p  #p(k+1)=r(k+1)+beta(k)*p(k)


print(x)
print("done Conjugate Gradient!")
print('\n')
print("QR x:")
Q=np.zeros_like(A) #Q.shape=A.shape
w = 0
for a in A.T:
    u = np.copy(a)
    for i in range(0, w):
           u -= np.dot(np.dot(Q[:, i].T, a), Q[:, i])
    ex = u / np.linalg.norm(u)
    Q[:, w] = ex
    w+= 1
R = np.dot(Q.T, A) # A=Q*R
N=np.dot(Q.T,b)
x2=np.linalg.solve(R,N)  # Rx=Q.T*b
print(x2)   #solve x
print("done QR!")