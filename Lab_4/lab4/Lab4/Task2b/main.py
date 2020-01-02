import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
import time


print("*********** Loading data **************")
data = pd.read_csv("./Lab4PokerData_modified.csv", delimiter=";")
X = np.array(data.drop(["p2_final_action"], 1))
Y = np.array(data["p2_final_action"])
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.2)

print ('***************************************')
print('Length of Train Data:', len(X_train))
print('Length of Test Data:', len(X_test))
print ('***************************************')


results = {"KNN":{}, "SVC":{}, "Decision Tree":{}}

classifiers = [
    KNeighborsClassifier(n_neighbors = 5),
    SVC(kernel="linear", C=0.025),
    DecisionTreeClassifier(max_depth=5),
]

names = ["KNN", "SVC", "Decision Tree"]

for classifier, name in zip(classifiers, names):
    print(name)
    start = time.time()
    classifier.fit(X_train, Y_train)
    computeTime = time.time() - start
    results.get(name).update({"Score":classifier.score(X_test, Y_test), "Time (s)":computeTime})

df = pd.DataFrame(results).transpose()
print("\n\n\n", df.to_latex())
print("\n",df)