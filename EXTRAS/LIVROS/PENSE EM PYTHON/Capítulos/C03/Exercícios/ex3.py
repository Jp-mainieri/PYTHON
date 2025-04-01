def topLine():
    print("+", end=" ")
    print("- " * 4, end="")
    print("+", end=" ")
    print("- " * 4, end="")
    print("+", end="")
    print()

def borders():
    print("|", end="         ")
    print("|", end="         ")
    print("|", end="         ")
    print()
def doFour(f):
    f()
    f()
    f()
    f()
def doTwice(f,value):
    f(value)
    f(value)

topLine()
doFour(borders)
topLine()
doFour(borders)
topLine()