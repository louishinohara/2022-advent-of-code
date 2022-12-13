class File:
    def __init__(self, filename, size):
        self.filename, self.size = filename, size

    def getClassName(self):
        return self.__class__.__name__
    
    def getFileSize(self):
        return self.size