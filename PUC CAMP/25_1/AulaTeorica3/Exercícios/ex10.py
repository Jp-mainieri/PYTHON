salaryBase = 1500
soldCars = int(input("Numero de carros vendidos: "))
salesValue = int(input("Valor total de vendas: "))
commision = 200 * soldCars + 0.05 * salesValue


totalSalary = salaryBase + commision

print("O Funcionário irá receber um total de {0}, somando o salario base ({1}), os 200 reais por cada carro vendido ({2} carros) e 5/100 do valor de todas as vendas ({3})".format(totalSalary, salaryBase, soldCars, salesValue))

