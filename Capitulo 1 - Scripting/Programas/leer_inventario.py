import csv

with open("Capitulo 1 - Scripting/Datos/inventario.csv", "r", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)

    for equipo in lector:
        if equipo["sistema"] == "Windows 11":
            print(f"{equipo['nombre']} - {equipo['ip']}")