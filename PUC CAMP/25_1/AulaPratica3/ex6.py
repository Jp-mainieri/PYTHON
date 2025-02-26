# litros gastos por um automóvel na viagem

autonomy = 12 #KM/L

time = float(input("Tempo gasto: "))
velAverage = float(input("Velocidade média: "))

totalDistance = velAverage * time

totalConsume = totalDistance / autonomy

print(velAverage, 'km/h')
print(time, 'h')
print(totalDistance, 'km')
print(totalConsume, 'L')



