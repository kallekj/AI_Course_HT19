import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import accuracy_score
from KNN_Regression import KNN_Regressor, KNN_Regressor_fast
import time

print("*********** Loading data **************")
data = pd.read_csv("../Lab4Data.csv", delimiter=";")
X = np.array(data.drop(["FuelConsum"], 1))
Y = np.array(data["FuelConsum"])
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.2)

print ('***************************************')
print('Length of Train Data:', len(X_train))
print('Length of Test Data:', len(X_test))
print ('***************************************')


results = {"Own KNN_Regressor_fast":{}, "Own KNN_Regressor":{}, "Sklearn":{}}
k = 5
algorithm = "euclidean"
p=2 #p=1 manhattan, p=2 euclidean


print("Now running KNN_Regressor_fast()")
start = time.time()
classifier = KNN_Regressor_fast(k=k, distanceFormula=algorithm)
tempRes = []
for i, predict in enumerate(X_test):
    tempRes.append(classifier.calc(X_train, Y_train, predict))
computeTime = time.time() - start

# This is the score algorithm from Sklearn
# score = 1 - u/v
# u = ((y_true - y_pred) ** 2).sum()
# v = ((y_true - y_true.mean()) ** 2).sum()
u = np.sum(np.square(Y_test - np.array(tempRes)))
v = np.sum(np.square(Y_test - Y_test.mean()))
score = (1 - u/v)
results.get("Own KNN_Regressor_fast").update({"Algorithm":algorithm, "Score":score, "Time (s)":computeTime})

print("Now running KNN_Regressor()")
start = time.time()
classifier = KNN_Regressor(k=k, distanceFormula=algorithm)
tempRes = []
for i, predict in enumerate(X_test):
    tempRes.append(classifier.calc(X_train, Y_train, predict))
computeTime = time.time() - start

# This is the score algorithm from Sklearn
# score = 1 - u/v
# u = ((y_true - y_pred) ** 2).sum()
# v = ((y_true - y_true.mean()) ** 2).sum()
u = np.sum(np.square(Y_test - np.array(tempRes)))
v = np.sum(np.square(Y_test - Y_test.mean()))
score = (1 - u/v)
results.get("Own KNN_Regressor").update({"Algorithm":algorithm, "Score":score, "Time (s)":computeTime})

print("Now running sklearn KNeighborsRegressor()")
start = time.time()
classifier3 = KNeighborsRegressor(n_neighbors = k, p=p)
classifier3.fit(X_train, Y_train)
computeTime = time.time() - start
results.get("Sklearn").update({"Algorithm":algorithm, "Score":classifier3.score(X_test, Y_test), "Time (s)":computeTime})


df = pd.DataFrame(results).transpose()
print("\n\n\n", df.to_latex())
print("\n",df)