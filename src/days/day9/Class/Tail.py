class Tail:
    def __init__(self) -> None:
        self.x, self.y = 0, 0
        self.visited = set()

    def updateCoord(self, head):
        x, y = head.getCoord()
        self._updateCoord(x, y, head)
        self.updateVisited()

    def updateVisited(self):
        self.visited.add(tuple((self.x, self.y)))

    def getVisited(self):
        return self.visited

    def _updateCoord(self, x, y, head):
        ABS_DIFF_X, ABS_DIFF_Y = self._getAbsDiff(x, self.x), self._getAbsDiff(self.y, y)
        HEAD_TAIL_SAME_LOCATION = self.x == x and self.y == y
        HEAD_TAIL_DIAGONAL = ABS_DIFF_X == 1 and ABS_DIFF_Y == 1
        HEAD_TAIL_ONE_HOP_AWAY_SAME_AXIS = ABS_DIFF_X + ABS_DIFF_Y < 2
        
        print("X: {0} Y:{1}".format(ABS_DIFF_X, ABS_DIFF_Y))
        if HEAD_TAIL_SAME_LOCATION or HEAD_TAIL_DIAGONAL or HEAD_TAIL_ONE_HOP_AWAY_SAME_AXIS: 
            print("1 Hop Away Head({0},{1}) Tail({2},{3})".format(x, y, self.x, self.y))
            return
        else:
            prevX, prevY = head.getPrevCoord()
            print("Adjust Both Values Head({0},{1}) Tail({2},{3}) New Tail({4},{5})".format(x, y, self.x, self.y, prevX, prevY))
            self.x, self.y = head.getPrevCoord()

                
    def _getAbsDiff(self, a, b):
        return abs(abs(a)-(abs(b)))

    def getCoord(self):
        return (self.x, self.y)

    def _checkPositive(self, val):
        if val > 0: return 1 
        elif val < 0: return -1
        else: return None

