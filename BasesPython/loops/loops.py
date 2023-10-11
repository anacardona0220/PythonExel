# https://www.mclibre.org/consultar/python/lecciones/python-for-2.html

matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]

print(matriz[0][2],"\n")

for element in matriz:
    print(element)
    for item in element:
        print(item)
     
 
print('--- Ejemplo de bucle anidado (variables independientes)---\n')
 
for i in [0, 1, 2]:
    for j in [0, 1]:
        print(f"i vale {i} y j vale {j}")
        
print('\n')
for i in range(3):
    for j in range(2):
        print(f"i vale {i} y j vale {j}")

print('--- Ejemplo de sangrado en bucle anidado (1)---\n')
for i in [1, 2, 3]:
    for j in [11, 12]:
        print(j, end=" ")
        print(i, end=" ")
        
print('\n')

print('--- Ejemplo de sangrado en bucle anidado (3) ---\n')
for i in [1, 2, 3]:
    for j in [11, 12]:
        print(j, end=" ")
print(i, end=" ")
print('\n')

# En Python se puede incluso utilizar la misma variable 
# en los dos bucles anidados porque Python asigna el valor 
# que corresponde a la variable de control cada vez que se 
# ejecuta el cuerpo de un bucle. Por ejemplo:


print('--- Ejemplo misma variable ---\n')
for i in range(1, 4):
    print(f"i vale {i}")
    for i in range(11, 13):
        print(f"  i  vale {i}")
        
        
print('\n')
print('--- Ejemplo de bucle anidado (variables dependientes) 1 ---\n')
for i in [1, 2, 3]:
    for j in range(i):
        print(f"i vale {i} y j vale {j}")