# tipo o estructura de datos que permite almacenar datos 
# de una manera muy parecida a las listas, con la salvedad 
# de que son inmutables. no pueden ser modificadas una vez declaradas,


tupla = (1, 2, 3)
print(tupla) #1 ,2 ,3 

tupla = (1, 2, 3)
#tupla[0] = 5 # Error! TypeError

# -------  Al igual que las listas, las tuplas también pueden ser anidadas.

tupla = 1, 2, ('a', 'b'), 3
print(tupla)       #(1, 2, ('a', 'b'), 3)
print(tupla[2][0]) #a


# Y también es posible convertir una lista en tupla haciendo uso de al función tuple().
lista = [1, 2, 3]
tupla = tuple(lista)
print(type(tupla)) #<class 'tuple'>
print(tupla)       #(1, 2, 3)

# Se puede iterar una tupla de la misma forma que se hacía con las listas.
tupla = [1, 2, 3]
for t in tupla:
    print(t) #1, 2, 3
    
    
# Y se puede también asignar el valor de una tupla con n elementos a n variables.

l = (1, 2, 3)
x, y, z = l
print(x, y, z) #1 2 3

# -------------  Métodos tuplas  -------------------

# count(<obj>)
# El método count() cuenta el número de veces que el objeto pasado como parámetro se ha encontrado en la lista.

l = [1, 1, 1, 3, 5]
print(l.count(1)) #3

# index(<obj>[,index])
# El método index() busca el objeto que se le pasa como parámetro y devuelve el índice en el que se ha encontrado.

l = [7, 7, 7, 3, 5]
print(l.index(5)) #4

# En el caso de no encontrarse, se devuelve un ValueError.

l = [7, 7, 7, 3, 5]
#print(l.index(35)) #Error! ValueError

# El método index() también acepta un segundo parámetro opcional, que indica a partir de que índice empezar a buscar el objeto.

l = [7, 7, 7, 3, 5]
print(l.index(7, 2)) #2