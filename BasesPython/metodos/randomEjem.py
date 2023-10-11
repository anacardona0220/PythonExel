import random

def fnRandom():
 for item in range(3):
    print('Random simple : ',random.random())
    print('Random enteros : ',random.randrange(1,5))
    print('Random float : ',random.uniform(1,10))
    print('Imprimir solo pares :', random.randrange(0,20,2))

fnRandom()
 
print('')
alumnos = ['Carlos','Ruben','ana']
print('Alumnos uno solo : ', random.choice(alumnos))
print('Alumnos solo dos : ', random.sample(alumnos, 2))

print('')
# Programa para generar contraseñas
letras = 'abcdfghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numeros = '1234567890'
simbolos = '!@#$%^&*(){\}[]'

unir = f'{letras}{numeros}{simbolos}'
longitud = 12
extension = random.sample(unir, longitud)
password = ''.join(extension)
print(password)
