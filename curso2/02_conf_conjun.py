set_countries = {'col', 'mex', 'bol'}

tamaño = len(set_countries)
print(tamaño)

print('col' in set_countries)
print('pe' in set_countries)

#add agregar un elemento
set_countries.add('pe')
print(set_countries)
set_countries.add('pe')
print(set_countries)

#update agregar conjunto
set_countries.update({'arg','ecu','pe'})
print(set_countries)

#remove
set_countries.remove('mex')
set_countries.discard('mex')
#con discard si no existe no hace nada
print(set_countries)
set_countries.clear()
print(set_countries)
