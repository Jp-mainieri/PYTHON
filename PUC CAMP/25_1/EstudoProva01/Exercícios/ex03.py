first = second = third = float("-inf")
for x in range(3):
    num = int(input(">"))
    if num > first:
        third = second
        second = first
        first = num
    elif num > second:
        third = second
        second = num
    elif num > third:
        third = num
print(f"a sequencia em ordem decrescente ficou: {first}, {second}, {third}")