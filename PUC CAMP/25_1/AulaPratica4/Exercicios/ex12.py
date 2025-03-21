num = int(input("Digite um numero: "))


if num <= 1:
    num = print("O numero não é primo")
else:
    isPrime = True
    for i in range(2, num+1):
        if num % i == 0:
            isPrime = False
            break
    print(i)
if isPrime:
    print("O numero é primo")
else:
    print("O numero não é primo")
