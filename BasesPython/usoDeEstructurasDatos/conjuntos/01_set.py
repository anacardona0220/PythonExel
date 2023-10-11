# un conjunto es una colección desordenada de elementos 
# que no se repiten. 
# Puede agregar y eliminar elementos de un conjunto; por lo tanto, 
# el conjunto es un colección mutable. Puede contener elementos de 
# diferentes tipos de datos.

set_countries = {'Col','Mex','Chi','Bol'}
print(set_countries)
print(type(set_countries))

setNumber = {1,4,7,9}
print(setNumber)

setTypes = { 1, 'Hola', True, 4.5, False}
print(setTypes)

setString = set('Hola')
print(setString)

setFromTuplas = set(('abc', 'bcd', 'cde', 'abc'))
print(setFromTuplas)


numbers = [1,2,2,3,5,4,6,6,5,5,4,8,7,0]
setNumeros = set(numbers)
print(setNumeros)
# Regrerar los datos a lista
aLista = list(setNumeros)
print(aLista)

# A diferencia de las listas, en los set no podemos modificar 
# un elemento a través de su índice. Si lo intentamos, tendremos un TypeError.

s = set([5, 6, 7, 8])
#s[0] = 3 #Error! TypeError

lista = ["Perú", "Argentina"]
#s = set(["México", "España", lista]) #Error! TypeError

s = set([1, 2, 2, 3, 4])
print(len(s)) #4

# También podemos saber si un elemento está presente en un set con el operador in. 
# Se el valor existe en el set, se devolverá True.
s = set(["Guitarra", "Bajo"])
print("Guitarra" in s) #True


# Los sets tienen además diferentes funcionalidades, que se pueden aplicar en forma de 
# operador o de método. Por ejemplo, el operador | nos permite realizar la unión de dos sets, 
# lo que equivale a juntarlos. El equivalente es el método union() que vemos a continuación.

s1 = set([1, 2, 3])
s2 = set([3, 4, 5])
print(s1 | s2) #{1, 2, 3, 4, 5}


# -----------  Métodos sets   ---------------
# s.add(<elem>)
# El método add() permite añadir un elemento al set.

l = set([1, 2])
l.add(3)
print(l) #{1, 2, 3}
# s.remove(<elem>)
# El método remove() elimina el elemento que se pasa como parámetro. 
# Si no se encuentra, se lanza la excepción KeyError.

s = set([1, 2])
s.remove(2)
print(s) #{1}
# s.discard(<elem>)
# El método discard() es muy parecido al remove(), borra el elemento que se pasa como parámetro, 
# y si no se encuentra no hace nada.

s = set([1, 2])
s.discard(3)
print(s) #{1, 2}
s.pop()
# El método pop() elimina un elemento aleatorio del set.

s = set([1, 2])
s.pop()
print(s) #{2}
s.clear()
# El método clear() elimina todos los elementos de set.

s = set([1, 2])
s.clear()
print(s) #set()
# -------------------  Otros ----------------------------
# Los sets cuentan con una gran cantidad de métodos que permiten realizar 
# operaciones con dos o más, como la unión o la intersección.

# Podemos calcular la unión entre dos sets usando el método union(). 
# Esta operación representa la “mezcla” de ambos sets. Nótese que el 
# método puede ser llamado con más parámetros de entrada, y su resultado 
# será la unión de todos los sets.

s1 = {1, 2, 3}
s2 = {3, 4, 5}
print(s1.union(s2)) #{1, 2, 3, 4, 5}
# También podemos calcular la intersección entre dos o más set. 
# Su resultado serán aquellos elementos que pertenecen a ambos sets.

s1 = {1, 2, 3}
s2 = {3, 4, 5}
print(s1.intersection(s2)) #{3}
# Los set en Python tiene gran cantidad de métodos, por lo que 
# lo dejaremos para otro capítulo, pero aquí os dejamos con un listado de ellos:

# s1.union(s2[, s3 ...])
# s1.intersection(s2[, s3 ...])
# s1.difference(s2[, s3 ...])
# s1.symmetric_difference(s2)
# s1.isdisjoint(s2)
# s1.issubset(s2)
# s1.issuperset(s2)
# s1.update(s2[, s3 ...])
# s1.intersection_update(s2[, s3 ...])
# s1.difference_update(s2[, s3 ...])
# s1.symmetric_difference_update(s2)