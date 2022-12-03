from src.days.day2.Outcome.Outcome import Outcome
from src.constants import BASEPATH
from src.days.day2.Class.hand.Hand import Hand
from src.days.day2.Class.game.Game import Game
from src.days.day2.Class.game.ModifiedGame import ModifiedGame
from src.helpers.helpers import getPuzzleInput

def exec():
    currPath = BASEPATH + "/day2/input.txt"
    data = getPuzzleInput(currPath)
    res1 = game1(data)
    res2 = game2(data)
    printSolution(res1, res2)

def game1(data):
    game = Game()
    count = 0
    OPPONENT_INDEX, ME_INDEX = 0, 1
    for item in data:
        d = item.rstrip().split()
        opponent, me = Hand(d[OPPONENT_INDEX]), Hand(d[ME_INDEX])
        count += game.playGame(opponent.getOption(), me.getOption())
    return count 

def game2(data):
    game = ModifiedGame()
    count = 0
    OPPONENT_INDEX, ME_INDEX = 0, 1
    for item in data:
        d = item.rstrip().split()
        opponent, me = Hand(d[OPPONENT_INDEX]), Outcome(d[ME_INDEX])
        count += game.playGame(opponent.getOption(), me.getOption())
    return count 

def printSolution(res1, res2):
    print('--- Answer To Part 1 ---')
    print(res1)
    print()
    print('--- Answer To Part 2 ---')
    print(res2)
    print()