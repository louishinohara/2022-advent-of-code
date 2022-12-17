class Head:
    def __init__(self) -> None:
        self.x, self.y = 0, 0
        self.prevX, self.prevY = 0, 0

    def updateX(self, x):
        self._setPrevCoord()
        self.x += x

    def updateY(self, y):
        self._setPrevCoord()
        self.y += y

    def getCoord(self):
        return (self.x, self.y)

    def _setPrevCoord(self):
        self.prevX, self.prevY = self.x, self.y 

    def getPrevCoord(self):
        return (self.prevX, self.prevY)