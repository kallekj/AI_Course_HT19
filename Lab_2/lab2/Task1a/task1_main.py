import path_planning as pp
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from node import Node

from task1_USA_RS import RandomSearch
from task1_USA_BFS import BFSearch
from task1_USA_DFS import DFSearch
from task1_ISA_GreedySearch_Euclidean import GreedySearchE
from task1_ISA_GreedySearch_Manhattan import GreedySearchM
from task1_ISA_Astar_Euclidean import AstarE
from task1_ISA_Astar_Manhattan import AstarM



BFS_Data=[]
Random_Data=[]
DFS_Data=[]

for i in range(100):
    print(i)
    BFSAgent = BFSearch()
    RandomAgent = RandomSearch()
    DFSAgent = DFSearch()

    map_object = pp.generateMap2d([100, 100])
    map_object2 = np.copy(map_object)
    map_object3 = np.copy(map_object)

    start = Node([np.where(map_object == -2)[0][0], np.where(map_object == -2)[1][0]], None, 0, 0)
    goal = Node([np.where(map_object == -3)[0][0], np.where(map_object == -3)[1][0]], None, 0, 0)

    BFSAgent.search(map_object, start, goal)
    RandomAgent.search(map_object2, start, goal)
    DFSAgent.search(map_object3, start, goal)

    BFS_Data.append({"nodes":BFSAgent.searchedNodes, "pathLength":len(BFSAgent.path[0]) + len(BFSAgent.path[1])})
    Random_Data.append({"nodes":RandomAgent.searchedNodes, "pathLength":len(RandomAgent.path[0]) + len(RandomAgent.path[1])})
    DFS_Data.append({"nodes":DFSAgent.searchedNodes, "pathLength":len(DFSAgent.path[0]) + len(DFSAgent.path[1])})

BFS_DF = pd.DataFrame(BFS_Data)
BFS_Mean = BFS_DF.mean(axis=0)
Random_DF = pd.DataFrame(Random_Data)
Random_Mean = Random_DF.mean(axis=0)
DFS_DF = pd.DataFrame(DFS_Data)
DFS_Mean = DFS_DF.mean(axis=0)

print("\n       BFS Mean")
print(BFS_Mean)
print("\n       Random Mean")
print(Random_Mean)
print("\n       DFS Mean")
print(DFS_Mean)



print("")
print(BFS_Mean.to_latex())
print("")
print(Random_Mean.to_latex())
print("")
print(DFS_Mean.to_latex())



# # map_object, info = pp.generateMap2d([60,60])
# map_object = pp.generateMap2d([100, 100])
# map_object2 = np.copy(map_object)
# map_object3 = np.copy(map_object)

# start = Node([np.where(map_object == -2)[0][0], np.where(map_object == -2)[1][0]], None, 0, 0)
# goal = Node([np.where(map_object == -3)[0][0], np.where(map_object == -3)[1][0]], None, 0, 0)

# searcher = AstarM()
# searcher.search(map_object, start, goal)
# print("\nA* Manhattan")
# print("Number of visited nodes: {}".format(searcher.searchedNodes))
# print("Length of path: {}".format(len(searcher.path[0])+len(searcher.path[1])))
# #pp.plotMap(map_object,searcher.path)



# searcher2 = AstarE()
# searcher2.search(map_object2, start, goal)
# print("\nA* Euclidean")
# print("Number of visited nodes: {}".format(searcher2.searchedNodes))
# print("Length of path: {}".format(len(searcher2.path[0])+len(searcher2.path[1])))
# #pp.plotMap(map_object2,searcher2.path)

# searcher3 = BFSearch()
# searcher3.search(map_object3, start, goal)
# print("\nBFS")
# print("Number of visited nodes: {}".format(searcher3.searchedNodes))
# print("Length of path: {}".format(len(searcher3.path[0])+len(searcher3.path[1])))
#pp.plotMap(map_object3,searcher3.path)
