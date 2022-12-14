class Hand:
    pointKey = {'Rock': 1, 'Paper': 2, 'Scissor': 3}
    def __init__(self, choice):
        self._option = self._setOption(choice)
        
    def _setOption(self, choice):
        keys = {
            'A': Rock(), 'X': Rock(),
            'B': Paper(), 'Y': Paper(),
            'C': Scissor(), 'Z': Scissor(),
        }
        return keys[choice]
    
    def getOption(self):
        return self._option

    def getPoint(self):
        return self.pointKey[self.getClassName()]

    def getClassName(self):
        return self.__class__.__name__

class Rock(Hand):
    def __init__(self):
        pass

class Paper(Hand):
    def __init__(self):
        pass

class Scissor(Hand):
    def __init__(self):
        pass