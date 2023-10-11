arreglo = ['h','o','l','a']
palabra = 'Hola'

print(arreglo)
print(arreglo[1])
print(palabra)
print("\n")

for item in arreglo:
    print(item)
    if item == 'l':
      print("Es L")
 
 
 #.append()   /  .remove()
 
vocales = ['a','e']
print(vocales)
print("\n")
vocales.append('i')
vocales.append('o')
vocales.append('u')
print(vocales)
print("\n")
vocales.remove('u')
print(vocales)

 
 #agregar desde for
 
numeros = []
print("\n")
for x in range(4):
   numeros.append(input("Agregar dato #:"+str(x + 1)))

print(numeros)