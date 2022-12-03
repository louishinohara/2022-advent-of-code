from src.constants import BASEPATH
from src.helpers.helpers import getPuzzleInput

def exec():
    currPath = BASEPATH + "/day1/input.txt"
    data = getPuzzleInput(currPath)
    splitData = splitByNewLine(data)
    partitionedData = partitionData(splitData)
    printSolution(partitionedData)
    
# Remove new line from the chunks of data
def splitByNewLine(data):
    return [i if i == '\n' else i.rstrip() + ' ' for i in data ]

# Combine chunks of data into sublists in a list and find sum
def partitionData(data):
    removeNewLineAndJoin = ''.join(data).split("\n")
    partitionAndSum = [ sum([int(i) if i != '' else 0 for i in item.split(' ')]) for item in removeNewLineAndJoin ]
    partitionAndSum.sort()
    return partitionAndSum

def printSolution(data):
    print('--- Answer To Part 1 ---')
    maxVal = data[-1]
    print(maxVal)
    print()
    print('--- Answer To Part 2 ---')
    top3 = sum(data[-3:])
    print(top3)
