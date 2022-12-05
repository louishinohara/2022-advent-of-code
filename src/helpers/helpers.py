from functools import reduce

# Get's puzzle input and convert to list
def getPuzzleInput(path):
    file = open(path, 'r')
    lines = file.readlines()
    return lines

def reduceFunc(data):
    return reduce(lambda a, b: a+b, data)

def printSolution(res):
    res1, res2 = res
    print(f'--- Answer To Part 1 --- \n {res1} \n')
    print(f'--- Answer To Part 2 --- \n {res2} \n')