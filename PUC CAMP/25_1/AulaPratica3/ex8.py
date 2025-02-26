num1 = int(input("Numero INTEIRO de 3 dígitos: "))

a = num1//100*100
b = (num1%100)//10*10
c = num1%10
print(num1)
num1 = a+b+c
print(c,b,a)
print(num1)
