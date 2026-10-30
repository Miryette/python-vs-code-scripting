from pathlib import Path

directorio_programa = Path(__file__).resolve().parent
directorio_capitulo = directorio_programa.parent

ruta_equipos = directorio_capitulo / "datos" / "equipos.txt"

with open(ruta_equipos, "r", encoding="utf-8") as archivo:
    for linea in archivo:
        equipo = linea.strip()

        if equipo:
            print(equipo)