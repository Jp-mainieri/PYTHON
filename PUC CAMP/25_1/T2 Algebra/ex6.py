import numpy as np

# Matriz aumentada do sistema
A = np.array([
    [2, 5, 2, -38],
    [3, -2, 4, 17],
    [-6, 1, -7, -12]
], dtype=float)

# Função para aplicar o Método de Eliminação de Gauss
def eliminacao_de_gauss(matriz):
    n = len(matriz)
    
    # Escalonamento
    for i in range(n):
        # Pivotamento parcial (opcional para evitar divisões por zero)
        for k in range(i + 1, n):
            if abs(matriz[i][i]) < abs(matriz[k][i]):
                matriz[[i, k]] = matriz[[k, i]]
        
        # Tornar os elementos abaixo do pivô iguais a zero
        for j in range(i + 1, n):
            fator = matriz[j][i] / matriz[i][i]
            matriz[j, i:] -= fator * matriz[i, i:]
    
    return matriz

# Substituição retroativa para encontrar as soluções
def substituicao_retroativa(matriz):
    n = len(matriz)
    x = np.zeros(n)
    
    for i in range(n - 1, -1, -1):
        x[i] = (matriz[i, -1] - np.dot(matriz[i, i+1:n], x[i+1:n])) / matriz[i, i]
    
    return x

# Aplicando o método
A_escalonada = eliminacao_de_gauss(A)
solucoes = substituicao_retroativa(A_escalonada)

# Exibindo os resultados
print("Matriz escalonada:")
print(A_escalonada)
print("\nSoluções (x, y, z):")
print(solucoes)