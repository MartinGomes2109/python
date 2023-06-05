for i in range(1,11):
    print(i)

my_inter = iter(range(1,11))
print(my_inter)
print(next(my_inter))
next(my_inter)
print(next(my_inter))

#iter sirve para crear un iterable manual, con el next se pasa al siguiente elemente de la iteracion manualmente, osea , se puede avanzar en cualquier momento