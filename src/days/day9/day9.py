from src.constants import BASEPATH
from src.days.day9.Class.Game import Game
from src.days.day9.Class.Head import Head
from src.days.day9.Class.Tail import Tail
from src.helpers.helpers import getPuzzleInput, printSolution
from itertools import chain


def exec():
    currPath = BASEPATH + "/day9/input2.txt"
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
    v = tail.getVisited()
    vList = list(chain.from_iterable(v))
    return sum([1 if i > 0 else 0 for i in vList ])