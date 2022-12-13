class CD:
    def __init__(self) -> None:
        pass
    
    def execute(self, command, fs):
        dir = None
        if command == '..':
            dir = self._upOneDirectory(fs)
        else:
            dir = self._changeDirectory(fs, command)
        return dir

    def _changeDirectory(self, fs, dirName):
        return fs.cd(dirName)
        
    def _upOneDirectory(self, fs):
        return fs.cdUp() 
    
