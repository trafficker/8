import os
import random
import math
os.chdir(u"D:\gnuplot")
from svmutil import *
import numpy
Data_Set=[]
Data_Lab=[]
for k in range(5):
    arr = numpy.random.random([30,45])
    lab =[k]*30
    for i in numpy.arange(0,30):
        j =i%3
        arr[i,k*9+j*3:k*9+j*3+3]=arr[i,k*9+j*3:k*9+j*3+3]+100
    print(arr.shape)
    Data_Set.append(arr)
    Data_Lab.append(lab)
train = Data_Set[0].tolist()
m =svm_train(Data_Lab[0], Data_Set[0].tolist(),'-c 10 -t 0 -p 10')
p_label,p_acc,p_val=svm_predict(Data_Lab[0],Data_Set[0].tolist(),m)
