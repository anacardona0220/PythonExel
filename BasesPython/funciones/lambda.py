# Version py lambda x, y: x + y
# version javascript (x, y) => x + y


# function tradicional 

def increment(a):
 return a * 2

print(increment(3))

# ----- Version lambda ----------

increment_v2 =  lambda a : a * 4

print(increment_v2(5))


# ----- lambda dos argumentos ----------

full_name = lambda name, lastName : f'My name is { name.title() } {lastName.title()}'
print(full_name('carlos', 'montoya'))