num = int(input("Digite um numero: "))


if num <= 1:
    num = print("O numero não é primo")
else:
    isPrime = True
    i = 2
    while i < num:
        if num % i == 0:
            isPrime = False
            break
        i += 1
    print(i)
if isPrime:
    print("O numero é primo")
else:
    print("O numero não é primo")
