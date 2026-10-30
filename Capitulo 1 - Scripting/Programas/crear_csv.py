import csv

equipos = [
    ["PC-AULA-01", "192.168.1.101", "Windows 11", "Aula 1"],
    ["PC-AULA-02", "192.168.1.102", "Windows 11", "Aula 1"],
    ["SERVIDOR-01", "192.168.1.10", "Ubuntu Server", "CPD"]
]

with open("Capitulo 1 - Scripting/Datos/equipos_exportados.csv", "w", encoding="utf-8", newline="") as archivo:
    escritor = csv.writer(archivo)

    escritor.writerow(["nombre", "ip", "sistema", "ubicacion"])

    for equipo in equipos:
        escritor.writerow(equipo)

print("Inventario exportado correctamente.")