"""

read
readlineas
readline

"""

with open('cuento.txt', 'r') as archivo:
    texto = archivo.read() 

print("funcion read")
print(texto)


with open('cuento.txt', 'r') as archivo:
    lineas = archivo.readlines() 

print("funcion readlines")
print(lineas)
for linea in lineas:
    print(linea) 

print("funcion readline")
with open('cuento.txt', 'r') as archivo:
    linea = archivo.readline() 
    print("funcion readline")
    print(linea)
    linea = archivo.readline()
    print(linea)




