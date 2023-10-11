# La función de Map de Python es una función que te permite transformar un iterable 
# completo usando otra función.

# ----------- Version tradicional --------
numbers = [1,2,3,4]
numbers_v2 = []

for i in numbers:
    numbers_v2.append(i * 2)
    
# ---------- Version map --------------------
    
numbers_v3 = list(map(lambda i: i * 2, numbers))

print(numbers)
print(numbers_v2)
print(numbers_v3)
     
# ---------- Version map Iterar dos listas --------------------
print('')
n1 =[1,2,3,4]
n2 =[5,6,7]

print(n1)
print(n2)

result = list(map(lambda a, b : a + b, n1, n2 ))
print(f'Result: {result}')

# ---------- Version map Iterar dos diccionarios --------------------
print('')
vengadores = [
  { 'nombre': "Tony",   'apellidos': "Stark" },
  { 'nombre': "Steve",  'apellidos': "Rogers" },
  { 'nombre': "Bruce",  'apellidos': "Banner" },
  { 'nombre': "Natasha",'apellidos': "Romanoff" },
  { 'nombre': "Thor",   'apellidos': "Odinson" },
  { 'nombre': "Clint",  'apellidos': "Barton" },
];

fullname = list(map(lambda vengador: f"{vengador['nombre']} {vengador['apellidos']}", vengadores))
output = "\n".join(fullname)
print(output)

# ---------- Version map Iterar dos diccionarios SOLO PRECIOS --------------------
print('')

items = [
    {
        'product': 'camisa',
        'price':100
    },
    {
        'product': 'pantalon',
        'price':200
    },
    {
        'product': 'zapatos',
        'price':300
    }
]

prices = list(map(lambda item : item['price'], items))
print(prices)

# ---------- Reto: map con inmutabilidad --------------------

def add_taxes(item):
 new_item = item.copy()
 new_item['taxes'] = new_item['price'] * .19
 return new_item

new_items = list(map(add_taxes, items))

print(items)
print(new_items)


# ---------- Reto: Multiplica todos los elementos por dos --------------------
print('')
def multiply_numbers(numbers):
    res = list(map(lambda num: num * 2, numbers))
    return res

numbers = [1, 2, 3, 4]
response = multiply_numbers(numbers)
print(response)