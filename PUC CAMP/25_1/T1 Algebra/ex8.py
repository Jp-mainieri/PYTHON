A = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]
for i in range(0,3):
    for j in range(0,4):
        if i < j:
            A[i][j] = j-1
        if i > j:
            A[i][j] = 2*i
        if i == j:
            A[i][j] = i+j
print(A[0])
print(A[1])
print(A[2])
        