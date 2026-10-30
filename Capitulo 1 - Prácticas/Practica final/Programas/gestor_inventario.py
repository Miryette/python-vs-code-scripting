import csv
from pathlib import Path


DIRECTORIO_PROGRAMA = Path(__file__).resolve().parent
DIRECTORIO_CAPITULO = DIRECTORIO_PROGRAMA.parent

ARCHIVO_INVENTARIO = DIRECTORIO_CAPITULO / "datos" / "inventario_final.csv"
DIRECTORIO_INFORMES = DIRECTORIO_CAPITULO / "informes"
ARCHIVO_INFORME = DIRECTORIO_INFORMES / "informe_inventario.txt"
ARCHIVO_EQUIPOS_WINDOWS = DIRECTORIO_CAPITULO / "equipos windows"

def mostrar_equipos():
    with open(ARCHIVO_INVENTARIO, "r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)

        print()
        print("INVENTARIO DE EQUIPOS")
        print("---------------------")

        for equipo in lector:
            print(
                f"{equipo['nombre']} - "
                f"{equipo['ip']} - "
                f"{equipo['sistema']} - "
                f"{equipo['ubicacion']}"
            )


def buscar_equipo():
    nombre = input("Nombre del equipo: ")

    encontrado = False

    with open(ARCHIVO_INVENTARIO, "r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)

        for equipo in lector:
            if equipo["nombre"] == nombre:
                print()
                print("Equipo encontrado")
                print("-----------------")
                print(f"Nombre: {equipo['nombre']}")
                print(f"IP: {equipo['ip']}")
                print(f"Sistema: {equipo['sistema']}")
                print(f"Ubicación: {equipo['ubicacion']}")
                encontrado = True
                break

    if not encontrado:
        print("El equipo no existe.")

def buscar_por_ip():
    ip = input("Dirección IP del equipo: ")

    encontrado = False

    with open(ARCHIVO_INVENTARIO, mode="r", encoding="utf-8", newline="") as archivo:
      lector = csv.DictReader(archivo)

      for equipo in lector:
        if equipo["ip"] == ip:
          print()
          print("Equipo encontrado")
          print("-----------------")
          print(f"Nombre: {equipo['nombre']}")
          print(f"IP: {equipo['ip']}")
          print(f"Sistema: {equipo['sistema']}")
          print(f"Ubicación: {equipo['ubicacion']}")
          encontrado = True
          break

    if not encontrado:
      print("El equipo no existe.")

def buscar_por_ubicacion():
    ubicacion = input("Ubicación del equipo: ")

    contador = 0

    with open(ARCHIVO_INVENTARIO, "r", encoding="utf-8", newline="") as archivo:
        lector = csv.DictReader(archivo)

        for equipo in lector:
            if equipo["ubicacion"] == ubicacion:
                contador += 1

                print()
                print(f"Equipo encontrado nº {contador}")
                print("-----------------")
                print(f"Nombre: {equipo['nombre']}")
                print(f"IP: {equipo['ip']}")
                print(f"Sistema: {equipo['sistema']}")
                print(f"Ubicación: {equipo['ubicacion']}")

    if contador == 0:
        print("No existen equipos en esa ubicación.")

def añadir_equipo():
    nombre = input("Nombre: ")
    ip = input("Dirección IP: ")
    sistema = input("Sistema operativo: ")
    ubicacion = input("Ubicación: ")

    with open(
        ARCHIVO_INVENTARIO,
        "a",
        encoding="utf-8",
        newline=""
    ) as archivo:

        escritor = csv.writer(archivo)

        escritor.writerow([
            nombre,
            ip,
            sistema,
            ubicacion
        ])

    print("Equipo añadido correctamente.")

def exportar_equipos_windows():
    ARCHIVO_EQUIPOS_WINDOWS.mkdir(
        parents=True,
        exist_ok=True
    )

    with open(ARCHIVO_INVENTARIO, "r", encoding="utf-8") as origen:
        lector = csv.DictReader(origen)

        with open(
            ARCHIVO_EQUIPOS_WINDOWS / "equipos_windows.csv",
            "w",
            encoding="utf-8",
            newline=""
        ) as destino:

            escritor = csv.writer(destino)

            escritor.writerow(["nombre", "ip", "sistema", "ubicacion"])

            for equipo in lector:
                if equipo["sistema"] == "Windows 11":
                    escritor.writerow([
                        equipo["nombre"],
                        equipo["ip"],
                        equipo["sistema"],
                        equipo["ubicacion"]
                    ])
        print("Informe de equipos Windows generado correctamente")


def generar_informe():
    DIRECTORIO_INFORMES.mkdir(
        parents=True,
        exist_ok=True
    )

    contador = 0

    with open(ARCHIVO_INVENTARIO, "r", encoding="utf-8") as origen:
        lector = csv.DictReader(origen)

        with open(ARCHIVO_INFORME, "w", encoding="utf-8") as destino:

            destino.write("INFORME DE INVENTARIO\n")
            destino.write("=====================\n\n")

            for equipo in lector:
                contador += 1

                destino.write(
                    f"{contador}. "
                    f"{equipo['nombre']} - "
                    f"{equipo['ip']} - "
                    f"{equipo['sistema']} - "
                    f"{equipo['ubicacion']}\n"
                )

            destino.write("\n")
            destino.write("=====================\n")
            destino.write(f"Total de equipos: {contador}\n")

    print("Informe generado correctamente.")


while True:

    print()
    print("================================")
    print("   GESTOR DE INVENTARIO")
    print("================================")
    print()
    print("1. Mostrar todos los equipos")
    print("2. Buscar por nombre")
    print("3. Buscar por IP")
    print("4. Buscar por ubicación")
    print("5. Añadir un equipo")
    print("6. Exportar equipos Windows")
    print("7. Generar informe")
    print("8. Salir")
    print()

    opcion = input("Selecciona una opción: ")
    
    if opcion == "1":
        mostrar_equipos()

    elif opcion == "2":
        buscar_equipo()

    elif opcion == "3":
        buscar_por_ip()

    elif opcion == "4":
        buscar_por_ubicacion()

    elif opcion == "5":
        añadir_equipo()

    elif opcion == "6":
        exportar_equipos_windows()

    elif opcion == "7":
        generar_informe()

    elif opcion == "8":
        print("Programa finalizado.")
        break

    else:
        print("Opción incorrecta.")