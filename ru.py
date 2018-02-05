import numpy as np
A=np.zeros((100,100))
for i in range(100):
    for j in range(100):
        if(i==j):
            A[i,j]=2
        if(abs(i-j)==1):
            A[i,j]=A[j,i]=-1
b=np.zeros((100,1))
D=2*np.eye(100,100) #generate D
L=-1*A
U=-A
for i in range(100):
    for j in range(100):
        if(i<=j):
            L[i,j]=0
        if(i>=j):
            U[i,j]=0
# D,L,U is get now
#b=np.array([[3],[15],[10]])
#D=np.array([[10,0,0],[0,10,0],[0,0,5]])
#L=np.array([[0,0,0],[2,0,0],[1,2,0]])
#U=np.array([[0,2,1],[0,0,1],[0,0,0]])
#print(np.linalg.norm(L-U))
E1=np.linalg.inv(D) #D^-1
E2=L+U
k=np.dot(E1,E2)  # D^-1(L+U)
g=np.dot(E1,b)
print("Jacob")
x=0.04*np.ones((100,1))
x=np.dot(k,x)+g
for i in range(50000): # X^(n+1)=k*X^n+g
    temp = x
    x=np.dot(k,x)+g
    #print(x)
    q=np.linalg.norm(temp-x)
    if(q<10**-6):
        break
print(x) #Jacob result6
print("goss")
x=0.04*np.ones((100,1))
Bg=np.dot(np.linalg.inv((D-L)),U) #Bg=(D-L)^-1*U
fg=np.dot(np.linalg.inv((D-L)),b) #fg=(D-L)^-1*b
x=np.dot(Bg,x)+fg
for i in range(50000):   #X^(k+1)=Bg*X^k+fg
    temp = x
    x=np.dot(Bg,x)+fg
    #print(x)
    q = np.linalg.norm(temp - x)
    if (q < 10 ** -6):
        break
print(x)#goss result
print("SOR")
w=1.35
z=(1-w)*D+w*U
Bw=np.dot(np.linalg.inv(D-w*L),z)
fw=w*np.dot(np.linalg.inv(D-w*L),b)
x=0.04*np.ones((100,1))
for i in range(50000):   #X^(k+1)=Bg*X^k+fg
    temp = x
    x=np.dot(Bw,x)+fw
    #print(x)
    q = np.linalg.norm(temp - x)
    if (q < 10 ** -6):
        break
print(x) #SOR result
