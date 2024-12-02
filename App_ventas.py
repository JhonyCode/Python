nombre = input("Cual es tu nombre:")
ventas = input("Indica cuanto has vendido:")

comision = int(ventas) * 13 / 100

print(f"Este mes has obtenido de comisión: {round(comision,2)} ")