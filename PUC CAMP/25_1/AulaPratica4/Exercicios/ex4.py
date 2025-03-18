print("Farhenheit | Celsius")
for fahrenheith in range(30, 51, 2):
    celsius = (fahrenheith - 32) * 5 / 9
    print(f"{fahrenheith}°F | {celsius:.2f}°C")