equipo = input("Nombre del equipo: ")
incidencia = input("Descripción de la incidencia: ")

with open("Capitulo 1 - Prácticas/23. Práctica propuesta/Datos/incidencias.txt", "a", encoding="utf-8") as archivo:
    archivo.write(f"{equipo} - {incidencia} \n")

print("Información guardada!")