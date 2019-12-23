import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from ownKNN import KNN, KNN_fast
import time

print("*********** Loading data **************")
data = pd.read_csv("../Lab4Data.csv", delimiter=";")
X = np.array(data.drop(["DriverPerformance"], 1))
Y = np.array(data["DriverPerformance"])
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.2)

print ('***************************************')
print('Length of Train Data:', len(X_train))
print('Length of Test Data:', len(X_test))
print ('***************************************')

correct = 0
classifier = KNN(k=5, distanceFormula="euclidean")
start = time.time()
for i, predict in enumerate(X_test):
    result = classifier.calc(X_train, Y_train, predict)
    if result[0][0] == Y_test[i]:
        correct += 1

print("Accuracy of own KNN: {} and took {}s to calculate, correct: {}".format(correct/len(Y_test), time.time()-start, correct))

correct = 0
classifier2 = KNN_fast(k=5, distanceFormula="euclidean")
start = time.time()
for i, predict in enumerate(X_test):
    result = classifier2.calc(X_train, Y_train, predict)
    if result[0][0] == Y_test[i]:
        correct += 1

print("Accuracy of own KNN_fast: {} and took {}s to calculate, correct: {}".format(correct/len(Y_test), time.time()-start, correct))



classifier3 = KNeighborsClassifier(n_neighbors = 5)
start = time.time()
classifier3.fit(X_train, Y_train)
y_pred = classifier3.predict(X_test)
result3 = accuracy_score(Y_test,y_pred)

print("Accuracy of sklearn KNN: {} and took {}s to calculate".format(result3, time.time()-start))

