ageAbove50 = 0
avgHeight = 0
wheigthBelow50 = 0

for x in range(25):
    age = int(input("Digite a idade: "))
    height = float(input("Digite a altura: "))
    wheigth = float(input("Digite o peso: "))
    if age > 50:
        ageAbove50 += 1
    if 10 <= age <= 20:
        avgHeight += height
    if wheigth < 50:
        wheigthBelow50 += 1
print(f"A quantidade de pessoas com idade superior a 50 anos é {ageAbove50}")
print(f"A média das alturas das pessoas com idade entre 10 e 20 anos é {avgHeight/25}")
print(f"A porcentagem de pessoas com peso inferior a 50 quilos é {wheigthBelow50/25*100}%")
        