from functools import reduce

class Node:
    def __init__(self, val) -> None:
        self.val = int(val)
        self.isVisible = False 
        self.nodeMap = { 'up': None, 'down': None,
                         'left': None, 'right': None }

    def __str__(self):
        return str(self.val)

    def exec(self):
        res = [1 if self.findVisibility(dir, self.val, True) else 0 for dir in self.nodeMap.keys()]
        return max(res)

    def findVisibility(self, direction, target, res):
        node = self.nodeMap[direction]
        return res if not node else False if node.getVal() >= target else node.findVisibility(direction, target, True) 

    def getScenicScore(self):
        res = [ self.findScenicDistance(dir, self.val, 0) for dir in self.nodeMap.keys() ]
        return reduce((lambda x, y: x * y), res)

    def findScenicDistance(self, direction, target, accum):
        node = self.nodeMap[direction]
        return accum if not node else accum + 1 if node.getVal() >= target else node.findScenicDistance(direction, target, accum + 1)

    def getNodes(self):
        return self.nodeMap

    def getVal(self):
        return self.val

    def setNodes(self, up, down, left, right):
        self.nodeMap['up'], self.nodeMap['down'] = up, down 
        self.nodeMap['left'], self.nodeMap['right'] = left, right