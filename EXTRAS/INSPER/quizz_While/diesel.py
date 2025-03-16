days = int(input('Days to analyse: '))
bestPrice = float('inf')
worstPrice = float('-inf')
averagePrice = 0
i = 1
while i <= days:
    dayPrice = float(input(f'Preço do dia {i}: '))
    if dayPrice < bestPrice:
        bestPrice = dayPrice
        bestPriceDay = i
    elif dayPrice > worstPrice:
        worstPrice = dayPrice
        worstPriceDay = i
    averagePrice = (averagePrice + dayPrice) / 2
    i += 1
print(f'O dia {bestPriceDay} foi o melhor dia para compra')
print(f'O dia {worstPriceDay} foi o pior dia para compra')
print(f'O preço médio cobrado foi de {averagePrice:.2f}')