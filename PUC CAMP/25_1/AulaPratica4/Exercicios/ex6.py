S = 0
for x in range(1,11):
    if x % 2 == 0:
        S -= x / (x ** 2)
    else:
        S += x / (x ** 2)
print(f"{S:.2f}")