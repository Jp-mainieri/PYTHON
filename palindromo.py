def eh_palindromo(n):
    original = n
    invertido = 0
    while n != 0:
       num = n % 10
       invertido = invertido * 10 + num
       n = n // 10
       print(n)
       print(invertido)
       print(num)
    if original == invertido:
        return True
    else:
        return False   
         
print(eh_palindromo(int(input('>'))))
