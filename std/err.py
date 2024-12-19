import sys

def ein():
    return sys.stderr.readline()


def eread():
    return sys.stderr.read()
    
def eout(content):
    sys.stderr.write(str(content))

def erout(content):
    sys.stderr.write(str(content) + "\n")

def redirerr(filename):
    sys.stderr = open(filename, "r")