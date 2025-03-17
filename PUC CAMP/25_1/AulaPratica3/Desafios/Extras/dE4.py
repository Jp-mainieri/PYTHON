N = int(input("quantos numeros?"))
i = 0
greaterX = float("-inf")
smallestX = float("inf")

if N >= 10:
    while i < N:
        x = int(input("numero: "))
        if x > greaterX:
            greaterX = x
        elif x < smallestX:
            smallestX = x
        i += 1
    print(greaterX)
    print(smallestX)
else:
    print("erro, escolha um numero maior ou igual a 10")