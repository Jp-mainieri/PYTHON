A = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]
for i in range(3):
    for j in range(4):
        if i < j:
            A[i][j] = j-1
        if i > j:
            A[i][j] = 2*i
        if i == j:
            A[i][j] = i+j
print(A)

        