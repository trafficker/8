import numpy as np
from PIL import Image
def LoadData(t):
    testp=np.array(Image.open("./feret/"+str(t)+"-6.bmp"))
    testp=np.reshape(testp,(10304,1))
    for i in np.arange(3,8):
     for j in np.arange(1,6):
        if i==3 and j==1:
            img = np.array(Image.open('./feret/' + str(i) + '-' + str(j) + ".bmp"))
            img = np.reshape(img, (112 * 92, 1))
            A = img
        else:
            img = np.array(Image.open('./feret/' + str(i) + '-' + str(j) + ".bmp"))
            img = np.reshape(img, (112 * 92, 1))
            A = np.concatenate((A, img), axis=1)
    A = dfc(A)
    data = testp / np.linalg.norm(testp, ord=2)
    return A, data
def dfc(A):
  m=A.shape[1]
  for i in range(m):
   if i==0:
      Cl=A[:,i]/np.linalg.norm(A[:,i],ord=2)
      Cl=np.reshape(Cl,(10304,1))
   else:
      Cf=A[:,i]/np.linalg.norm(A[:,i],ord=2)
      Cf=np.reshape(Cf,(10304,1))
      Cl=np.concatenate((Cl,Cf),axis=1)
  return Cl

def xishu(A,y):

 x0=np.ones((25,1))
 c=np.dot(A, A.T)
# L=np.linalg.norm(2*np.dot(A,A.T))
 L=100000
 k=0
 while True:
# gradient
  g=2*np.dot(np.dot(A.T,A),x0)-2*np.dot(A.T,y)
  z=x0-1.0/L*g
  lamda=1
  w0=np.linalg.norm(np.dot(A,x0)-y,ord=2)**2+lamda*np.linalg.norm(x0,ord=1)
  x=x0
  for i in range(25):
    if z[i,0]>lamda/L:
      x[i,0]=z[i,0]-lamda/L
    elif z[i,0]<-lamda/L:
      x[i,0]=z[i,0]+lamda/L
    else:
      x[i,0]=0
  k+=1
  w=np.linalg.norm(np.dot(A,x)-y,ord=2)**2+lamda*np.linalg.norm(x,ord=1)
  if w0-w<1e-7:
   return x
  x0=x
def NewX(x,i):

 newX=np.zeros((25,1))

 for t in np.arange(5*i,5*i+5):

   newX[t,0]=x[t,0]

 return newX



def judgeClass(A,x,y):
 minValue=float(np.inf)
 minIndex=-1
 for i in range(5):
   dis=np.linalg.norm(y-np.dot(A,NewX(x,i)))
   print("对类", i + 3, "差异度为： ", dis)
   if dis <= minValue:
    minValue = dis
    minIndex = i
 return minIndex + 3

if __name__=="__main__":
 m=4
 print("Start testing...")
 A,y=LoadData(m)
 cl=xishu(A,y)
 print(m,"最有可能在类",judgeClass(A,cl,y),"中")
 print("end.....")