class Clock:
    def __init__(self) -> None:
        self.x, self.cycle = 1, 0
        self.queue = []
        self.history = {20: None, 60: None, 100: None, 140: None, 180: None, 220: None}

    def _incrementClock(self):
        self.cycle += 1
    
    def _up(self):
        self._incrementClock()
        self._recordInHistory()

    def _recordInHistory(self):
        if self.cycle in self.history:
            self.history[self.cycle] = self.x

    def _down(self):
        if self.queue:
            c = self.queue[0]
            c.decrementCycle()
            if c.isElligible():
                if not c.isNoop(): self.x += c.getVal()
                del self.queue[0]
            return 1
        else:
            return -1

    def load(self, data):
        self.queue = data
        
    def exec(self):
        self._up()
        return self._down()

    def printVals(self):
        return (self.cycle, self.x)

    def getSum(self):
        print(self.history)
        return sum([k * v for k, v in self.history.items()])