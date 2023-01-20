set_countries = {'argentina', 'colombia', 'mexico'}
print(set_countries)
print(type(set_countries))

set_numbre={1,2,3,4}
print(set_numbre)
print(type(set_numbre))

set_types = {1,'hola', False, 12.12}
print(set_types)
print(type(set_types))

#dividir el conjuntos en sus elementos no repetidos
#desordenado
set_from_string=set('hooola')
print(set_from_string)

set_from_tuples=set(('abc','cbv','mdj','kjf','abc'))
print(set_from_tuples)

numbers= [1,2,3,4,1,2,3]
set_numbers=set(numbers)
print(set_numbers)
unique_numbers=list(set_numbers)
print(unique_numbers)