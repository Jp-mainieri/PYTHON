
n = float(input(">"))
qt025 = 0
qt2650 = 0
qt5175 = 0
qt76100 = 0
while n >= 0:
    if 0 <= n <= 25:
        qt025 +=1
    elif 26 <= n <= 50:
        qt2650 += 1
    elif 51 <= n <= 75:
        qt5175 +=1
    elif 76 <= n <= 100:
        qt76100 +=1
    n = float(input(">"))
print(qt025)
print(qt2650)
print(qt5175)
print(qt76100)