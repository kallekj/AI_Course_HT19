import path_planning as pp
import matplotlib.pyplot as plt
import numpy as np
from node import Node

from task1_USA_RS import RandomSearch
from task1_USA_BFS import BFSearch
from task1_USA_DFS import DFSearch
from task1_ISA_GreedySearch_Euclidean import GreedySearchE
from task1_ISA_GreedySearch_Manhattan import GreedySearchM
from task1_ISA_Astar import Astar



# map_object, info = pp.generateMap2d([60,60])
map_object = pp.generateMap2d([60, 60])
map_object2 = np.copy(map_object)
map_object3 = np.copy(map_object)

start = Node([np.where(map_object == -2)[0][0], np.where(map_object == -2)[1][0]], None, 0, 0)
goal = Node([np.where(map_object == -3)[0][0], np.where(map_object == -3)[1][0]], None, 0, 0)

searcher = Astar()
searcher.search(map_object, start, goal)
print("\nA*")
print("Number of visited nodes: {}".format(searcher.searchedNodes))
print("Length of path: {}".format(len(searcher.path[0])+len(searcher.path[1])))
pp.plotMap(map_object,searcher.path)



searcher2 = GreedySearchM()
searcher2.search(map_object2, start, goal)
print("\nGreedy Manhattan")
print("Number of visited nodes: {}".format(searcher2.searchedNodes))
print("Length of path: {}".format(len(searcher2.path[0])+len(searcher2.path[1])))
pp.plotMap(map_object2,searcher2.path)

searcher3 = BFSearch()
searcher3.search(map_object3, start, goal)
print("\nBFS")
print("Number of visited nodes: {}".format(searcher3.searchedNodes))
print("Length of path: {}".format(len(searcher3.path[0])+len(searcher3.path[1])))
pp.plotMap(map_object3,searcher3.path)



#pp.plotMap(map_object2,searcher2.path)