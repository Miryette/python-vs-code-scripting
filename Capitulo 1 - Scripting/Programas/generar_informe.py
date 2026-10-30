contador = 0

with open("Capitulo 1 - Scripting/Datos/equipos.txt", "r", encoding="utf-8") as origen:
    with open("Capitulo 1 - Scripting/Datos/informe_equipos.txt", "w", encoding="utf-8") as destino:

        destino.write("INFORME DE INVENTARIO\n")
        destino.write("=====================\n")

        for linea in origen:
            equipo = linea.strip()

            if equipo:
                contador += 1
                destino.write(f"{contador}. {equipo}\n")

        destino.write("=====================\n")
        destino.write(f"Total de equipos: {contador}\n")

print("Informe generado correctamente.")