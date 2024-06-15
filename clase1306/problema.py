"""

$ python3 problema.py apellido dni

$python3 problema.py perez 34566788


1. Leer esos argumentos que me pasaron por comando 
2. Guardamos apellido y dni en un diccionario
3. Agregar la fecha y hora de la registracion
"""
import json
import sys

from datetime import datetime, timezone


print("Bienvenidos al registro de ")


print(sys.argv)

invitados = []     # array    
invitado = {}      # object

with open('invitados.json', 'r') as archivo:
    invitados = json.load(archivo)

print(invitados)

invitado["apellido"] = sys.argv[1]
invitado["dni"] = sys.argv[2]
invitado["fecha"] = datetime.now(timezone.utc)
# invitado["fecha"] = datetime.now()

print("invitado python")
print(invitado)

print("invitado json")
invitado["fecha"] = invitado["fecha"].isoformat()
print(invitado)

invitados.append(invitado)

with open("invitados.json", 'w') as archivo:
    json.dump(invitados, archivo, indent=4)    


fecha_antigua = invitados[0]["fecha"]
fecha_antigua_dt = datetime.fromisoformat(fecha_antigua)
invitado_antiguo = invitados[0]


for registro in invitados:
    fecha_actual_dt = datetime.fromisoformat(registro["fecha"])
    if fecha_actual_dt < fecha_antigua_dt:
        fecha_antigua_dt = fecha_actual_dt
        invitado_antiguo = registro 


print("el invitado mas antigiuo es:")
print(invitado_antiguo)







