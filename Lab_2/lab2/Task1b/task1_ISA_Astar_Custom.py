import path_planning as pp
import matplotlib.pyplot as plt
from PriorityQueue import PriorityQueue
import numpy as np
from node import Node
import math
import random
"""
create maps with obstacles randomly distributed
cells with a value of 0: Free cell; 
                     -1: Obstacle;
                     -2: Start point;
                     -3: Goal point;
"""

class AstarC():
    def __init__(self):
        self.queue = PriorityQueue()
        self.path = [[],[]]
        self.searchedNodes = 0

    def search(self, theMap, start, goal, objInfo):
        
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
                    newNode = Node([xCords+(-1+i), yCords], current, 0, current.depth+1)
                    nodeCost = _cost_function("euclidean", newNode, goal, objInfo)
                    newNode.set_cost(nodeCost)

                    if theMap[xCords+(-1+i)][yCords] > nodeCost or theMap[xCords+(-1+i)][yCords] in {0, -3}:
                        neighbors.append(newNode) 

                if (yCords+(-1+i) not in {-1, yCords, len(theMap[1])}):
                    newNode = Node([xCords, yCords+(-1+i)], current, 0, current.depth+1)
                    nodeCost = _cost_function("euclidean", newNode, goal, objInfo)
                    newNode.set_cost(nodeCost)

                    if theMap[xCords][yCords+(-1+i)] > nodeCost or theMap[xCords][yCords+(-1+i)] in {0, -3}:
                        neighbors.append(newNode) 


            return neighbors
        
        # Will increase the cost of a node if the node is within the "obstacle area" otherwise return 0
        def _weight_func(theNode, objInfo):
            obj_upper_y, obj_lower_y, obj_x = objInfo
            weight = 0
            if(theNode.pos[0] < obj_upper_y and theNode.pos[0] > obj_lower_y):
                if(theNode.pos[1] < obj_x):
                    weight = (obj_x - theNode.pos[1]) * 100
            return weight

        def _cost_function(func, theNode, theGoal, objInfo):
            if func == "manhattan":
                if theNode.pos[1] > theNode.parent.pos[1]:
                    extraCost = _weight_func(theNode, objInfo)
                    return abs(theGoal.pos[0] - theNode.pos[0]) + abs(theGoal.pos[1] - theNode.pos[1]) + theNode.depth + extraCost
                else:    
                    return abs(theGoal.pos[0] - theNode.pos[0]) + abs(theGoal.pos[1] - theNode.pos[1]) + theNode.depth
            elif func == "euclidean":
                if theNode.pos[1] > theNode.parent.pos[1]:
                    extraCost = _weight_func(theNode, objInfo)
                    return math.sqrt(pow(theGoal.pos[0] - theNode.pos[0],2) + pow(theGoal.pos[1] - theNode.pos[1], 2)) + theNode.depth + extraCost
                else:
                    return math.sqrt(pow(theGoal.pos[0] - theNode.pos[0],2) + pow(theGoal.pos[1] - theNode.pos[1], 2)) + theNode.depth
            else:
                return 1


        # def _weight_func(theNodeCords, objInfo, theMap):
        #     obj_upper_y, obj_lower_y, obj_x = objInfo
        #     weightY = 0
        #     weightX = 0
        #     # lagg till sa att bedommer vikten pa om malet ar pa ovre eller nedre halvan ocksa
        #     if(theNodeCords[0] <= obj_upper_y and theNodeCords[0] >= obj_lower_y):
        #         # normX = _norm(theNodeCords[1], 0, obj_right_x, 0, 100) # lower vals are more to left, higher vals are closer to object
        #         # normLowY = _norm(theNodeCords[0], obj_lower_y, len(theMap[1])/2, 0, 100)
        #         # normUpperY = _norm(theNodeCords[0], obj_upper_y, len(theMap[1])/2, 0, 100)
        #         if theNodeCords[1] < obj_x:
        #             weightX = _norm(theNodeCords[1], 0, obj_x) * 10
        #             if(theNodeCords[0] < len(theMap[0])/2):
        #                 weightY = _norm(theNodeCords[0], obj_lower_y, len(theMap[1])/2)
        #             else:
        #                 weightY = _norm(theNodeCords[0], len(theMap[1])/2, obj_upper_y)
        #     return (weightX + weightY) * 10

        
        # def _weight_func(theNodeCords, objInfo, theMap, theGoal):
        #     obj_upper_y, obj_lower_y, obj_x = objInfo
        #     weightY = 0
        #     weightX = 0
        #     # lagg till sa att bedommer vikten pa om malet ar pa ovre eller nedre halvan ocksa
        #     if(theNodeCords[0] <= obj_upper_y and theNodeCords[0] >= obj_lower_y and theNodeCords[1] < obj_x):
        #         # normX = _norm(theNodeCords[1], 0, obj_right_x, 0, 100) # lower vals are more to left, higher vals are closer to object
        #         # normLowY = _norm(theNodeCords[0], obj_lower_y, len(theMap[1])/2, 0, 100)
        #         # normUpperY = _norm(theNodeCords[0], obj_upper_y, len(theMap[1])/2, 0, 100)
        #         weightX = _norm(theNodeCords[1], 0, obj_x) * 10
        #         if(theNodeCords[0] < len(theMap[0])/2 and theGoal.pos[0] < len(theMap[0])/2):
        #             weightY = _norm(theNodeCords[0], obj_lower_y, len(theMap[1])/2)
        #         else:
        #             weightY = _norm(theNodeCords[0], len(theMap[1])/2, obj_upper_y)
    
    
        #     return (weightX + weightY) * 100


        # def _norm(value, in_min, in_max, out_min, out_max):
        #     return (value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

        def _norm(value, in_min, in_max):
            return (value - in_min) / (in_max - in_min) 


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
            current = self.queue.remove()

            # check if the goal is reached
            if current.pos == goal.pos:
                goal.parent = current
                self.path = _calc_path(start, goal)
                break

            for next in _get_neighbors(current, theMap):

                if theMap[next.pos[0]][next.pos[1]] >= 0:
                    theMap[next.pos[0]][next.pos[1]] = next.depth

                self.searchedNodes += 1
                self.queue.sort_add(next)

        return self.path



if __name__ == "__main__":

    # map_object, info = pp.generateMap2d([60,60])
    map_object, info = pp.generateMap2d_obstacle([60, 60])
    print(info)
    start = Node([np.where(map_object == -2)[0][0], np.where(map_object == -2)[1][0]], None, 0, 0)
    goal = Node([np.where(map_object == -3)[0][0], np.where(map_object == -3)[1][0]], None, 0, 0)

    print("Start node is: {}".format(start.pos))
    print("Goal node is at: {}".format(goal.pos))

    searcher = AstarC()
    searcher.search(map_object, start, goal, info)
    print("Number of visited nodes: {}".format(searcher.searchedNodes))
    print("Length of path: {}".format(len(searcher.path[0])+len(searcher.path[1])))
    pp.plotMap(map_object,searcher.path)