number = []

for item in range(1, 11):
    number.append(item * 2)

print(number)

number_v2 = [element * 2 for element in range(1, 11)]
print(number_v2)


evenNumber = [i * 2 for i in range(1, 11) if i % 2 == 0]
print(evenNumber)

# --------------- Ejercicio crear list comprehension -------------

numbers = [35, 16, 10, 34, 37, 25]

even_number = []
for num in numbers:
    if num % 2 == 0:
        even_number.append(num)
print('')
print(even_number)
        
even_numberb = [num for num in numbers if num % 2 == 0]
print(even_numberb)
    
