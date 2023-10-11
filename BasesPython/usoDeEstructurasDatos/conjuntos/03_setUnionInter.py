# ------------Union ---------------
set_a = {'Col', 'Perù', 'Chi'}
set_b = {'Chi', 'Bra'}

# ------------Interseccion ---------------
set_c = set_a.union(set_b)
print(set_c)
print(set_a | set_b)
set_d = set_a.intersection(set_b)
print(set_d)
print(set_a & set_b)
# ------------Diferencia ---------------

set_diferencia = set_a.difference(set_b)
print(set_diferencia)
# ------------ symetric_difeference ---------------
set_symetric = set_a.symmetric_difference(set_b)
print(set_symetric)
print(set_a ^ set_b)