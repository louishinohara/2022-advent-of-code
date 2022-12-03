class Outcome:
    def __init__(self, choice):
        self._option = self._setOption(choice)
        
    def _setOption(self, choice):
        if choice in ('A', 'X'):
            return Loss()
        elif choice in ('B', 'Y'):
            return Tie()
        else:
            return Win()
    
    def getOption(self):
        return self._option


class Win(Outcome):
    ASSOCIATED_POINT = 6
    def __init__(self):
        pass
    
    def getPoint(self):
        return self.ASSOCIATED_POINT
       
    def getName(self):
        return self.__class__.__name__
     
class Loss(Outcome):
    ASSOCIATED_POINT = 0
    def __init__(self):
        pass
    
    def getPoint(self):
        return self.ASSOCIATED_POINT
    
    def getName(self):
        return self.__class__.__name__
    
class Tie(Outcome):
    ASSOCIATED_POINT = 3
    def __init__(self):
        pass
    
    def getPoint(self):
        return self.ASSOCIATED_POINT
    
    def getName(self):
        return self.__class__.__name__