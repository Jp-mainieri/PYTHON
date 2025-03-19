grade = float(input("Nota de 0 até 10: "))
while not 0 <= grade <= 10:
    print("ERRO, VALOR INVÁLIDO")
    grade = float(input("Nota de 0 até 10: "))
print(grade)