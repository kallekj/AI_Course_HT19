class PriorityQueue:
    def __init__(self):
        self.elements = []
    def isEmpty(self):
        return len(self.elements) == 0
    def add(self, item):
        self.elements.append(item)
        self.elements.sort(key=lambda item: item.cost)
    def remove(self):
        theItem = self.elements[0]
        self.elements.remove(theItem)
        return theItem