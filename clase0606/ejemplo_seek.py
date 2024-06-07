"""
0 1 2 3 4 5 6 
*
"""

with open('numeros.txt') as archivo:
    posicion = archivo.tell()
    caracter = archivo.read(1)
    print(f"caracter: {caracter} -- posicion: {posicion}")

    posicion = archivo.tell()
    caracter = archivo.read(1)
    print(f"caracter: {caracter} -- posicion: {posicion}")

    posicion = archivo.tell()
    caracter = archivo.read(1)
    print(f"caracter: {caracter} -- posicion: {posicion}")

    print("******")
    print("vuelvo al inicio del archivo")
    print("******")
    archivo.seek(0)

    posicion = archivo.tell()
    caracter = archivo.read(1)
    print(f"caracter: {caracter} -- posicion: {posicion}")

    posicion = archivo.tell()
    caracter = archivo.read(1)
    print(f"caracter: {caracter} -- posicion: {posicion}")

    posicion = archivo.tell()
    caracter = archivo.read(1)
    print(f"caracter: {caracter} -- posicion: {posicion}")

    print("******")
    print("voy a la posicion 3")
    print("******")
    archivo.seek(3)

    posicion = archivo.tell()
    caracter = archivo.read(1)
    print(f"caracter: {caracter} -- posicion: {posicion}")

    posicion = archivo.tell()
    caracter = archivo.read(1)
    print(f"caracter: {caracter} -- posicion: {posicion}")

    posicion = archivo.tell()
    caracter = archivo.read(1)
    print(f"caracter: {caracter} -- posicion: {posicion}")



