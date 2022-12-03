from src.days.day2.Class.outcome.Outcome import Win, Loss, Tie
from src.days.day2.Class.hand.Hand import Rock, Paper, Scissor

class Game:
    rules = {
        'Rock' : {'Rock': Tie, 'Paper': Win, 'Scissor': Loss },
        'Paper' : {'Rock': Loss, 'Paper': Tie, 'Scissor': Win },
        'Scissor' : {'Rock': Win, 'Paper': Loss, 'Scissor': Tie },
    }

    modifiedRules = {
        'Rock' : {'Tie': Rock, 'Win': Paper, 'Loss': Scissor },
        'Paper' : {'Loss': Rock, 'Tie': Paper, 'Win': Scissor },
        'Scissor' : {'Win': Rock, 'Loss': Paper, 'Tie': Scissor },
    }

    def __init__(self):
        pass

    def playGame(self, opponent, me):
        res = self._applyRules(opponent.getClassName(), me.getClassName())
        return res.getPoint() + me.getPoint()

    def playModifiedGame(self, opponent, me):
        res = self._applyModifiedRules(opponent.getClassName(), me.getClassName())
        return res.getPoint() + me.getPoint()

    def _applyRules(self, opponent, me):
        return self.rules[opponent][me]()
        
    def _applyModifiedRules(self, opponent, me):
        return self.modifiedRules[opponent][me]()
