
numberOfProducts = int(input("Insira o numero de produtos para entrar em liquidação: "))
product = []
productPrice = []
productNewPrice = []
discount = int(input("Desconto em %: "))
i = 0

while i < numberOfProducts:
    product.append(input("Nome do Produto {}: ".format(i + 1)))
    productPrice.append(float(input("Preço do Produto {}: ".format(i + 1))))
    print(product, productPrice)
    i += 1

i = 0

while i < numberOfProducts:  
    new_price = productPrice[i] * (1 - discount / 100)  
    productNewPrice.append(new_price)  
    print("O produto: {0} que custava {1:.2f}, custa agora apenas {2:.2f}".format(product[i], productPrice[i], productNewPrice[i]))
    i += 1
