valorHoraAula = float(input("Digite o valor da HORA AULA: "))
aulasLecionadas = int(input("Digite a quantidade de AULAS LECIONADAS no mês: "))
descontoINSS = float(input("Digite percentual de desconto do INSS(%): "))
descontoINSS = descontoINSS/100 * valorHoraAula * aulasLecionadas
salarioLiquido = (valorHoraAula * aulasLecionadas) - descontoINSS
print(f"O salário líquido do professor foi {salarioLiquido}")