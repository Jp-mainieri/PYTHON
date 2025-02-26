temperatureF = float(input("Insira a temperatura em Fahrenheit"))

temperatureC = (temperatureF - 32) * 5/9

print("Em Graus Celcius, a temperatura de {0} Fahrenheit fica {1:.2f}°C".format(temperatureF,temperatureC))