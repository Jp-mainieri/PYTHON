intervalo0_25 = 0
intervalo26_50 = 0
intervalo51_75 = 0
intervalo76_100 = 0


while True:
    num = int(input("Digite um número: "))
    if num < 0:
        break
    if (0 <= num <= 25):
        intervalo0_25 +=  1    
    elif (26 <= num <= 50):
        intervalo26_50 += 1
    elif (51 <= num <= 75):
        intervalo51_75 += 1
    elif (76 <= num <= 100):
        intervalo76_100 += 1

print(f"Intervalo [0, 25]: {intervalo0_25}")
print(f"Intervalo [26, 50]: {intervalo26_50}")
print(f"Intervalo [51, 75]: {intervalo51_75}")
print(f"Intervalo [76, 100]: {intervalo76_100}")