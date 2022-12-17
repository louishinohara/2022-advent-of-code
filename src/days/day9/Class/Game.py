from matplotlib import pyplot as plt

class Game:
    def __init__(self, head, tail) -> None:
        self.head, self.tail = head, tail
    
    def exec(self, c):
        coord = self._parseCoord(c)
        print("Coord is {0}".format(coord))
        x, y = self._decodeCoord(coord)
        self.move(x, y)
        print('------------')

    # def showPlot(self):
    #     x1, y1 = self.head.getCoord()
    #     x2, y2 = self.tail.getCoord()

    #     plt.plot([x1, x2], [y1, y2], 'ro')
    #     plt.show()

    def _parseCoord(self, c):
        DIR_INDEX, STEPS_INDEX = 0, 1
        coord = c.split(' ')
        dir, steps = coord[DIR_INDEX], coord[STEPS_INDEX]
        return (dir, int(steps)) 

    def _decodeCoord(self, coord):
        dir, steps = coord
        d = { 'U': (0,1), 'D': (0,-1),
              'L': (-1,0), 'R': (1,0) }
        x, y = tuple([steps*x for x in d[dir]])
        return x, y

    def move(self, x, y):
        print("COORDS ARE X:" + str(x) + " Y:" + str(y))

        for i in range(abs(x)):
            self.head.updateX(1 * self._checkPositive(x))
            self.tail.updateCoord(self.head)

        for j in range(abs(y)): 
            print(j)
            self.head.updateY(1 * self._checkPositive(y))
            self.tail.updateCoord(self.head)

        print("=== NEW ===")
        print("HEAD: {0}".format(self.head.getCoord()))
        print("TAIL: {0}".format(self.tail.getCoord()))
        print("================")

    def moveTail(self, x, y):
        self.tail.updateCoord(self.head)

    def _checkPositive(self, val):
        if val > 0: return 1 
        else: return -1
    
    def getTail(self):
        return self.tail