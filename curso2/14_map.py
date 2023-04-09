numbers = [1,2,3,4]
numbers2 = []
for i in numbers:
    numbers2.append(i * 2)

print(numbers)
print(numbers2)

numbers3 = list(map(lambda i: i * 3, numbers))
print(numbers3)

##iteracion entre 2 listas de distinto tamaño
##la lista resultante siempre es del tamañao de la lista mas pequeña
##se excluyen los elementos restantes de la lista mas grande

numbers4 = [5,6,7,8]
numbers5 = [2,3,4]

numbers6 = list(map(lambda x, y: x + y, numbers4, numbers5))
print(numbers4)
print(numbers5)
print(numbers6)