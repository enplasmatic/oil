import sys, inspect

endl = "\n"
endr = "\r\n"

def lin():
    try:
        return sys.stdout.readline()
    except:
        return input()
    
def linf():
    try:
        return sys.stdout.read()
    except:
        return input()

def getlin():
    try:
        return sys.stdout.readlines()
    except:
        return input()
    
def ln(content):
    sys.stdout.write(str(content))

def lnf(content):
    sys.stdout.write(str(content)+"\n")

def lnraw(content):
    sys.stdout.write((content))
    
def lnrawf(content):
    sys.stdout.write((content)+"\n")

def redirin(filename):
    sys.stdin = open(filename, "r")

def redirout(filename):
    sys.stdout = open(filename, "r")


class IOScanner:
    def __init__(self):
        self.terminal = []
        self.syncio(1)
    
    def __call__(self):
        return "\n".join(self.terminal)
    
    def println(self, content):
        self.ln(content)
        self.terminal.append(content)

    def printlnf(self, content):
        self.ln(content+"\n")
        self.terminal.append(content+"\n")

    def getln(self, message=""):
        content = self.lin(message)
        self.terminal.append(message+content)
        return content
    
    def clear(self):
        self.terminal = []

    def access(self, index):
        return self.terminal[index]
    
    def accessrange(self, start, end):
        return self.terminal[start:end+1]
    
    def syncio(self, cut):
        if cut == 0:
            self.lin = sys.stdout.readline
            self.ln = sys.stdin.write
        else:
            self.lin = input
            self.ln = print

class ErrScanner:
    def __call__(self, *args, **kwds):
        pass
