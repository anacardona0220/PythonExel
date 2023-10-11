# Existen dos formas de llamar funciones

# # mètodo 1:
# import fuciones
# fuciones.media
# fuciones.dicPersona

# # mètodo 2:

from fuciones import media, dicPersona

# Crear diccionario

dicionarioPersona = dict()

a = dicPersona(dicionarioPersona, 'Carlos', 'Montoya', 44 )
print('Nombre :', a['nom'], 'Apellido:', a['ape'],  'y la edad es :', a['edad'])



num1 = 8
num2 = 9

med = media(num1, num2)
print('La media de {} y de {} es : {}'.format(num1, num2, med))