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
from task1_ISA_Astar_Custom import AstarC

BFS_Data = []
AStar_Man = []
AStar_Euc = []
#AStar_Cust_E = []
AStar_Cust_M = []
Greedy_M_Data = []
Greedy_E_Data = []

for i in range(100):
    print(i)
    BFSAgent = BFSearch()
    AStar_Man_Agent = AstarM()
    AStar_Euc_Agent = AstarE()
    AStar_Cust_M_Agent = AstarC()
    Greedy_agent_m = GreedySearchM()
    Greedy_agent_e = GreedySearchE()


    map_object, info = pp.generateMap2d_obstacle([100, 100])
    map_object2 = np.copy(map_object)
    map_object3 = np.copy(map_object)
    map_object4 = np.copy(map_object)
    map_object5 = np.copy(map_object)
    map_object6 = np.copy(map_object)

    start = Node([np.where(map_object == -2)[0][0], np.where(map_object == -2)[1][0]], None, 0, 0)
    goal = Node([np.where(map_object == -3)[0][0], np.where(map_object == -3)[1][0]], None, 0, 0)

    AStar_Man_Agent.search(map_object, start, goal)
    AStar_Euc_Agent.search(map_object2, start, goal)
    AStar_Cust_M_Agent.search(map_object3, start, goal, info)
    BFSAgent.search(map_object4, start, goal)
    Greedy_agent_m.search(map_object5, start, goal)
    Greedy_agent_e.search(map_object6, start, goal)

    BFS_Data.append({"nodes":BFSAgent.searchedNodes, "pathLength":len(BFSAgent.path[0]) + len(BFSAgent.path[1])})
    AStar_Man.append({"nodes":AStar_Man_Agent.searchedNodes, "pathLength":len(AStar_Man_Agent.path[0]) + len(AStar_Man_Agent.path[1])})
    AStar_Euc.append({"nodes":AStar_Euc_Agent.searchedNodes, "pathLength":len(AStar_Euc_Agent.path[0]) + len(AStar_Euc_Agent.path[1])})
    AStar_Cust_M.append({"nodes":AStar_Cust_M_Agent.searchedNodes, "pathLength":len(AStar_Cust_M_Agent.path[0]) + len(AStar_Cust_M_Agent.path[1])})
    Greedy_M_Data.append({"nodes":Greedy_agent_m.searchedNodes, "pathLength":len(Greedy_agent_m.path[0]) + len(Greedy_agent_m.path[1])})
    Greedy_E_Data.append({"nodes":Greedy_agent_e.searchedNodes, "pathLength":len(Greedy_agent_e.path[0]) + len(Greedy_agent_e.path[1])})
    

BFS_DF = pd.DataFrame(BFS_Data)
BFS_Mean = BFS_DF.mean(axis=0)
AStarM_DF = pd.DataFrame(AStar_Man)
AStarM_Mean = AStarM_DF.mean(axis=0)
AStarE_DF = pd.DataFrame(AStar_Euc)
AStarE_Mean = AStarE_DF.mean(axis=0)
AStarC_DF = pd.DataFrame(AStar_Cust_M)
AStarC_Mean = AStarC_DF.mean(axis=0)
GreedyM_DF = pd.DataFrame(Greedy_M_Data)
GreedyM_Mean = GreedyM_DF.mean(axis=0) 
GreedyE_DF = pd.DataFrame(Greedy_E_Data)
GreedyE_Mean = GreedyE_DF.mean(axis=0) 



print("\n       BFS Mean")
print(BFS_Mean)
print("\n       A* Manhattan Mean")
print(AStarC_Mean)
print("\n       A* Euclidean Mean")
print(AStarE_Mean)
print("\n       A* Custom Mean")
print(AStarC_Mean)
print("\n       Greedy Manhattan Mean")
print(GreedyM_Mean)
print("\n       Greedy Euclidean Mean")
print(GreedyE_Mean)



print("")
print(BFS_Mean.to_latex())
print("")
print(AStarM_Mean.to_latex())
print("")
print(AStarE_Mean.to_latex())
print("")
print(AStarC_Mean.to_latex())
print("")
print(GreedyM_Mean.to_latex())
print("")
print(GreedyE_Mean.to_latex())


# map_object, info = pp.generateMap2d_obstacle([100, 100])
# #plt.imshow(map_object)
# map_object2 = np.copy(map_object)
# map_object3 = np.copy(map_object)

# start = Node([np.where(map_object == -2)[0][0], np.where(map_object == -2)[1][0]], None, 0, 0)
# goal = Node([np.where(map_object == -3)[0][0], np.where(map_object == -3)[1][0]], None, 0, 0)

# print(info)
# print("Start node is: {}".format(start.pos))
# print("Goal node is at: {}".format(goal.pos))

# searcher = AstarE()
# searcher.search(map_object, start, goal)
# print("\nA* Euclidean")
# print("Number of visited nodes: {}".format(searcher.searchedNodes))
# print("Length of path: {}".format(len(searcher.path[0])+len(searcher.path[1])))
# pp.plotMap(map_object,searcher.path)



# searcher2 = AstarC()
# searcher2.search(map_object2, start, goal, info)
# print("\nA* Custom")
# print("Number of visited nodes: {}".format(searcher2.searchedNodes))
# print("Length of path: {}".format(len(searcher2.path[0])+len(searcher2.path[1])))
# pp.plotMap(map_object2,searcher2.path)

# # searcher3 = BFSearch()
# # searcher3.search(map_object3, start, goal)
# # print("\nBFS")
# # print("Number of visited nodes: {}".format(searcher3.searchedNodes))
# # print("Length of path: {}".format(len(searcher3.path[0])+len(searcher3.path[1])))
# # #pp.plotMap(map_object3,searcher3.path)
