def saludo(nombre):
    print(f"Hola {nombre}")


saludo("Timmy")
saludo("Kristy")
saludo("Jackie")
saludo("Liv")
print('')


def nombre_y_edad(nombre, edad):
    print(f"Soy {nombre} y tengo{edad} años!")


def saludo(nombre):
    print("Hola " + nombre)


def saludo(nombre):
    print(f"Hola {nombre}")


saludo("Timmy")
# Resultado
# Hola Timmy


# función definida con dos parámetros:
def saludo(primer_nombre, apellido):
    print(f"Hola, {primer_nombre} {apellido}")


def saludo(primer_nombre, apellido):
    print(f"Hola, {primer_nombre} {apellido}")


saludo("Timmy", 'App')

# Cada "key" o clave, coincide con cada parámetro en la definición de la función.
# Explícitamente llamando el nombre de los parámetros y los valores que toma,
# ayuda a evitar posibles confusiones.


def fav_lenguaje(nombre, lenguaje):
    print(
        f"Hola, soy {nombre} y mi lenguaje de programación favorito es {lenguaje}")


fav_lenguaje(nombre="Dionysia", lenguaje="Python")
# Resultado:
# Hola, Soy Dionysia y mi lenguaje de programación favorito es Python


def calcula(a, b, op):

    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError('Los argumentos deben ser números.')
    if op == 'd' and b == 0:
        raise ZeroDivisionError('No puedes dividir por cero.')

    oper = {
        's': '+',
        'r': '-',
        'm': 'x',
        'd': '/'
    }

    operaciones = {
        's': a + b,
        'r': a - b,
        'm': a * b,
        'd': a / b,
    }

    
    result = operaciones[op]
    print(f'El resultado de {a} {oper[op]}  {b} es : {result}')


calcula(6,2,'d')

# ----------------- return -------------------------

def sumRange(a, b):
    sum = 0
    for item in range(a, b):
        sum += item
    return sum

print('')
result = sumRange(1, 10)
print(result)
result_2 = sumRange(result, result + 5)
print(result_2)
    
# ----------------- return multiples resultados -------------------------
print('')
def find_volume(length= 1, width= 1, depth= 1):
    return length * width * depth, width, 'Hola!!!'
    
result = find_volume(width=10) 
print(result) 
result2, width, text = find_volume( width=10)

print(result2)
print(width)
print(text)