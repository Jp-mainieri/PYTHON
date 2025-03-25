salarioHabitante = int(input("salário: "))
mediaSal = 0
mediafil = 0
maiorSalario = 0
percentualSalarioMinimo = 0
cont = 0
while salarioHabitante >= 0:
    filhosHabitante = int(input("número de filhos: "))
    mediaSal += salarioHabitante
    mediafil += filhosHabitante
    if salarioHabitante > maiorSalario:
        maiorSalario = salarioHabitante
    if salarioHabitante < 1500:
        percentualSalarioMinimo += 1
    cont+= 1
    salarioHabitante = int(input("salário: "))
print(mediaSal/cont)
print(mediafil/cont)
print(maiorSalario)
print(percentualSalarioMinimo/cont*100, "%")
