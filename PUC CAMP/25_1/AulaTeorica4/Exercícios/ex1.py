#Menor número sem loops

a = int(input('num1'))
b = int(input('num2'))
c = int(input('num3'))
if a == b == c:
    print("iguais")
elif a < b and a < c:
    print(f"{a} é menor")
elif b < a and b < c:
    print(f"{b} é menor")
else:
    print(f"{c} é menor")

#com loops

numbers = []

numbers.append(int(input(len(numbers))))