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

results = {"Own KNN_Regressor_fast":{}, "Own KNN_Regressor":{}, "Sklearn":{}}
k = 5
algorithm = "euclidean"
p=2 #p=1 manhattan, p=2 euclidean

correct = 0
print("Now running KNN_Regressor()")
start = time.time()
classifier = KNN(k=k, distanceFormula=algorithm)
for i, predict in enumerate(X_test):
    result = classifier.calc(X_train, Y_train, predict)
    if result[0][0] == Y_test[i]:
        correct += 1
computeTime = time.time() - start
results.get("Own KNN_Regressor").update({"Algorithm":algorithm,"Accuracy (%)":correct/len(Y_test), "Correct":correct, "Time (s)":computeTime})

correct = 0
print("Now running KNN_Regressor_fast()")
classifier2 = KNN_fast(k=k, distanceFormula="euclidean")
start = time.time()
for i, predict in enumerate(X_test):
    result = classifier2.calc(X_train, Y_train, predict)
    if result[0][0] == Y_test[i]:
        correct += 1
computeTime = time.time() - start
results.get("Own KNN_Regressor_fast").update({"Algorithm":algorithm,"Accuracy (%)":correct/len(Y_test), "Correct":correct, "Time (s)":computeTime})


print("Now running KNeighborsClassifier()")
classifier3 = KNeighborsClassifier(n_neighbors = k, p=p)
start = time.time()
classifier3.fit(X_train, Y_train)
y_pred = classifier3.predict(X_test)
computeTime = time.time() - start
result3 = accuracy_score(Y_test,y_pred)

results.get("Sklearn").update({"Algorithm":algorithm,"Accuracy (%)":correct/len(Y_test), "Correct":correct, "Time (s)":computeTime})

df = pd.DataFrame(results).transpose()
print("\n\n\n", df.to_latex())
print("\n",df)
