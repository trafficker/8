import numpy as np
def getdistance(test):
    L=len(test)
    w=np.empty([L,L],np.float32)
    for i in range(L):
       for j in range(L):
        w[i][j]=np.linalg.norm(test[i]-test[j])
    return w
def mds(test,deg):
    L=len(test)
    if(deg>L):
        deg=L
    R=np.zeros([L,L],np.float32)
    Q=getdistance(test)
    ss=1/L**2*np.sum(Q**2)
    for i in range(L):
        for j in range(L):
            R[i,j]=-0.5*(Q[i,j]**2-1/L**2*np.dot(Q[i:],Q[i:])-1/L**2*np.dot(Q[:j],Q[:j])+ss)

    a1,a2=np.linalg.eig(R)
    c=np.argpartition(a1,deg-1)[-deg:]
    d=np.diag(np.maximum(a1[c],0.0))
    return np.matmul(a2[:c],np.sqrt(d))
def dirk(test,st):
    L=len(test)




