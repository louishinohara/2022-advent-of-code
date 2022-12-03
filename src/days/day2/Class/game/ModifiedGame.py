from src.days.day2.Outcome.Outcome import Win, Loss, Tie
from src.days.day2.Class.hand.Hand import Rock, Paper, Scissor


class ModifiedGame:
    def __init__(self):
        pass

    def playGame(self, opponent, me):
        res = None
        if isinstance(opponent, Rock):
            res = self._opponentIsRock(me)
        elif isinstance(opponent, Paper):
            res = self._opponentIsPaper(me)
        else:
            res = self._opponentIsScissor(me)
        return res.getPoint() + me.getPoint()
    
    def _opponentIsRock(self, me):
        res = None
        if isinstance(me, Win):
            res = Paper()
        elif isinstance(me, Loss):
            res = Scissor()
        else:
            res = Rock()
        return res


    def _opponentIsPaper(self, me):
        res = None
        if isinstance(me, Win):
            res = Scissor()
        elif isinstance(me, Loss):
            res = Rock()
        else:
            res = Paper()
        return res


    def _opponentIsScissor(self, me):
        res = None
        if isinstance(me, Win):
            res = Rock()
        elif isinstance(me, Loss):
            res = Paper()
        else:
            res = Scissor()
        return res