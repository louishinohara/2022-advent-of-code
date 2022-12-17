from src.constants import BASEPATH
from src.days.day9.Class.Game import Game
from src.days.day9.Class.Head import Head
from src.days.day9.Class.Tail import Tail
from src.helpers.helpers import getPuzzleInput, printSolution

def exec():
    currPath = BASEPATH + "/day9/input.txt"
    data = getPuzzleInput(currPath)
    playGame(data)

def playGame(coords):
    head, tail = Head(), Tail()
    game = Game(head, tail)
    counter = 0
    for c in coords:
        game.exec(c)
        counter += 1
        if counter == 10:
            break