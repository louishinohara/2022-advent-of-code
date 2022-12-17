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
    res1, res2 = execClock(parsedData)
    print("Solution for part 1: {0} \n".format(res1))
    betterPrint(res2)
    
def parseData(data):
    return [Command(d) for d in data]

def execClock(data):
    clock = Clock()
    clock.load(data)
    clock.exec()
    return clock.getResults(), clock.getDrawing()

def betterPrint(res):
    print("Solution for part 2")
    for i in res: print(i)

###..#....####.####.#..#.#....###..###..
#..#.#....#....#....#..#.#....#..#.#..#.
#..#.#....###..###..#..#.#....#..#.###..
###..#....#....#....#..#.#....###..#..#.
#....#....#....#....#..#.#....#....#..#.
#....####.####.#.....##..####.#....###..

#PLEFULPB