
cont = int(input("contagem: "))
res = 0
odds = 0
while cont > 0:
    num = int(input(f"número: "))
    if num % 2 == 0:
        res +=num
    else:
        print(f"{num} é impar")
        odds += 1
    cont -= 1
print(res)
print(odds)