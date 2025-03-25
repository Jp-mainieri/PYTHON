average = 0 
cont = 0
for x in range(15,101): #para x no intervalo de 15 a 100, a variavel average soma ela mesma com o x (número de 15 a 100) e o contador soma 1.
    average = average + x
    cont += 1
average /= cont # aqui é cauculada a média, onde á soma dos números é dividida pelo contador.
print(f"a média dos números entre 15 e 100 é {average}") #Imprimir no console