import csv

nombre = input("Nombre del equipo: ")
ip = input("Dirección IP: ")
sistema_operativo = input("Sistema Operativo: ")
ubicacion = input("Ubicación: ")

with open("Capitulo 1 - Prácticas/36. Inventario de red/Datos/inventario_alumnos.csv", "a", encoding="utf-8", newline="") as archivo:
    escritor = csv.writer(archivo)

    escritor.writerow([nombre, ip, sistema_operativo, ubicacion])