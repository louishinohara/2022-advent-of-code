class Clock:
    UPPER_LIMIT = 40
    def __init__(self) -> None:
        self.x, self.cycle = 1, 0
        self.queue = []
        self.history = {20: None, 60: None, 100: None, 140: None, 180: None, 220: None}
        self.spritePos = self._getSpritePosiiton()
        self.spriteDrawing = []

    def exec(self):
        while True:
            self._up()
            self._down()
            if not self.queue: break

    def load(self, data):
        self.queue = data

    def _incrementClock(self):
        self.cycle += 1
    
    def _up(self):
        self._getSpritePosiiton()
        self._drawSprite()
        self._incrementClock()
        self._recordInHistory()

    def _down(self):
        if self.queue:
            c = self.queue[0]
            c.decrementCycle()
            if c.isElligible():
                if not c.isNoop(): self.x += c.getVal()
                del self.queue[0]

    def _recordInHistory(self):
        if self.cycle in self.history: self.history[self.cycle] = self.x

    def _drawSprite(self):
        pixel = '.'
        head, tail = self.spritePos
        if self.cycle % self.UPPER_LIMIT in [i for i in range(head, tail + 1)]: pixel = '#'
        self.spriteDrawing.append(pixel)

    def _getSpritePosiiton(self):
        self.spritePos = (self.x-1, self.x+1)

    def getResults(self):
        return sum([k * v for k, v in self.history.items()])

    def getDrawing(self):
        return [ ''.join(self.spriteDrawing[i:i+self.UPPER_LIMIT]) 
                    for i in range(0, len(self.spriteDrawing), self.UPPER_LIMIT) ]