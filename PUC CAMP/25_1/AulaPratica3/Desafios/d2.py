x = int(input("Número: "))
n = int(input("Elevado á: "))

if n < 0:
    print("erro")
elif n == 0:
    print(1)
else:
    pot=1
    while n > 1:
        pot = x * pot
        n -= 1
    print(pot)