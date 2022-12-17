from src.constants import BASEPATH
from src.days.day9.Class.Game import Game
from src.days.day9.Class.Head import Head
from src.days.day9.Class.Tail import Tail
from src.helpers.helpers import getPuzzleInput, printSolution


def exec():
    currPath = BASEPATH + "/day9/input.txt"
    data = getPuzzleInput(currPath)
    tail = playGame(data)
    res = getVisited(tail)
    print(res)
    
def playGame(coords):
    head, tail = Head(), Tail()
    game = Game(head, tail)
    for c in coords: game.exec(c)
    return game.getTail()

def getVisited(tail):
    # l = list(tail.getVisited())
    # l.sort()
    # print(l)
    return len(tail.getVisited())


# 6352 Is Wrong