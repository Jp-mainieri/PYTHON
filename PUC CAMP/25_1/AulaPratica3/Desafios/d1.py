workPlan = int(input("Plano de trabalho"))
salary = int(input("Seu Salário atual"))
newSalary = int()

if 3 < workPlan or workPlan < 1:
    print("Erro")
else:
    if workPlan == 1:
        newSalary = salary + salary * 0.1
        print(newSalary)
    elif workPlan == 2:
        newSalary = salary + salary * 0.15
        print(newSalary)
    else:
        newSalary = salary + salary * 0.2
        print(newSalary)