def greaterNum():
    greater = float("-inf")
    for i in range(0,3):
        num = int(input("Digite um número: "))
        if greater < num:
            greater = num
    print(f"O maior número é: {greater}")
greaterNum()