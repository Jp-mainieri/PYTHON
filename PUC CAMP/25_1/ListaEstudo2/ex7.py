def somaNumeros(numero):
    soma = 0
    maiorN = 0
    numero = str(numero)
    for n in numero:
        n = int(n)
        soma += n
        if n > maiorN:
            maiorN = n
    return soma, maiorN
print("Digite um número inteiro:")
numero = int(input("> "))
soma,maior = somaNumeros(numero)
print(f"A soma dos digitos é: {soma}")
print(f"O maior dígito é: {maior}")
