import sys

class Log:
    
    def __init__(self):
        self.out = sys.stdout
        self.err = sys.stderr
        self.verbose = False

    def error(self, string):
        try:
            self.err.write("ERROR: " + str(string) + "\n")
        except:
            return

    def default(self, string):
        try:
            self.out.write(str(string) + "\n")
        except:
            return
    
    def debug(self, string):
        if self.verbose:
            self.default(string)

log = Log()
