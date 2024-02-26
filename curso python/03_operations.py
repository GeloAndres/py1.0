set_a = {'col', 'mex', 'bol'}
set_b = {'per', 'bol'}

set_c = set_a.union(set_b)
print(set_c)
print(set_a | set_b)

#Intersection
set_c = set_a.intersection(set_b)
print(set_c)
print(set_a & set_b)

#Difference, quitar el cojunto de "B" en "A"
set_c = set_a.difference(set_b)
print(set_c)
print(set_a - set_b)

#diferencia simetrica, sacar los elementos en comun

set_c = set_a.symmetric_difference(set_b)
print(set_c)
print(set_a ^ set_b)

##como las tablas de mysql, los JOIN