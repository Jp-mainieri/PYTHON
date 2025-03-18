# Sequencia = 2, 3, 5, 8, 13, 21...
Nprimeiros = int(input("Digite a quantidade de termos: "))
termo1, termo2 = 2, 3
soma = 0
for x in range(Nprimeiros):
    soma += termo1
    proximo = termo1 + termo2
    termo1 = termo2
    termo2 = proximo
print(soma)
