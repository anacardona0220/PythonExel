set_countries = {'Col','Mex','Chi','Bol'}
print(set_countries)
print(type(set_countries))

# size del conjunto
print(len(set_countries))

# add element
set_countries.add('Ecua')
print(set_countries)

# update element
set_countries.update({'ar', 'bra', 'Ecua'})
print(set_countries)

# delete element
set_countries.remove('ar')
print(set_countries)

set_countries.discard('arg')# por si no esta
print(set_countries)

set_countries.clear()
print(set_countries)
