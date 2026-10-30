import csv

with open("Capitulo 1 - Scripting/Datos/inventario.csv", "r", encoding="utf-8") as archivo:
    lector = csv.reader(archivo)

    next(lector)

    for fila in lector:
        print(f"Equipo: {fila[0]}")
        print(f"IP: {fila[1]}")
        print(f"Sistema: {fila[2]}")
        print(f"Ubicación: {fila[3]}")
        print("-------------------------")