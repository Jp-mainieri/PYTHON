#ax+by = c
#dx+ey = f



while True:
    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))
    d = int(input("d: "))
    e = int(input("e: "))
    f = int(input("f: "))
    
    
    if a == 0 and b == 0 and c == 0 and d == 0:
        print("Sistema impossível")
        break
    else:
        x = (c*e - b*f) / (a*e - b*d)
        y = (a*f - c*d) / (a*e - b*d)
        print(f"x = {x}")
        print(f"y = {y}")
    
    
    
    