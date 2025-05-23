emprestimoElegivel = True
pessoas = [
    {"nome": "pessoa1", "idade": 18, "renda mensal": 2000, } #"escolaridade": "superior"
]

inadimplentes = ["João Pedro","Bet","Bubula","Kendi"]

def verificar(pessoas):
        elegivel = True
        motivo = []
        nome = input("Nome da pessoa para verificar a eligibilidade para o empréstimo:")
        i = 0
        for p in pessoas:
            i+=1
            if nome == p["nome"]:
                break
            elif len(pessoas) == i:
                return print("Nome Inválido")
        if p["idade"] < 18:
            elegivel = False
            motivo.append("Idade menor que 18 anos")
        if p["renda mensal"] < 2000:
            elegivel = False
            motivo.append("Renda mensal menor que R$2.000,00")
       
        for n in inadimplentes:
            if p["nome"] == n:
                elegivel = False
                motivo.append("Nome na lista de inadimplentes")
        if elegivel == True:
            print(f"{nome} é elegível para um empréstimo")
        else:
            f"{nome} não é elegivel para um empréstimo, motivos:"
            for m in motivo:
                print(f"-{m}")



verificar(pessoas)


        