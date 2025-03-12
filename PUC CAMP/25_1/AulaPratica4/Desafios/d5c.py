while True:
    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))
    d = int(input("d: "))
    e = int(input("e: "))
    f = int(input("f: "))

    if a == 0 and b == 0 and c == 0 and d == 0:
        break

    # Determinante principal
    det = a * e - b * d

    if det == 0:
        print("O sistema não tem solução.")
    else:
        # Usando a regra de Cramer
        x = (c * e - b * f) / det
        y = (a * f - c * d) / det
        print(f"Solução: x = {x}, y = {y}")