#Sequencia(5 primeiros) = [1,2,5,12,29]
#Formula = 2* (N-1) + (N-2)


N = int(input(">"))                             #Pede o qual vai ser o termo a ser achado (enésimo)
termo1 = 1                                      #Define o termo 1 da sequencia = 1
termo2 = 2                                      #Define o termo 2 da sequencia = 2
soma = 0                                        #Pode ser soma = 3 para exluir etapas no processo
if N == 1:                                      #Verifica se o N = 1, se sim, o resultado é igual ao primeiro termo, 1
    termoN = termo1
    soma = termo1
elif N == 2:                                    #Verifica se o N = 2, se sim, o resultado é igual ao segundo termo, 2
    termoN = termo2
    soma = termo1 + termo2                      #Excluível, se definir soma = 3 no inicio
else: #OU :
    soma = termo1 + termo2                      #Excluível, se definir soma = 3 no inicio
    for _ in range(3, N+1):                     #Para _ de 3 até N (enésimo termo) + 1 ## +1 para o enésimo entrar na variação esperada
        termoN = 2 * termo2 + termo1            #Define que o termoAtual = 2 * (o enésimo termo-1 (anterior)) + (enésimo termo-2 (anti-anterior)) ##Usando a fórmula da sequência
        soma += termoN                          #Somar os termos até chegar no esperado
        termo1,termo2=termo2,termoN             #Define que o termo 1 agora é igual ao seguinte(termo2), o termo2 vira o seu sucessor(termoAtual)
print(termoN)                                   #Imprimir a resposta (enésimo termo)
print(soma)                                     #Imprimir a soma dos termos até o enésimo

