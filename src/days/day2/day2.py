from src.days.day2.Outcome.Outcome import Outcome
from src.constants import BASEPATH
from src.days.day2.Class.hand.Hand import Hand
from src.days.day2.Class.game.Game import Game
from src.days.day2.Class.game.ModifiedGame import ModifiedGame
from src.helpers.helpers import getPuzzleInput

def exec():
    currPath = BASEPATH + "/day2/input.txt"
    data = getPuzzleInput(currPath)
    res1, res2 = game(data)
    printSolution(res1, res2)

def game(data):
    game, modifiedGame = Game(), ModifiedGame()
    count1, count2 = 0, 0
    OPPONENT_INDEX, ME_INDEX = 0, 1
    for item in data:
        d = item.rstrip().split()
        opponent, me, outcome = Hand(d[OPPONENT_INDEX]), Hand(d[ME_INDEX]), Outcome(d[ME_INDEX])
        count1 += game.playGame(opponent.getOption(), me.getOption())
        count2 += modifiedGame.playGame(opponent.getOption(), outcome.getOption())
    return count1, count2 

def printSolution(res1, res2):
    print('--- Answer To Part 1 ---')
    print(res1)
    print()
    print('--- Answer To Part 2 ---')
    print(res2)
    print()