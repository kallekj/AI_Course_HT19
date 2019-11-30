class Node:
    def __init__(self, pos, parent, cost, depth):
        self.pos = pos
        self.parent = parent
        self.cost = cost
        self.depth = depth
    
    def set_parent(self, newParent):
        self.parent = newParent

    def set_cost(self, newCost):
        self.cost = newCost
