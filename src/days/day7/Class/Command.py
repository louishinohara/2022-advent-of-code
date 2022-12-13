from src.days.day7.Class.Commands.CD import CD
from src.days.day7.Class.Commands.LS import LS

class Command:
    def __init__(self, input):
        self.commandName = self._parseInput(input)

    def _addToFs(self, fs, key, val):
        fs.setFiles(key, val)

    def execute(self, index, data, fs):
        newIndex, updatedFS = None, None
        if isinstance(self.commandName, LS): newIndex, updatedFS = self._executeLSCommand(data, index, fs)
        elif isinstance(self.commandName, CD): newIndex, updatedFS = self._executeCDCommand(data, index, fs)
        return newIndex, updatedFS

    def _executeLSCommand(self, data, index, fs):
        return self.commandName.execute(data, index, fs)   

    def _executeCDCommand(self, data, index, fs):
        COMMAND_INDEX = 2
        command = data[index].strip().split(' ')[COMMAND_INDEX]
        return index + 1, self.commandName.execute(command, fs)       

    def getClassName(self):
        return self.__class__.__name__
        
    def _parseInput(self, input):
        COMMAND_KEY = 1
        d = {'ls': LS, 'cd': CD}
        return d[input[COMMAND_KEY]]()


