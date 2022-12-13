from src.days.day7.Class.Dir import Dir
from src.days.day7.Class.File import File

class LS:
    def __init__(self) -> None:
        pass

    def execute(self, data, index, fs):
        index += 1
        while index < len(data):
            input = data[index].rstrip().split(' ')
            command = input[0]
            if command  == '$': break   # Do stuff till we see a command
            elif command == 'dir':
                self._addDirToFS(fs, input)
            else:
                self._addFileToFS(fs, input)
            index += 1
        return index, fs

    def _addDirToFS(self, fs, input):
        NAME_INDEX = 1
        dirName = input[NAME_INDEX]
        dir = Dir(fs, dirName)
        self._addToFs(fs, dirName, dir)

    def _addFileToFS(self, fs, input):
        SIZE_INDEX, NAME_INDEX = 0, 1
        fileSize, fileName = int(input[SIZE_INDEX]), input[NAME_INDEX]
        file = File(fileName, fileSize)
        self._addToFs(fs, fileName, file)

    def _addToFs(self, fs, key, val):
        fs.setFiles(key, val)