

# archivo = open('texto', 'r')
# archivo.read()


print("Comienzo y codigo de mi programa")

with open('texto', 'r+') as archivo:
    texto = archivo.read()
    archivo.write("Hola!")
    archivo.write("Chau!")

print(texto)
print("sigue mi programa")

