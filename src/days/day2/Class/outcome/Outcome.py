class Outcome:
    pointKey = {'Win': 6, 'Loss': 0, 'Tie': 3}
    def __init__(self, choice):
        self._option = self._setOption(choice)
        
    def _setOption(self, choice):
        keys = {
            'X': Loss(),
            'Y': Tie(),
            'Z': Win(),
        }
        return keys[choice]
    
    def getOption(self):
        return self._option

    def getPoint(self):
        return self.pointKey[self.getClassName()]

    def getClassName(self):
        return self.__class__.__name__   


class Win(Outcome):
    def __init__(self):
        pass

class Loss(Outcome):
    def __init__(self):
        pass

class Tie(Outcome):
    def __init__(self):
        pass
