alunos = int(input("Número de alunos na sala: "))
mediaSala = 0
for x in range(alunos):
    nota = float(input(f"nota do {x+1}^o aluno: "))
    mediaSala += nota
print(f"a média da sala foi {mediaSala/alunos}")