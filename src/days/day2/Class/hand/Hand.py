class Hand:
    def __init__(self, choice):
        self._option = self._setOption(choice)
        
    def _setOption(self, choice):
        if choice in ('A', 'X'):
            return Rock()
        elif choice in ('B', 'Y'):
            return Paper()
        else:
            return Scissor()
    
    def getOption(self):
        return self._option


class Rock(Hand):
    ASSOCIATED_POINT = 1
    def __init__(self):
        pass
    
    def getPoint(self):
        return 1
       
    def getName(self):
        return self.__class__.__name__
     
class Paper(Hand):
    ASSOCIATED_POINT = 2
    def __init__(self):
        pass
    
    def getPoint(self):
        return 2
    
    def getName(self):
        return self.__class__.__name__
    
class Scissor(Hand):
    ASSOCIATED_POINT = 3
    def __init__(self):
        pass
    
    def getPoint(self):
        return 3
    
    def getName(self):
        return self.__class__.__name__