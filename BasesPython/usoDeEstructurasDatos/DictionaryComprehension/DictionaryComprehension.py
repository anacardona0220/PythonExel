import random


contactos = {
    'Juan': '555-1234',
    'María': '555-5678',
    'Carlos': '555-9876'
}

productos = {
    'manzanas': 0.5,
    'plátanos': 0.25,
    'naranjas': 0.75
}


calificaciones = {
    'Juan': 90,
    'María': 95,
    'Carlos': 87
}

configuracion = {
    'modo': 'desarrollo',
    'líneas': 80,
    'tema': 'oscuro'
}

coordenadas = {
    'ciudad1': (40.7128, -74.0060),
    'ciudad2': (51.5074, -0.1278),
    'ciudad3': (35.6895, 139.6917)
}





dic = {}
for item in range(1 , 5):
    dic[item] = item  * 2
    
print(dic)
# -----------------------------------------------------
dic_v2 = {i: i * 2 for i in range(1, 4)}
print(dic_v2)

# -----------------------------------------------------
dic_v3 = {i: i * 2 for i in range(1, 4)}
print(dic_v3)

# -----------------------------------------------------
countries = ['Col','Mex','Chi','Bol']

population = {}

for country in countries:
    population[country] = random.randint(1, 100)

print(population)
# ------------------ population_v2 ---------------------

population_v2 = {country: random.randint(1,50) for country in countries}
print(population_v2)


# ------------------ Iterar dos listas ---------------------

names = ['Carlos', 'Andrea', 'Juanma', 'Joel']
ages = [44, 43, 18, 14]

new_dic = { name: age for (name, age) in zip(names, ages) }
print(new_dic)



# ------------------ Con condicionales ---------------------

population_v3Confitional = { country: population for (country, population) in population_v2.items() if population > 20}
print('')
print(population_v3Confitional)


# ------------------ Con condicionales  dic de texto ---------------------

texto = 'Hola soy Carlos alfredo'

unique = { c: c.upper() for c in texto if c in 'aeiou' }
print(unique)