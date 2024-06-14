from datetime import datetime, timezone
from time import sleep

# Fecha y Hora

fecha_hora = datetime.now()

print(fecha_hora)

fecha_hora_utc_1 = datetime.now(timezone.utc)

sleep(1)

fecha_hora_utc_2 = datetime.now(timezone.utc)


print(fecha_hora_utc_1)
print(fecha_hora_utc_2)
print(f"type: {type(fecha_hora_utc_1)}")
print(f"diferencia: {fecha_hora_utc_2 - fecha_hora_utc_1}")

fecha_hora_1_iso = fecha_hora_utc_1.isoformat() 

print(f"iso 8601: {fecha_hora_1_iso}  -- type: {type(fecha_hora_1_iso)}")


fecha_hora_dt = datetime.fromisoformat(fecha_hora_1_iso)


print(f"fecha hora datetime: {fecha_hora_dt} -- type: {type(fecha_hora_dt)} ")

