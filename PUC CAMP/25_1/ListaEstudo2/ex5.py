numeros = [int(input("Digite um número real: ")) for _ in range(10)]
media = 0
cont = 0
pares = []
for n in numeros:
    if n > 30:
        media += n
        cont += 1
    if n >= 24 and n % 2 == 0:
        pares.append(n)
media = media / cont if cont > 0 else 0
print(numeros)
print(f"A média dos números maiores que 30 é: {media}")
for p in pares:
    print(f"Número par maior ou igual a 24: {p}")