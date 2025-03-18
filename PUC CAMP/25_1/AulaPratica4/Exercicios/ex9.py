population = 10
avgSalary = 0
avgSons = 0
greatestSalary = 0
hSalaryMin = 0

for _ in range(population):
    hSalary = float(input("Digite o salário do habitante: "))
    hSons = int(input("Digite a quantidade de filhos do habitante: "))
    avgSalary += hSalary
    avgSons += hSons
    if hSalary > greatestSalary:
        greatestSalary = hSalary
    if hSalary <= 100:
        hSalaryMin += 1
print(f"A média de salário da população é {avgSalary/population}")
print(f"A média de filhos da população é {avgSons/population}")
print(f"O maior salário é {greatestSalary}")
print(f"A quantidade de habitantes com salário menor ou igual a R$100,00 é {hSalaryMin}")
