# for item in range(3):
#   print(f"valor de i : { item}")

# print("\n")

# for item in range(-2,1):
#   print(f"valor de i : { item}")

# print("\n")

# for item in range(2,11, 2):
#   print(f"valor de i : { item}")

# print("\n")

# for item in range(5,1, -2):
#   print(f"valor de i : { item}")


# print("---- Tablas de multiplicar ---- \n")


#  #-------- Ingresar datos con input()-----------
# print("\n")
# num = input("Ingrese el numero de la tabla :")

# res = 0
# for item in range(1, 11):
#   res = int(num) * item
#   print(f"{ num } X { item }  = {res}")


print("--- Recorrer array ---\n")

my_array = [6, 2, 4]

for item in my_array:
    print(item)

print("--- Recorrer tuple ---\n")

my_tuple = {'a', 'r', 'd'}

for item in my_tuple:
    print(item)


print("--- Recorrer diccionary ---\n")

product = {

    'nombre': 'Carlos',
    'apellido': 'Montoya',
    'edad': 44

}

for item in product:
    print(item, '=>', product[item])

print("\n")

for key, value in product.items():
    print(key, '=>', value)

print("\n")

people = [
    {
        'nombre': 'Carlos',
        'apellido': 'Montoya',
        'edad': 44
    },
    
    {
        'nombre': 'Andrea',
        'apellido': 'Montoya',
        'edad': 43
    },
    {
        'nombre': 'Juan',
        'apellido': 'Montoya',
        'edad': 18
    },
    
]

for person in people:
  print ('Nombre = ', person['nombre'])
  print ('Apellido = ', person['apellido'])
  print ('Edad = ', person['edad'])
  print ('\n')
  
  
  print("--- Recorrer string ---\n")
cadena = "Carlos"

# Método 1, sin índice
for caracter in cadena:
    print(caracter)
    
cadena = "Alfredo"

# Método 2, con índice
for indice in range(len(cadena)):
    caracter = cadena[indice]
    print("En el índice {} tenemos a '{}'".format(indice, caracter))