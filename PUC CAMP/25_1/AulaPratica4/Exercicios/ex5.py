S = 0

for d in range(1, 100, 2):
    for n in range(1,51):
        S += d / n
print(f"{S:.2f}")
#S = D/N + D/N + D/N