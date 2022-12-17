class Head:
    def __init__(self) -> None:
        self.x, self.y = 0, 0
    
    def updateX(self, x):
        self.x += x

    def updateY(self, y):
        self.y += y

    def getCoord(self):
        return (self.x, self.y)