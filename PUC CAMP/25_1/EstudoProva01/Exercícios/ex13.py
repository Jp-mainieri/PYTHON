mais50 = 0
mediaAltura1020 = 0
porcentagemPeso40 = 0

for x in range(25):
    idade = int(input("idade:"))
    altura = int(input("altura:"))
    peso = int(input("peso:"))
    if idade > 50:
        mais50 += 1
    elif 10 < idade < 20:
        mediaAltura1020 += altura
    if peso < 40:
        porcentagemPeso40 += 1
print(mais50)
print(mediaAltura1020/25)
print(porcentagemPeso40/25*100)
