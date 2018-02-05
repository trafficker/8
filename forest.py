import numpy as np
from sklearn import tree
trees=[]
def generalize(data,label,treenum):
    lenth=len(label)
    for i in range(treenum):
        count=np.random.randint(0, lenth,lenth//4,np.int)
        data0,label0=data[count],label[count]
        tree1= tree.DecisionTreeRegressor()
        tree1.fit(data0,label0)
        trees.append(tree1)

def predict(data):
    lenth=len(data)
    re=np.zeros(lenth,np.int)
    for t in  trees:
        re+= t.predict(data).astype(np.int)
    zheng=np.where(re>lenth//2)
    fu=np.where(re<=lenth//2)
    re[zheng],re[fu]=0,1
    return re

if __name__=="__main__":
    file=open("wine.data")
    str=file.readlines()
    l=len(str)
    np.random.shuffle(str)
    file.close()
    label=np.ndarray([l],np.int)
    value=np.ndarray([l,13],np.float32)
    for i in range(l):
     dataall =str[i].strip('\n').split(',')
     value[i]=dataall[1: ]
     label[i]=dataall[0]
    generalize(value[:100],label[:100],30)
    result=predict(value[100:])
    errornum = len(np.where(label[100:] != result)[0])
    print(errornum)
    #print(np.where(label[1000:] != result))
    print(result)
    print("kgkgkghkg")
    print(label[100:])
    print('correct_rate: %.2f%%' % ((30.0 - errornum)* 100 /30), end='\r')