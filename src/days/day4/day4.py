from src.constants import BASEPATH
from functools import reduce
from src.helpers.helpers import getPuzzleInput, reduceFunc

def exec():
    currPath = BASEPATH + "/day4/input.txt"
    data = [i.rstrip().split(',') for i in getPuzzleInput(currPath)]
    res1, res2 = part1(data), part2(data)
    printSolution((res1, res2))

def part1(data):
    mapVal = map(mapFunc1, data)
    res = reduce(lambda a, b: a+b, mapVal)
    return res

def part2(data):
    mapVal = map(mapFunc2, data)
    res = reduce(lambda a, b: a+b, mapVal)
    return res

def mapFunc1(input):
    xSet, ySet = createSetData(input)
    return 1 if xSet.issubset(ySet) or ySet.issubset(xSet) else 0

def mapFunc2(input):
    xSet, ySet = createSetData(input)
    return 1 if not xSet.isdisjoint(ySet) else 0

def createSetData(input):
    x, y = input[0], input[1]
    x1, x2 = x.split('-')
    y1, y2 = y.split('-')
    xSet = set([i for i in range(int(x1), int(x2)+1)])
    ySet = set([i for i in range(int(y1), int(y2)+1)])
    return xSet, ySet

def printSolution(res):
    res1, res2 = res
    print(f'--- Answer To Part 1 --- \n {res1} \n')
    print(f'--- Answer To Part 2 --- \n {res2} \n')