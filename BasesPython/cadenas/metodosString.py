text = "Este es un texto de ejemplo"
print(text.split())
print(text.split(" "))
print()
animales = "perro, gato, ratón, caballo"
 
print(animales.split(" " ))
print(animales.split(", " ))

print()
animales = "perro, gato, ratón, caballo"
print(animales.split("a")) 
print(animales.split("a", 1))

#----------  find()  rfind() ----------------------
cadenaDeTexto = "Es quien peor cometer una injusticia que padecerla porque quien la comete se convierte en injusto y quien la padece no."
cadenaDeTexto.find('quien')
#52
cadenaDeTexto.rfind('quien')
print()
#94
print(cadenaDeTexto.find('quien'))   # first match
print(cadenaDeTexto.rfind('quien'))  # last match

#----------  str.join(iterable) ----------------------
print()
print("----------  str.join(iterable) ----------------------")
print("\n:".join(["freeCodeCamp", "es", "divertido"]))
print(" y ".join(["A", "B", "C"]))
print(" ".join("freeCodeCamp"))

listChar = ['p','r','o','g','r','a','m']  
print("".join(listChar))
test = {'2', '1', '3'}
s = ', '
print(s.join(test))
#----------  replace ----------------------

print()
print("----------  replace ----------------------")
string = "Esto es bonito. Esto es bueno."
newString = string.replace("es","FUE")
print(newString)
string2 = "Para mi esto es bonito. Esto es bueno."
nuevoString2 = string2.replace("es","FUE", 2)
print(nuevoString2)

#----------  string strip eliminar espacios  ----------------------

print()
string = '   Hola, Mundo!    '
print(string.lstrip())
print(string.rstrip())
print(string.strip())
 
#----------  string split dividir  ----------------------
 
print()
string = "freeCodeCamp is fun."
print(string.split(" "))
string = "freeCodeCamp, es divertido, y informativo"
print(string.split(","))
string = "freeCodeCamp es divertido y informativo"
print(string.split())
string = "freeCodeCamp        es     divertido y    informativo"
print(string.split())
string = "freeCodeCamp es divertido y informativo"
print(string.split(" ", 2))


#----------  string reverse  ----------------------

str = "LearnPython"

reversed_string=''.join(reversed(str))

print("The Reversed String is", str.join(reversed()))  