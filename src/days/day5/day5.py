from src.constants import BASEPATH
from src.helpers.helpers import getPuzzleInput, printSolution


def exec():
    currPath = BASEPATH + "/day5/input.txt"
    data = [i for i in getPuzzleInput(currPath)]
    instructions = getInstructions(data)
    res1, res2 = part1(instructions), part2(instructions)
    printSolution((res1, res2))

def part1(instructions):
    d = moveContainers(getBlocks(), instructions, reverse=True)
    return getTopItem(d)

def part2(instructions):
    d = moveContainers(getBlocks(), instructions, reverse=False)
    return getTopItem(d)

def getBlocks():
    d = {
        1: ['Z', 'P', 'M', 'H', 'R'],
        2: ['P', 'C', 'J', 'B'],
        3: ['S', 'N', 'H', 'G', 'L', 'C', 'D'],
        4: ['F', 'T', 'M', 'D', 'Q', 'S', 'R', 'L'],
        5: ['F', 'S', 'P', 'Q', 'B', 'T', 'Z', 'M'],
        6: ['T', 'F', 'S', 'Z', 'B', 'G'],
        7: ['N', 'R', 'V'],
        8: ['P', 'G', 'L', 'T', 'D', 'V', 'C', 'M'],
        9: ['W', 'Q', 'N', 'J', 'F', 'M', 'L']
    }
    return d


def getInstructions(data):
    return [ {  'count': int(i.rstrip().split(' ')[1]), 
                'src': int(i.rstrip().split(' ')[3]), 
                'dest': int(i.rstrip().split(' ')[5]) 
             }  for i in data ]


def moveContainers(blocks, instructions, reverse):
    for i in instructions:
        count, src, dest = i['count'], i['src'], i['dest']
        blocksToCopy = blocks[src][len(blocks[src]) - count:]
        del blocks[src][len(blocks[src]) - count:]
        if reverse: blocksToCopy.reverse()
        blocks[dest] += blocksToCopy
    return blocks


def getTopItem(data):
    return ''.join([data[i].pop() for i in sorted(data.keys())])
