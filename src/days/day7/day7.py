from src.constants import BASEPATH
from src.helpers.helpers import getPuzzleInput, printSolution
from src.days.day7.Class.FileSystem import FileSystem

def exec():
    currPath = BASEPATH + "/day7/input.txt"
    data = getPuzzleInput(currPath)
    fs = FileSystem()
    fs.buildFileSystem(data)
    res1, res2 = fs.getElligibleDirsToDelete(), fs.getExactDirToDelete()
    printSolution((res1, res2))