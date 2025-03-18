greatest = 0
secGreatest = 0

for x in range(0, 10):
    num = int(input("Digite um número: "))
    if num > greatest:
        secGreatest = greatest
        greatest = num
print(f"O maior número é {greatest} e o segundo maior é {secGreatest}")