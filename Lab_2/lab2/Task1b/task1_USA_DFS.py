import path_planning as pp
import matplotlib.pyplot as plt
from PriorityQueue import PriorityQueue
import numpy as np
from node import Node
import random
"""
create maps with obstacles randomly distributed
cells with a value of 0: Free cell; 
                     -1: Obstacle;
                     -2: Start point;
                     -3: Goal point;
"""

class DFSearch():
    def __init__(self):
        self.queue = PriorityQueue()
        self.path = [[],[]]
        self.searchedNodes = 0

    def search(self, theMap, start, goal):
        
        def _get_neighbors(current, theMap):
            xCords = current.pos[0]
            yCords = current.pos[1]

            neighbors = []

            ###########################
            #                         #
            #         [58,21]         #
            # [57,22] [58,22] [59,22] #
            #         [58,23]         #
            #                         #
            ###########################

            # Gets the neighbors to current, if the node is not a wall (-1) or if the node has not been visited, and also a check if the value is in range
            for i in range(3):
                if (xCords+(-1+i) not in {-1,xCords,len(theMap[0])}):
                    nodeCost = _cost_function()
                    newNode = Node([xCords+(-1+i), yCords], current, nodeCost, current.depth+1)

                    if theMap[xCords+(-1+i)][yCords] in {0, -3}:
                        neighbors.append(newNode) 

                if (yCords+(-1+i) not in {-1, yCords, len(theMap[1])}):
                    nodeCost = _cost_function()
                    newNode = Node([xCords, yCords+(-1+i)], current, nodeCost, current.depth+1)

                    if theMap[xCords][yCords+(-1+i)] in {0, -3}:
                        neighbors.append(newNode)

            return neighbors
        
        def _cost_function():
            return 1

        def _calc_path(theStart, theGoal):
            thePath = [[],[]]
            theNode = theGoal
            while theNode.pos != theStart.pos:
                thePath[1].append(theNode.pos[0])
                thePath[0].append(theNode.pos[1])
                theNode = theNode.parent
            return thePath

        # add starting cell to open list
        self.queue.add(start)

        # if there is still nodes to open
        while not self.queue.isEmpty():
            current = self.queue.pop()

            # check if the goal is reached
            if current.pos == goal.pos:
                goal.parent = current
                self.path = _calc_path(start, goal)
                break

            for next in _get_neighbors(current, theMap):

                if theMap[next.pos[0]][next.pos[1]] == 0:
                    theMap[next.pos[0]][next.pos[1]] = next.depth

                self.searchedNodes += 1
                self.queue.add(next)

        return self.path



if __name__ == "__main__":
        
    # map_object, info = pp.generateMap2d([60,60])
    map_object = pp.generateMap2d([100, 100])

    start = Node([np.where(map_object == -2)[0][0], np.where(map_object == -2)[1][0]], None, 0, 0)
    goal = Node([np.where(map_object == -3)[0][0], np.where(map_object == -3)[1][0]], None, 0, 0)

    searcher = DFSearch()
    searcher.search(map_object, start, goal)
    print("Number of visited nodes: {}".format(searcher.searchedNodes))
    print("Length of path: {}".format(len(searcher.path[0])+len(searcher.path[1])))
    pp.plotMap(map_object,searcher.path)
    