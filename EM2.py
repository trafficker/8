import numpy as np
import pandas as pd
from math import log
from tree import *
import sys
import importlib
importlib.reload(sys)
import codecs
import operator
import copy
import json

def em_algorithm(data, valid_count, total_count, eps=1e-4):
    # data: 输入的一维数组，valid_count: 有效样本数
    # total_count: 样本总数，eps: 收敛所需精度
    # avg: 隐变量的均值，theta: 隐变量的方差
    valid_data = data[0:valid_count]
    avg = np.sum(valid_data) / total_count
    theta = np.sum(np.square(valid_data)) / total_count - avg
    while True:
        s1 = np.sum(valid_data) + avg * (total_count - valid_count)
        s2 = np.sum(np.square(valid_data)) + (avg * avg + theta) * (total_count - valid_count)
        new_avg = s1 / total_count
        new_theta = s2 / total_count - new_avg * new_avg
        if new_avg - avg <= eps and new_theta - theta <= eps:
            break
        else:
            avg, theta = new_avg, new_theta
    return avg, theta


def generation(dtype1, dtype2, latent_idx):
    # build NAIVE bayesian
    avg, var = [], []
    for idx in range(latent_idx):# 对隐变量之前的数据，正常计算其均值和方差
        type1, type2 = dtype1[:, idx], dtype2[:, idx] # type1 ,type2 为多维数据中的一维
        avg.append([np.average(type1), np.average(type2)])
        var.append([np.var(type1), np.var(type2)])  #EM Algorithm
    em_avg1, em_var1 = em_algorithm(data_type1[:40,
                                 latent_idx], 20, 40)
    em_avg2, em_var2 = em_algorithm(data_type2[:40,
                                 latent_idx], 20, 40)
    avg.append([em_avg1, em_avg2]) # 加入估计出的均值和方差
    var.append([em_var1, em_var2])
    return avg, var


def calc_gaussian(x, avg, var): # 构造高斯分布函数
    t = 1.0 / np.sqrt(2 * np.pi * var)
    return t * np.exp(-np.square(x - avg) / (2.0 * var))


if __name__ == '__main__':
    data_str = open('ecoli.data').readlines()
    data_type1 = np.ndarray([50, 7], np.float32)
    data_type2 = np.ndarray([50, 7], np.float32)
    for idx in range(50):
     data_type1[idx] = data_str[idx].strip('\n').split(',')[0:7]
    for idx in range(50, 100):
     data_type2[idx - 50] = data_str[idx].strip('\n').split(',')[0:7]
    a, v = generation(data_type1[:40], data_type2[:40], 6)
    data_test = np.concatenate((data_type1[40:], data_type2[40:]))
    correct = 0
    for data_idx in range(len(data_test)):
        data = data_test[data_idx]
        val_type1, val_type2 = 0.5, 0.5
        for idx in range(7):
         val_type1 *= calc_gaussian(data[idx], a[idx][0], v[idx][0])   #朴素贝叶斯计算
         val_type2 *= calc_gaussian(data[idx], a[idx][1], v[idx][1])
        if val_type1 > val_type2 and data_idx < 10:
            correct += 1
        elif val_type1 < val_type2 and data_idx >= 10:
            correct += 1
        print("Number: %2d, cp: %f, im: %f"
              % (data_idx + 1, val_type1, val_type2))
    print("Accuracy: %.1f%%" % (correct * 5))