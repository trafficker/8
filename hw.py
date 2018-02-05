#!/usr/bin/env Python
# coding=utf-8
from numpy import *
import pandas as pd
import sys
import importlib
importlib.reload(sys)
import codecs
import operator
import copy
import json
from tree import *
import csv



def calcGini(dataSet):
    numEntries = len(dataSet)
    labelCounts = {}
    for featVec in dataSet:  # the the number of unique elements and their occurance
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    Gini = 1.0
    for key in labelCounts:
        prob = float(labelCounts[key]) / numEntries
        Gini -= prob * prob  # log base 2
    return Gini


def splitDataSet(dataSet, axis, value):
    returnMat = []
    for data in dataSet:
        if data[axis] == value:
            returnMat.append(data[:axis] + data[axis + 1:])
    return returnMat




def splitContinuousDataSet(dataSet, axis, value, direction):
    retDataSet = []
    for featVec in dataSet:
        if direction == 0:
            if featVec[axis] > value:
                # retDataSet.append(featVec[:axis] + featVec[axis + 1:])

                retDataSet.append(featVec)
        else:
            if featVec[axis] <= value:
                # retDataSet.append(featVec[:axis] + featVec[axis + 1:])

                retDataSet.append(featVec)
    return retDataSet



def chooseBestFeatureToSplit(dataSet, labels):
    numFeatures = len(dataSet[0]) - 1
    bestGini = 10000.0
    bestFeature = -1
    bestSplitDict = {}
    for i in range(numFeatures):

        featList = [example[i] for example in dataSet]

        if type(featList[0]).__name__ == 'float' or type(featList[0]).__name__ == 'int':

            sortfeatList = sorted(featList)
            splitList = []
            for j in range(len(sortfeatList) - 1):
                splitList.append((sortfeatList[j] + sortfeatList[j + 1]) / 2.0)
            bestSplitGini = 10000

            for value in splitList:
                newGini = 0.0
                subDataSet0 = splitContinuousDataSet(dataSet, i, value, 0)
                subDataSet1 = splitContinuousDataSet(dataSet, i, value, 1)
                prob0 = len(subDataSet0) / float(len(dataSet))
                newGini += prob0 * calcGini(subDataSet0)
                prob1 = len(subDataSet1) / float(len(dataSet))
                newGini += prob1 * calcGini(subDataSet1)
                if newGini < bestSplitGini:
                    bestSplitGini = newGini
                    bestSplit = value
            bestSplitDict[labels[i]] = bestSplit
            newGini = bestSplitGini
        else:
            uniqueVals = set(featList)
            newGini = 0.0
            for value in uniqueVals:
                subDataSet = splitDataSet(dataSet, i, value)
                prob = len(subDataSet) / float(len(dataSet))
                newGini += prob * calcGini(subDataSet)
        if newGini < bestGini:
            bestGini = newGini
            bestFeature = i

    if type(dataSet[0][bestFeature]).__name__ == 'float' or type(dataSet[0][bestFeature]).__name__ == 'int':
        bestSplitValue = bestSplitDict[labels[bestFeature]]
        labels[bestFeature] = labels[bestFeature] + '<=' + str(bestSplitValue)
        for i in range(shape(dataSet)[0]):
            if dataSet[i][bestFeature] <= bestSplitValue:
                dataSet[i][bestFeature] = 1
            else:
                dataSet[i][bestFeature] = 0
    return bestFeature


def majorityCnt(classList):
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys(): classCount[vote] = 0
        classCount[vote] += 1

    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)

    return sortedClassCount[0][0]


def classify(inputTree, featLabels, testVec):
    firstStr = inputTree.keys()[0]
    if u'<=' in firstStr:
        featvalue = float(firstStr.split(u"<=")[1])
        featkey = firstStr.split(u"<=")[0]
        secondDict = inputTree[firstStr]
        featIndex = featLabels.index(featkey)
        if testVec[featIndex] <= featvalue:
            judge = 1
        else:
            judge = 0
        for key in secondDict.keys():
            if judge == int(key):
                if type(secondDict[key]).__name__ == 'dict':
                    classLabel = classify(secondDict[key], featLabels, testVec)
                else:
                    classLabel = secondDict[key]
    else:
        secondDict = inputTree[firstStr]
        featIndex = featLabels.index(firstStr)
        for key in secondDict.keys():
            if testVec[featIndex] == key:
                if type(secondDict[key]).__name__ == 'dict':
                    classLabel = classify(secondDict[key], featLabels, testVec)
                else:
                    classLabel = secondDict[key]
    return classLabel


def testing(myTree, data_test, labels):
    error = 0.0
    for i in range(len(data_test)):
        if classify(myTree, labels, data_test[i]) != data_test[i][-1]:
            error += 1
    # print 'myTree %d' % error
    return float(error)


def testing_feat(feat, train_data, test_data, labels):
    class_list = [example[-1] for example in train_data]
    bestFeatIndex = labels.index(feat)
    train_data = [example[bestFeatIndex] for example in train_data]
    test_data = [(example[bestFeatIndex], example[-1]) for example in test_data]
    all_feat = set(train_data)
    error = 0.0
    for value in all_feat:
        class_feat = [class_list[i] for i in range(len(class_list)) if train_data[i] == value]
        major = majorityCnt(class_feat)
        for data in test_data:
            if data[0] == value and data[1] != major:
                error += 1.0
    # print 'myTree %d' % error
    return error


def testingMajor(major, data_test):
    error = 0.0
    for i in range(len(data_test)):
        if major != data_test[i][-1]:
            error += 1
    # print 'major %d' % error
    return float(error)


def postPruningTree(inputTree,dataSet,data_test,labels):
     firstSides = list(myTree.keys())
     firstStr = firstSides[0]
     secondDict=inputTree[firstStr]
     classList=[example[-1] for example in dataSet]
     featkey=copy.deepcopy(firstStr)
     if u'<=' in firstStr:
         featkey=firstStr.split(u'<=')[0]
         featvalue=float(firstStr.split(u'<=')[1])
     labelIndex=labels.index(featkey)
     temp_labels=copy.deepcopy(labels)
     del(labels[labelIndex])
     for key in secondDict.keys():
         if type(secondDict[key]).__name__=='dict':
             if type(dataSet[0][labelIndex]).__name__=='unicode':
                 inputTree[firstStr][key]=postPruningTree(secondDict[key],\
                  splitDataSet(dataSet,labelIndex,key),splitDataSet(data_test,labelIndex,key),copy.deepcopy(labels))
             else:
                 inputTree[firstStr][key]=postPruningTree(secondDict[key],\
                 splitContinuousDataSet(dataSet,labelIndex,featvalue,key),\
                 splitContinuousDataSet(data_test,labelIndex,featvalue,key),\
                 copy.deepcopy(labels))
     if testing(inputTree,data_test,temp_labels)<=testingMajor(majorityCnt(classList),data_test):
         return inputTree
     return majorityCnt(classList)





def createTree(dataSet, labels, data_full, labels_full, test_data, mode="unpro"):
    classList = [example[-1] for example in dataSet]
    if classList.count(classList[0]) == len(classList):
        return classList[0]
    if len(dataSet[0]) == 1:
        return majorityCnt(classList)

    labels_copy = copy.deepcopy(labels)
    bestFeat = chooseBestFeatureToSplit(dataSet, labels)
    bestFeatLabel = labels[bestFeat]
    if mode == "unpro" or mode == "post":
        myTree = {bestFeatLabel: {}}
    elif mode == "prev":
        if testing_feat(bestFeatLabel, dataSet, test_data, labels_copy) < testingMajor(majorityCnt(classList),
                                                                                       test_data):
            myTree = {bestFeatLabel: {}}
        else:
            return majorityCnt(classList)

    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)

    if type(dataSet[0][bestFeat]).__name__ == 'unicode':
        currentlabel = labels_full.index(labels[bestFeat])
        featValuesFull = [example[currentlabel] for example in data_full]
        uniqueValsFull = set(featValuesFull)

    del (labels[bestFeat])

    for value in uniqueVals:
        subLabels = labels[:]
        if type(dataSet[0][bestFeat]).__name__ == 'unicode':
            uniqueValsFull.remove(value)

        myTree[bestFeatLabel][value] = createTree(splitDataSet \
                                                      (dataSet, bestFeat, value), subLabels, data_full, labels_full,
                                                  splitDataSet \
                                                      (test_data, bestFeat, value), mode=mode)
    if type(dataSet[0][bestFeat]).__name__ == 'unicode':
        for value in uniqueValsFull:
            myTree[bestFeatLabel][value] = majorityCnt(classList)

    if mode == "post":
        if testing(myTree, test_data, labels_copy) > testingMajor(majorityCnt(classList), test_data):
            return majorityCnt(classList)
    return myTree


def load_data(file_name):
    with open(r"dd.csv", 'rb') as f:
      df = pd.read_csv(f,sep=",")
      print(df)
      train_data = df.values[:11, 1:].tolist()
     # train_data=df.values[:11,1:].tolist()
    print(train_data)
    test_data = df.values[11:, 1:].tolist()
    labels = df.columns.values[1:-1].tolist()
    return train_data, test_data, labels


if __name__ == "__main__":
    train_data, test_data, labels = load_data("dd.csv")
    data_full = train_data[:]
    labels_full = labels[:]

    mode="unpro"
    mode = "prev"
    myTree = createTree(train_data, labels, data_full, labels_full, test_data, mode=mode)
    #myTree = postPruningTree(myTree,train_data,test_data,labels_full)
    createPlot(myTree)
    print(json.dumps(myTree, ensure_ascii=False, indent=4))