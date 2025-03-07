#ler 100 numeros, imprimir o menor
menor_num = int('inf')
i = 0
while i < 10:
    num = float(input(f"numero {i + 1}: "))

    if num < menor_num:
        menor_num = num

    i += 1

print(f'menor número entre os 100 é: {menor_num}')