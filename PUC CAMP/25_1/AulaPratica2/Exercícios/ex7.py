# perimetro do terreno + preço por M

width = int(input("width"))
lenght = int(input("lenght"))

perimeter = width*2 + lenght*2
print(perimeter)

price = float(input('Price'))

totalPrice = price * perimeter

print(totalPrice)