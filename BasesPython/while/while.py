# Imprime i siempre que i sea menor que 6:
i = 1
while i < 6:
  print(i)
  i += 1
print('--- Break---\n')
# Con la sentencia break podemos detener el bucle 
# incluso si la condición while es verdadera:
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

print('--- continue (Detener y seguir despues...)---\n')
# Con la sentencia continue podemos detener la iteración actual 
# y continuar con la siguiente:
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

print('--- continue (else)---\n')
# Con la sentencia else podemos ejecutar un bloque de código 
# una vez cuando la condición deja de ser cierta:
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")