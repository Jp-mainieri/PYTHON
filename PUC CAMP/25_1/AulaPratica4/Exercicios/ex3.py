num1 = float(input("number1: "))
num2 = float(input("number2: "))
if num1 == num2:
    print("são iguais")
elif num1 > num2:
    print(f"{num1:.2d} é maior")
else:
    print(f"{num2:.2d} é maior")