n1 = float(input("Nota1: "))
n2 = float(input("Nota2: "))
p1 = float(input("Peso1: "))
p2 = float(input("Peso2: "))
media = (n1*p1 + n2*p2) / (p1 + p2)

if media == 10:
    print("Aprovado com Distinção")
elif media >= 7:
    print("Aprovado")
else:
    print("Reprovado")