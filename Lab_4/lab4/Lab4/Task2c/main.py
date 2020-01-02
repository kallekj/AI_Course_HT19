import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier


print("*********** Loading data **************")
data = pd.read_csv("./Lab4PokerData_modified.csv", delimiter=";")
X = np.array(data.drop(["p2_final_action"], 1))
Y = np.array(data["p2_final_action"])
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.2)

print ('***************************************')
print('Length of Train Data:', len(X_train))
print('Length of Test Data:', len(X_test))
print ('***************************************')

classifiers = [    
    KNeighborsClassifier(n_neighbors = 2, p=1),
    KNeighborsClassifier(n_neighbors = 3, p=1),
    KNeighborsClassifier(n_neighbors = 4, p=1),
    KNeighborsClassifier(n_neighbors = 5, p=1),
    KNeighborsClassifier(n_neighbors = 6, p=1),
    KNeighborsClassifier(n_neighbors = 7, p=1),
    KNeighborsClassifier(n_neighbors = 8, p=1),
    KNeighborsClassifier(n_neighbors = 9, p=1),
    KNeighborsClassifier(n_neighbors = 10, p=1),
    KNeighborsClassifier(n_neighbors = 11, p=1),
    KNeighborsClassifier(n_neighbors = 12, p=1),
    KNeighborsClassifier(n_neighbors = 2, p=2),
    KNeighborsClassifier(n_neighbors = 3, p=2),
    KNeighborsClassifier(n_neighbors = 4, p=2),
    KNeighborsClassifier(n_neighbors = 5, p=2),
    KNeighborsClassifier(n_neighbors = 6, p=2),
    KNeighborsClassifier(n_neighbors = 7, p=2),
    KNeighborsClassifier(n_neighbors = 8, p=2),
    KNeighborsClassifier(n_neighbors = 9, p=2),
    KNeighborsClassifier(n_neighbors = 10, p=2),
    KNeighborsClassifier(n_neighbors = 11, p=2),
    KNeighborsClassifier(n_neighbors = 12, p=2),
    KNeighborsClassifier(n_neighbors = 2, p=2**1.5),
    KNeighborsClassifier(n_neighbors = 3, p=2**1.5),
    KNeighborsClassifier(n_neighbors = 4, p=2**1.5),
    KNeighborsClassifier(n_neighbors = 5, p=2**1.5),
    KNeighborsClassifier(n_neighbors = 6, p=2**1.5),
    KNeighborsClassifier(n_neighbors = 7, p=2**1.5),
    KNeighborsClassifier(n_neighbors = 8, p=2**1.5),
    KNeighborsClassifier(n_neighbors = 9, p=2**1.5),
    KNeighborsClassifier(n_neighbors = 10, p=2**1.5),
    KNeighborsClassifier(n_neighbors = 11, p=2**1.5),
    KNeighborsClassifier(n_neighbors = 12, p=2**1.5)
]

data = {"Classifier":[], "Neighbors":[], "Distance Measure":[], "Score":[]}

for i, classifier in enumerate(classifiers):
    if  classifier.get_params().get("p") == 1:
        data.get("Classifier").append("KNN")
        data.get("Neighbors").append(i+2)
        data.get("Distance Measure").append("Manhattan")
        score = cross_val_score(classifier, X_test, Y_test, cv=5)
        data.get("Score").append("%0.2f (+/-%0.2f)" % (score.mean(),score.std()*2))  
    elif classifier.get_params().get("p") == 2:
        data.get("Classifier").append("KNN")
        data.get("Neighbors").append((i-9))
        data.get("Distance Measure").append("Euclidean")
        score = cross_val_score(classifier, X_test, Y_test, cv=5)
        data.get("Score").append("%0.2f (+/-%0.2f)" % (score.mean(),score.std()*2))
    else:
        data.get("Classifier").append("KNN")
        data.get("Neighbors").append((i-20))
        data.get("Distance Measure").append("Minkowski p=$2^{1.5}$")
        score = cross_val_score(classifier, X_test, Y_test, cv=5)
        data.get("Score").append("%0.2f (+/-%0.2f)" % (score.mean(),score.std()*2))
data_df = pd.DataFrame(data)
print(data_df.to_latex())