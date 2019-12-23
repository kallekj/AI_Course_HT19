import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from operator import itemgetter
from collections import Counter
import warnings
import math
import copy


class KNN:
    def __init__(self, k=5, distanceFormula="euclidean"):
        self.k = k
        self.distanceFormula = distanceFormula
    
    def calc(self, X_train, Y_train, predict):
        def _manhattan(feature, predict):
            return np.sum(np.array(feature)-np.array(predict))
    
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

        votes = [neighbors[1] for neighbors in dists[:self.k]]
        nVotes = Counter(votes).most_common(1)
        return nVotes


class kList:
    def __init__(self, k):
        self.maxLength = k
        self.theList = [[float("inf"), float("inf")]]
    
    def push(self, item):
        self.theList.append(item)
        self.theList.sort(key=itemgetter(0))
        if len(self.theList) > self.maxLength:
            self.theList.pop()


class KNN_fast:
    def __init__(self, k=5, distanceFormula="euclidean"):
        self.k = k
        self.distanceFormula = distanceFormula
    
    def calc(self, X_train, Y_train, predict):
        def _manhattan(feature, predict):
            return np.sum(np.array(feature)-np.array(predict))
    
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
            if dist < max(dists.theList[0]):
                dists.push([dist, Y_train[i]])

        votes = [neighbors[1] for neighbors in dists.theList[:self.k]]
        nVotes = Counter(votes).most_common(1)
        return nVotes



    
    
