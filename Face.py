import os
import pickle
import numpy as np
from PIL import Image
data=[]
label=[]
traindata=[]
trainlabel=[]
testdata=[]
testlabel=[]
finalw=[]
def loadData():
  #从图片集中获得训练集和测试集。
  #其中训练集为720组，测试集为240组
  j = 1
  for i in range(720):  #读入图片
    if j>6:
        j=1
    if (i+1)%6==0:
        ph=int((i+1)/6)
    else:
      ph=int((i+1)/6)+1
    s=str(ph)+'-'+str(j)+'.bmp'
    s1="E:\project\o\\feret"
    img=Image.open(s1+'\\'+s,'r')
    pdata=np.asarray(img,'float64')/256  #图片转换成数据格式存储
    pdata=pdata.reshape((10304))
    data.append(pdata)
    label.append(ph)
    if j<=3:
      traindata.append(pdata)
      trainlabel.append(ph)
    if j>=4:
      testdata.append(pdata)
      testlabel.append(ph)
    #print(pdata)
    j=j+1
  print(len(testdata[0]))
  print((len(testdata)))
  print("==================")
def train(traindata):
   finalw=[]
   L=1

   wk= 0*np.ones((3,1))
   wki=0.5*np.ones((3,1))
   res=9*np.ones(wki.shape)
   #for j in range(240):
    # for h in range (112):
     #  for m in range (92):
      #   t[j1][h1][m1]= np.abs(testlabel[j1][h1][m1]- testdata[j1][h1][m1])
       #  m1+=1
      # h1+=1

   td=np.transpose(np.array(traindata)) #得到训练集数组
   count=0
   finalw0=[]
   for v in range(400):
       print("新一次迭代开始！！！——————————————————————")
     #for i in range(360):
       # #定义lamda
       lamda= 0.4* np.ones((3, 10304))
       #print(tdz)
       #for j in range((len(t))):
        #for h in range (len(t[0])):
         # t[j][h]=testlabel[i][j][h]-testlabel[i][j][h
       tdt=np.transpose(td) #图片数据项的转置
       #print(tdt.shape)
       for d in range(10304):

        for p in range(3):
          if(wki[p][0]+tdt[p][d]/0.5>lamda[p][d]/0.5):
            wki[p][0]=wki[p][0]+tdt[p][d]/0.5-lamda[p][d]/0.5
            #print(wki[d])
            print("---------————---------------------")
          elif(wki[p][0]+tdt[p][d]/0.5<=lamda[p][d]/0.5) and (wki[p][0]+tdt[p][d]/0.5>=-lamda[p][d]/0.5):
            wki[p][0]=0

            print("0.00")
          elif (wki[p][0]+tdt[p][d]/0.5<-lamda[p][d]/0.5):
            wki[p][0] = float(wki[p][0]+tdt[p][d]/0.5 + lamda[p][d]/0.5)
            #print(wki[d])
            print("+++++++++++++++++++++++++++++++++++++")

        print("该项结束")
       print(wki)
       print("该次该图结束：：：：")
       if(np.linalg.norm(wki-res)<0.0001):
           print("????????????")
           #print(res)
           print(np.linalg.norm(wki-res))
           #break
       print("+++++++")
       count+=1
       res=wki

   print(count)
   print("训练结束")
   return wki
def test(wki,testdata,traindata): #检测函数
    testd=np.transpose(np.array(testdata))
    traind = np.transpose(np.array(traindata))
    correct=0
    print(testd.shape)
    print(traind.shape)
    for j in range(10304):
      if(np.linalg.norm(testd[j][0]-np.dot(traind,wki)[j]) <=0.1):
        correct+=1
    #print(testd)
    print("--+++_))")
    #print(traind)
    print(testd)
    print(np.dot(traind,wki))
    print("正确率为:%d"%(correct/10304))

if __name__=="__main__":
    loadData()
    trainX1=traindata[0:3]
    tX1=np.transpose(np.array(trainX1))
    wki=train(trainX1)
    testdataX1=testdata[0:1]
    print("测试开始.....")
    test(wki,testdataX1,trainX1)
    print("end")
