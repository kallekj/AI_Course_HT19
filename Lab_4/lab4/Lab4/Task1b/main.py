import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
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

results = {"SVC":{}, "Decision Tree":{}, "Random Forest":{}}

classifiers = [
    SVC(kernel="linear", C=0.025),
    DecisionTreeClassifier(max_depth=5),
    RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1)
]

names = ["SVC", "Decision Tree", "Random Forest"]

for classifier, name in zip(classifiers, names):
    start = time.time()
    classifier.fit(X_train, Y_train)
    computeTime = time.time() - start
    results.get(name).update({"Score":classifier.score(X_test, Y_test), "Time (s)":computeTime})

df = pd.DataFrame(results).transpose()
print("\n\n\n", df.to_latex())
print("\n",df)
