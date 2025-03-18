num = int(input("Digite um número: "))
numFactorial = 1
while num >=0:
    while num > 0:
        numFactorial = numFactorial * num
        num -= 1
    print(f"O fatorial de {num} é {numFactorial}")
    numFactorial = 1
    num = int(input("Digite um número: "))