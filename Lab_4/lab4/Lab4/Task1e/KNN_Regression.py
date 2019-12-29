import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from operator import itemgetter
from collections import Counter
import warnings
import math
import copy


class kList:
    def __init__(self, k):
        self.maxLength = k
        self.theList = [[float("inf"), float("inf")]]
    
    def push(self, item):
        self.theList.append(item)
        self.theList.sort(key=itemgetter(0))
        if len(self.theList) > self.maxLength:
            self.theList.pop()


# This is the new and improved one, takes about 5sec on this dataset. It only appends the calculated distance if it's shorter than the max(distance) in the list.
class KNN_Regressor_fast:
    def __init__(self, k=5, distanceFormula="euclidean"):
        self.k = k
        self.distanceFormula = distanceFormula
    
    def calc(self, X_train, Y_train, predict):
        def _manhattan(feature, predict):
            return np.sum(np.abs(np.array(feature)-np.array(predict)))
    
        def _euclidean(feature, predict):
            return np.linalg.norm(np.array(feature)-np.array(predict))

        if self.k < 3 and self.k%2 == 0:
            warnings.warn("K cannot be less than 3 and must not be even!")
            return -1

        dists = kList(self.k)
        for i, feature in enumerate(X_train):
            if self.distanceFormula == "euclidean":
                dist = _euclidean(feature, predict)
            else:
                dist = _manhattan(feature, predict)
            if dist <= max(dists.theList)[0]:
                dists.push([dist, Y_train[i]])

        kNeighborsClass = [neighbors[1] for neighbors in dists.theList[:self.k]]
        predictedClass = sum(kNeighborsClass)/len(kNeighborsClass)
        return predictedClass


# My first implementation of KNN, this one is really slow, takes approx 40sec on this dataset.
class KNN_Regressor:
    def __init__(self, k=5, distanceFormula="euclidean"):
        self.k = k
        self.distanceFormula = distanceFormula
    
    def calc(self, X_train, Y_train, predict):
        def _manhattan(feature, predict):
            return np.sum(np.abs(np.array(feature)-np.array(predict)))
    
        def _euclidean(feature, predict):
            return np.linalg.norm(np.array(feature)-np.array(predict))

        if self.k < 3 and self.k%2 == 0:
            warnings.warn("K cannot be less than 3 and must not be even!")
            return -1
             
        dists = []
        for i, feature in enumerate(X_train):
            if self.distanceFormula == "euclidean":
                dist = _euclidean(feature, predict)
            else:
                dist = _manhattan(feature, predict)
            dists.append([dist, Y_train[i]])
            dists.sort(key=itemgetter(0))

        kNeighborsClass = [neighbors[1] for neighbors in dists[:self.k]]
        predictedClass = sum(kNeighborsClass)/len(kNeighborsClass)
        return predictedClass


