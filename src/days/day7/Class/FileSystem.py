from src.days.day7.Class.Dir import Dir
from src.days.day7.Class.File import File
from src.days.day7.Class.Command import Command

class FileSystem:
    def __init__(self):
        self.fs = Dir(None, '/')

    def getFS(self):
        return self.fs

    def buildFileSystem(self, data):
        self._createFileSystem(data)
        self._calculateDirSize()

    def _createFileSystem(self, data):
        index, fs = 1, self.fs
        while index <= len(data) - 1:
            input = data[index]
            command = self._parseInput(input)
            index, fs = command.execute(index, data, fs)

    def _parseInput(self, input):
        OPTION_KEY = 0
        parsedInput = input.rstrip().split(' ')
        option, output = parsedInput[OPTION_KEY], None

        if option == '$': output = Command(parsedInput)
        elif option == 'dir': output = Dir(self.fs, option)
        else: output = File(option)
        return output

    # Get dir of top dir. Then recursively calculate dirs    
    def _calculateDirSize(self):
        self.fs.getTotalDirSize()
        def helper(fs):
            for item in fs.values():
                if isinstance(item, Dir):
                    item.getTotalDirSize()
                    helper(item.getFiles())
        helper(self.fs.getFiles())

    # Get total dir size where that dir is less than 100000
    def getElligibleDirsToDelete(self):
        def helper(fs, accum): 
            total = 0
            for item in fs.values():
                if isinstance(item, Dir):
                    dirSize = item.getDirSize()
                    if dirSize < 100000: total += dirSize
                    total += helper(item.getFiles(), accum)
            return accum + total
        return helper(self.fs.getFiles(), 0) 

    # Find dir that fits criteria and delete
    def getExactDirToDelete(self):
        maxDirSize, dirSizeRequired, currDirSize, candidate = 70000000, 30000000, self.fs.getDirSize(), float('inf')
        unusedSpace = maxDirSize - currDirSize
        amtToFree = dirSizeRequired - unusedSpace
        def helper(fs):
            nonlocal candidate
            for item in fs.values():
                if isinstance(item, Dir):
                    dirSize = item.getDirSize()
                    if dirSize > amtToFree: candidate = min(dirSize, candidate)
                    helper(item.getFiles())
        helper(self.fs.getFiles())
        return candidate 

    def _printFS(self, fs, depth):
        for k, v in fs.items():
            if isinstance(v, Dir):
                print('---' * depth, depth, k, v.getDirSize())
                self._printFS(v.getFiles(), depth + 1)
            else:
                print('---' * depth, depth, k, v)
    