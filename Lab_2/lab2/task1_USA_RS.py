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

# map_object = pp.generateMap2d([60,60])
# plt.clf()
# plt.imshow(map_object)
# #print(map_object)
# plt.show()

class RandomSearch():
    def __init__(self):
        self.moving_cost = 1
        self.frontier = PriorityQueue()        

    def search(self, theMap, start, goal):
        
        def _get_neighbors(current, theMap):
            xCords = current.pos[0]
            yCords = current.pos[1]

            neighbours = []

            ###########################
            #                         #
            #         [58,21]         #
            # [57,22] [58,22] [59,22] #
            #         [58,23]         #
            #                         #
            ###########################
            
            # Gets the neighbours to current, if the node is not a wall (-1) or already visited (1), and also a check if the value is in range
            for i in range(3):
                if theMap[xCords+(-1+i)][yCords] not in {-1,1} and (xCords+(-1+i) not in {-1,xCords,len(theMap[0])}):
                    neighbours.append(Node([xCords+(-1+i), yCords], current, _cost_function([xCords+(-1+i), yCords], goal)))
                if theMap[xCords][yCords+(-1+i)] not in {-1, 1} and (yCords+(-1+i) not in {-1, yCords, len(theMap[1])}):
                    neighbours.append(Node([xCords, yCords+(-1+i)], current, _cost_function([xCords, yCords+(-1+i)], goal)))

            return neighbours
        
        def _cost_function(theNodeCords, theGoal):
            return random.randint(1, 5)
            #return abs(theGoal.pos[0] - theNodeCords[0]) + abs(theGoal.pos[1] - theNodeCords[1])

        # add starting cell to open list
        self.frontier.add(start, 0)

        # path taken
        came_from = {}

        # expanded list with cost value for each cell
        cost = {}

        # init. starting node
        #start.parent = None
        #start.g = 0

        # if there is still nodes to open
        while not self.frontier.isEmpty():
            current = self.frontier.remove()

            # check if the goal is reached
            if current == goal:
                break

            # for each neighbour of the current cell
            # Implement get_neighbors function (return nodes to expand next)
            # (make sure you avoid repetitions!)
            for next in _get_neighbors(current, theMap):

                # compute cost to reach next cell
                # Implement cost function
                #cost = _cost_function(current, next)

                # add next cell to open list
                self.frontier.add(next, cost)
                # add to path
                #came_from[next] = current

        return came_from, cost



if __name__ == "__main__":
        
    # map_object, info = pp.generateMap2d([60,60])
    map_object = pp.generateMap2d([60, 60])
    plt.clf()
    plt.imshow(map_object)


    example_solved_map = map_object

    # x_corr, y_corr = range(30),  range(30)[::-1]
    # example_solved_path = [x_corr, y_corr]

    # pp.plotMap(example_solved_map,example_solved_path)
    # plt.clf()
    # plt.imshow(map_object)
    # plt.show()

    start = Node([np.where(map_object == -2)[0][0], np.where(map_object == -2)[1][0]], None, 0)
    goal = Node([np.where(map_object == -3)[0][0], np.where(map_object == -3)[1][0]], None, 0)

    searcher = RandomSearch()
    searcher.search(map_object, start, goal)
