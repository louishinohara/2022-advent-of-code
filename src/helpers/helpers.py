# Get's puzzle input and convert to list
def getPuzzleInput(path):
    file = open(path, 'r')
    lines = file.readlines()
    return lines

def reduceFunc(data):
    return reduce(lambda a, b: a+b, data)