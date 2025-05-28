str1 = input("Digite a primeira string: ")
str2 = input("Digite a segunda string: ")
ultimas = str1[len(str1)-len(str2):]
if str2 in ultimas:
    print("sim")