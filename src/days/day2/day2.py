from functools import reduce
from src.constants import BASEPATH
from src.helpers.helpers import getPuzzleInput
from src.days.day2.Class.hand.Hand import Hand
from src.days.day2.Class.game.Game import Game
from src.days.day2.Class.outcome.Outcome import Outcome

def exec():
    currPath = BASEPATH + "/day2/input.txt"
    data = getPuzzleInput(currPath)
    res = game(data)
    printSolution(res)

def game(data):
    mapVal = map(mapFunc, data)
    reduceVal = reduce(reduceFunc, mapVal)
    return reduceVal

def mapFunc(input):
    game = Game()
    d = input.rstrip().split()
    OPPONENT_INDEX, ME_INDEX = 0, 1
    opponent, me, outcome = Hand(d[OPPONENT_INDEX]), Hand(d[ME_INDEX]), Outcome(d[ME_INDEX])
    res1 = game.playGame(opponent.getOption(), me.getOption())
    res2 = game.playModifiedGame(opponent.getOption(), outcome.getOption())
    return (res1, res2)

def reduceFunc(x, y):
    x1, y1 = x
    x2, y2 = y
    return (x1 + x2, y1 + y2)

def printSolution(res):
    res1, res2 = res
    print(f'--- Answer To Part 1 --- \n {res1} \n')
    print(f'--- Answer To Part 2 --- \n {res2} \n')