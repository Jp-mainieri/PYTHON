tabuleiro = [
    [1,2,3],
    [1,2,3],
    [1,0,1]
]

numColunas = len(tabuleiro[0])
pontosColuna = []

for j in range(numColunas):
    totalC = 0
    dadosColuna = 0
    repetidos = []
    elementosColuna = []
    contRepetidos = []
    for i in range(len(tabuleiro)): #Pssa pela primeira coluna, por cada uma das linhas

        elementosColuna.append(tabuleiro[i][j])
        totalC += tabuleiro[i][j]
        print(tabuleiro[i][j])
        print()
        print(elementosColuna)
    for i in range(len(tabuleiro)):
        if elementosColuna.count(tabuleiro[i][j]) > 1:
            if tabuleiro[i][j] not in repetidos:
                repetidos.append(tabuleiro[i][j])
                contRepetidos.append(elementosColuna.count(tabuleiro[i][j]))
        print()
        print(repetidos)
        print(contRepetidos)
        print()

    



    pontosColuna.append(totalC)
print()
print(pontosColuna)
