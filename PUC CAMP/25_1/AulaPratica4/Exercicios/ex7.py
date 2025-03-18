num = int(input("> "))
pares = 0
impares = 0
while num != 0:
    if num < 0:
        num = int(input("Digite um número válido:  "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    num = int(input("> "))
print(f"Quantidade de pares: {pares}")
print(f"Quantidade de ímpares: {impares}")

    