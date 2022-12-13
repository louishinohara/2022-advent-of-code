from src.constants import BASEPATH
from src.helpers.helpers import getPuzzleInput, printSolution
from src.days.day8.node import Node 
from itertools import chain

def exec():
    currPath = BASEPATH + "/day8/input.txt"
    data = [ list(map(Node, i.rstrip())) for i in getPuzzleInput(currPath)]
    paddedArr = padArr(data, 1, None)   # Give array a border
    assignNodes(paddedArr)              # Create graph by connecting nodes  
    arr = removePad(paddedArr)          # Remove padding from arr
    flatten_list = list(chain.from_iterable(arr))   # Remove 2D list. No need
    res1, res2 = findVisibleNodes(flatten_list), findScenicScore(flatten_list)  # Run algorithm on nodes
    printSolution((res1, res2))

def padArr(mat, padding, pad_with=0):
    n_rows, n_cols = len(mat), len(mat[0])

    # new empty matrix of the required size
    new_mat = [
        [pad_with for col in range(n_cols + padding * 2)]
        for row in range(n_rows + padding * 2)
    ]

    # "insert" original matix in the empty matrix
    for row in range(n_rows):
        for col in range(n_cols):
            new_mat[row + padding][col + padding] = mat[row][col]

    return new_mat

def removePad(data):
    return [i[1:-1] for i in data[1:-1]]

def assignNodes(data):
    for i in range(1, len(data) - 1):
        for j in range(1, len(data) - 1):
            node = data[i][j]
            up, down = data[i-1][j], data[i+1][j]
            left, right = data[i][j-1], data[i][j+1]
            node.setNodes(up, down, left, right)

def findVisibleNodes(nodes):
    return sum([node.exec() for node in nodes])

def findScenicScore(nodes):
    return max([node.getScenicScore() for node in nodes])