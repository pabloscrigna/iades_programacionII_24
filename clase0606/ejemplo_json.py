import json

empleados = []

empleado = {
    "nombre": "juan",
    "dni": 4567890,
    "salario": 500000,
    "estado": True
}


empleados.append(empleado)

empleado = {
    "nombre": "maria",
    "dni": 8567890,
    "salario": 600000,
    "estado": False
}

empleados.append(empleado)

print("string json empleados")
empleados_json = json.dumps(empleados)
print(f"string json empleado: {empleados_json}")

with open('empleados.txt', 'w') as archivo:
    json.dump(empleados, archivo, indent=4)


with open('empleados.txt', 'r') as archivo:
    empleados = json.load(archivo)

# print(empleados)
# print(type(empleados))

print("Imprimir empleados activos")
for empleado in empleados:
    if empleado.get("estado") == True:
        print(empleado)



