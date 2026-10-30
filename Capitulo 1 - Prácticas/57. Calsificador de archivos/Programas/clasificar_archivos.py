from pathlib import Path

carpeta = Path("../datos")

for archivo in carpeta.interdir():
    print(archivo.name)