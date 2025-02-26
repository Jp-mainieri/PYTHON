num1 = int(input("Numero de até dois digitos: "))

if num1 < 10:
    print(num1)
else:
    soma = num1 // 10 + num1 % 10
    print(soma)