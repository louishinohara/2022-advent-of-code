class Command:
    COMMAND_INDEX, VAL_INDEX = 0, 1

    def __init__(self, c) -> None:
        self.command, self.cycle, self.value = self._parseCommand(c)

    def _parseCommand(self, c):
        res = c.rstrip().split(' ')
        command, cycle, value = res[self.COMMAND_INDEX], None, None 
        cycle = 2 if command == 'addx' else 1
        value = int(res[self.VAL_INDEX]) if command == 'addx' else None
        return command, cycle, value

    def isNoop(self):
        return self.command == 'noop'
    
    def getCycle(self):
        return self.cycle

    def decrementCycle(self):
        self.cycle -= 1

    def isElligible(self):
        return self.cycle == 0 

    def getVal(self):
        return self.value

    def getVals(self):
        return self.command, self.cycle, self.value