
class CliReader():
    
    def __init__(self, inputStream):
        self.inputStream = inputStream
        
    def readline(self):
        return self.inputStream.readline()