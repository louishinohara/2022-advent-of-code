from src.constants import BASEPATH
from src.helpers.helpers import getPuzzleInput, printSolution


def exec():
    currPath = BASEPATH + "/day6/input.txt"
    data = [*getPuzzleInput(currPath)[0]]
    PART1STEP, PART2STEP = 4, 14
    res1, res2 = slidingWindow(data, PART1STEP), slidingWindow(data, PART2STEP)
    printSolution((res1, res2))

def slidingWindow(list, STEP):
    res = [(i + STEP) if len(set(list[i:i+STEP])) == STEP else None for i in range(0, len(list)-STEP)]
    return next(item for item in res if item is not None)