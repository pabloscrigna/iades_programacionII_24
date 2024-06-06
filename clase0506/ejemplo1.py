"""

modo: r: lectura (read)
      w: escritura (write)
      a: agregar (append)

"""


archivo = open('texto', 'r+')
foo = archivo.read()
archivo.write("\nqwerty")
archivo.close()

print("contenido del archivo")
print(foo)

# Da error el archivo ya esta cerrado
# bar = archivo.read()
# print(bar)

