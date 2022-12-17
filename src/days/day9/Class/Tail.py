class Tail:
    def __init__(self) -> None:
        self.x, self.y = 0, 0
        self.visited = [[0 for i in range(1000)] for i in range(1000)]

    def updateCoord(self, head):
        x, y = head.getCoord()
        self._updateCoord(x, y, head)
        self.updateVisited()

    def updateVisited(self):
        self.visited[self.x][self.y] += 1

    def getVisited(self):
        return self.visited

    def _updateCoord(self, x, y, head):
        print("X: {0} Y:{1}".format(self._getAbsDiff(self.x, x), self._getAbsDiff(self.y, y)))
        if self.x == x and self.y == y: 
            print("Nothing to do here")
            return # Same spot no need to move
        elif self._getAbsDiff(x, self.x) + self._getAbsDiff(self.y, y) < 2 or (self._getAbsDiff(x, self.x) == 1 and self._getAbsDiff(self.y, y) == 1): 
            print("Within a hop head ({0},{1}) tail ({2},{3})".format(x, y, self.x, self.y))
            return # Within 1 hop away
        else:
            prevX, prevY = head.getPrevCoord()
            print("Adjust Both Values Head({0},{1}) Tail({2},{3}) New Tail({4},{5})".format(x, y, self.x, self.y, prevX, prevY))
            self.x = prevX
            self.y = prevY
            # if self._getAbsDiff(self.x, x) == 2 and self._getAbsDiff(self.y, y) == 0: self.x += (1 * self._checkPositive(x))
            # elif self._getAbsDiff(self.x, x) == 0 and self._getAbsDiff(self.y, y) == 2: self.y += (1 * self._checkPositive(y))
            # else:
            #     print("Updating both coords. x: {0} y:{1}".format(self._getAbsDiff(self.x, x), self._getAbsDiff(self.y, y)))
            #     # print(x,y)
            #     # print(self.x, self._checkPositive(x), self.y, self._checkPositive(y))
            #     self.x = prevX
            #     self.y = prevY
            #     # print(self.x, self.y)
                
    def _getAbsDiff(self, a, b):
        return abs(abs(a)-(abs(b)))

    def getCoord(self):
        return (self.x, self.y)

    def _checkPositive(self, val):
        if val >= 0: return 1 
        else: return -1

# (0,0) -> (0,0)    // Fine 
# (0,0) -> (0,1)    // Do Nothing
# (0,0) -> (1,1)    // Move Diagonal
# (0,0) -> (0,2)   // Move 1
# (1,1) -> (2,3)    // 3 - 1, 2 - 1 = 2, 1 So move to (2,2)
# (-1,-1) -> (-2,-3)
# (-1, 1) -> (-2, 3)
# Y is == 2. 


# To catch up, substract head from tail. Add to both coord 