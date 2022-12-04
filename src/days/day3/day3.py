from src.constants import BASEPATH
from src.helpers.helpers import getPuzzleInput, reduceFunc
from functools import reduce


def exec():
    currPath = BASEPATH + "/day3/input.txt"
    data = [i.rstrip() for i in getPuzzleInput(currPath)]
    res1, res2 = part1(data), part2(data)
    printSolution((res1, res2))


def part1(data):
    mapVal = map(mapFunc, data)
    res = reduceFunc(mapVal)
    return res


def part2(data):
    mapVal = scan(data)
    res = reduceFunc(mapVal)
    return res


def mapFunc(input):
    head, tail = input[:len(input)//2], input[len(input)//2:]
    match = comparisonAlgorithm(head, tail).pop()
    orderVal = getOrderVal(match)
    return orderVal


def scan(data):
    ans = []
    for i in range(0, len(data) - 2, 3):
        a, b, c = data[i], data[i + 1], data[i + 2]
        intersection = comparisonAlgorithm(comparisonAlgorithm(a, b), c).pop()
        ans.append(getOrderVal(intersection))
    return ans

def comparisonAlgorithm(a, b):
    return list(set(a).intersection(b))


def getOrderVal(c):
    UPPER_DIFF, LOWER_DIFF = 38, 96
    count = ord(c) - (UPPER_DIFF if c.isupper() else LOWER_DIFF)
    return count


def printSolution(res):
    res1, res2 = res
    print(f'--- Answer To Part 1 --- \n {res1} \n')
    print(f'--- Answer To Part 2 --- \n {res2} \n')
