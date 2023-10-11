import datetime

tiempo = datetime.datetime.now()

print(tiempo.year)
print(tiempo.month)
print(tiempo.day)
print(tiempo.second)

# ordenar informacion

print("Dia {} Mes {} Año {}".format(tiempo.day, tiempo.month, tiempo.year))

