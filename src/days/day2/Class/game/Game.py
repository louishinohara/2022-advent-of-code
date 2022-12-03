from src.days.day2.Class.hand.Hand import Rock, Paper, Scissor

class Game:
    WIN, LOSS, TIE = 6, 0, 3

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
        return res + me.getPoint()
    
    def _opponentIsRock(self, me):
        res = None
        if isinstance(me, Rock):
            res = self.TIE
        elif isinstance(me, Paper):
            res = self.WIN
        else:
            res = self.LOSS
        return res


    def _opponentIsPaper(self, me):
        res = None
        if isinstance(me, Rock):
            res = self.LOSS
        elif isinstance(me, Paper):
            res = self.TIE
        else:
            res = self.WIN
        return res


    def _opponentIsScissor(self, me):
        res = None
        if isinstance(me, Rock):
            res = self.WIN
        elif isinstance(me, Paper):
            res = self.LOSS
        else:
            res = self.TIE
        return res