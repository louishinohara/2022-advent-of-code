class Dir:
    def __init__(self, up, name):
        self.up = up
        self.files = {}
        self.name = name
        self.dirSize = 0

    def getClassName(self):
        return self.__class__.__name__

    def setFiles(self, k, v):
        self.files[k] = v

    def getFiles(self):
        return self.files

    def cd(self, k):
        return self.files[k]

    def cdUp(self):
        return self.up

    def getDirSize(self):
        return self.dirSize

    def _setDirSize(self, dirSize):
        self.dirSize = dirSize

    # Recursively check dirs and set size of current dir
    def getTotalDirSize(self):
        def helper(files):  # Recursively gets file size for dir
            localDirSize = sum([    # If Dir, recursively check files. If file, get size. Sum all items in list
                helper(item.getFiles()) 
                if isinstance(item, Dir) 
                else item.getFileSize() 
                for item in files.values()
            ])
            return localDirSize

        totalDirSize = helper(self.files)
        self._setDirSize(totalDirSize)
