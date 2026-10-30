contador = 0

with open("Capitulo 1 - Prácticas/13. Práctica propuesta/Datos/usuarios.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        usuario = linea.strip()
        print(f"Usuario: {usuario}")

        if usuario:
            contador += 1

print(f"\nNúmero de usuarios: {contador}")
