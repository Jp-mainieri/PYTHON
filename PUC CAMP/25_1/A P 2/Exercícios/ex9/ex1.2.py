buyCost = float(input("Valor da compra:"))
paid = float(input("Valor Pago:"))

troco = paid - buyCost

if troco != 0:
    c100 = troco//100
    c50 = (troco - c100*100) // 50
    c20=(troco-c100*100-c50*50)//20
    c10=(troco-c100*100-c50*50-c20*20)//10
    c5=(troco-c100*100-c50*50-c20*20-c10*10)//5
    c1=(troco-c100*100-c50*50-c20*20-c10*10-c5*5)//1
    print(troco)
    print(c100, c50, c20,c10,c5,c1)
else:
    print("sem troco")

