class Tail:
    def __init__(self) -> None:
        self.x, self.y = 0, 0
        self.visited = {}

    def updateCoord(self, head):
        x, y = head.getCoord()
        print("Current coord of head is {0}".format(head.getCoord()))
        self._updateX(x)
        self._updateY(y)

    def _updateX(self, x):
        print("Calculation for updateX is {0}".format(abs((abs(self.x) - abs(x)))))
        if self.x == x: return 
        elif abs((abs(self.x) - abs(x))) == 1: return 
        elif abs(abs(self.x) - abs(x)) == 2: self.x += (1 * self._checkPositive(x))

    def _updateY(self, y):
        print("Calculation for updateY is {0}".format(abs((abs(self.y) - abs(y)))))
        # print("Y: {0} and current tail coords are {1}".format(y, self.getCoord()))
        if self.y == y: return
        elif abs(abs(self.y) - abs(y)) == 1: return 
        elif abs(abs(self.y) - abs(y)) == 2: self.y += (1 * self._checkPositive(y))

    def getCoord(self):
        return (self.x, self.y)

    def _checkPositive(self, val):
        if val > 0: return 1 
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