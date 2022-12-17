from src.constants import BASEPATH
from src.helpers.helpers import getPuzzleInput, printSolution
from src.days.day10.Class.Clock import Clock
from src.days.day10.Class.Command import Command
# Input 1 -> 4
# Input 2 -> 16480
# Input 3 -> 13140 
def exec():
    currPath = BASEPATH + "/day10/input2.txt"
    data = getPuzzleInput(currPath)
    parsedData = parseData(data)
    res = calculate(parsedData)
    print(res)
    
def parseData(data):
    return [Command(d) for d in data]

def calculate(data):
    clock = Clock()
    clock.load(data)
    keepGoing = True
    while keepGoing:
        res = clock.exec()
        if res == -1: break


    return clock.getSum()