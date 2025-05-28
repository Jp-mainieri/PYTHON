while True:
    num = int(input("Digite um número: "))
    def isPerfeito(numero):
        soma = 0
        for i in range(1,numero):
            if numero % i == 0:
                soma+=i
        if numero == soma:
            return "É perfeito"
        else:
            return "Não é perfeito"
    print(isPerfeito(num))