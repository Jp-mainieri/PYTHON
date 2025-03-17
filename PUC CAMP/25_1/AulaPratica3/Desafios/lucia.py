x = int(input("Base: "))
n = int(input("Expoente: "))

if n < 0:
    print("erro")
else:
    pot=1
    cont=n
    while cont >= 1:
        pot = x * pot
        cont -= 1
    print(f"{x} ^ {n} = {pot}")