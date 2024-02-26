set_countries = {'col','mex','bol'}

size = len(set_countries)
print(size)

print('col' in set_countries)

#add 
set_countries.add('per')
print(set_countries)
size = len(set_countries)
print(size)

#update
set_countries.update({'arg','ecu','per'})
print(set_countries)

# remove

set_countries.remove( 'col')
print(set_countries)
