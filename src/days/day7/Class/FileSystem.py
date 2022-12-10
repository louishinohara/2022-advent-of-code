from Dir import Dir
from Command import Command

class FileSystem:
    def __init__(self):
        self.head = Dir('/')
        self.fs = {}
        
    def buildFileSystem(self, data):
        index = 1
        while index <= len(data):
            c = data[index]
    
    def parseInput(input):
        option = input.split('')[0]
        if option == '$':
            command = Command(c)
        elif option == 'dir':
            command = Dir(c)