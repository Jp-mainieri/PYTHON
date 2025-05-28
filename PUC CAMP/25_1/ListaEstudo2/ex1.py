def proc7(msg="Olá",repetir=1):
    for _ in range(repetir):
        print(msg + "!")
proc7()
proc7(msg="Mundo")
proc7(repetir=4)
proc7("Python",2)