senha = "senha1$"
InputSenha = input("Digite sua senha: ")
for t in range(1,3):
    if senha == InputSenha:
        print("senha correta")
        break
    print(f"Senha incorreta, {t}/3 tentativas ultilizadas")
    InputSenha = input("Digite sua senha novamente: ")
if InputSenha != senha:
    print("Suas tentaivas acabaram, senha incorreta")