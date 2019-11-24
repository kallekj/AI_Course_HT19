import path_planning as pp
import matplotlib.pyplot as plt
from search_algorithm import PriorityQueue
import numpy as np
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

    def search(self, map, start, goal):
        
        def get_neighbors(current):
            xCords = current
            
            pass 
        
        def cost_function(current, next):
            return 1

        # add starting cell to open list
        self.frontier.add(start, 0)

        # path taken
        came_from = {}

        # expanded list with cost value for each cell
        cost = {}

        # init. starting node
        start.parent = None
        start.g = 0

        # if there is still nodes to open
        while not self.frontier.isEmpty():
            current = self.frontier.remove()

            # check if the goal is reached
            if current == goal:
                break

            # for each neighbour of the current cell
            # Implement get_neighbors function (return nodes to expand next)
            # (make sure you avoid repetitions!)
            for next in get_neighbors(current):

                # compute cost to reach next cell
                # Implement cost function
                cost = cost_function(current, next)

                # add next cell to open list
                self.frontier.add(next, cost)
                # add to path
                came_from[next] = current

        return came_from, cost

if __name__ == "__main__":
        
    map_object, info = pp.generateMap2d([60,60])
    plt.clf()
    plt.imshow(map_object)

    print(info["start"])
    print(info["goal"])
    start = [info["start"]["x"], info["start"]["y"]]
    goal = [info["goal"]["x"], info["goal"]["y"]]

    searcher = RandomSearch()
    searcher.search(map_object, start, goal)