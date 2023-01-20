dicti ={}
for i in range(1,11):
    dicti[i]=i*2
print(dicti)

dictiv2 = {i: i * 2 for i in range(1,11)}
print(dictiv2)

import random
countries = ['col','arg','mex','bol','pe']
population = {}
for i in countries:
    population[i] = random.randint(1,100)
print(population)

populationv2 = {i: random.randint(1,100) for i in countries}
print(populationv2)

names=['nico','zule','santi']
ages = [12,56,98]
# zip es para unir 2 listas en una
#list, primero se crea la lista y despues se unen las 2 con zip
print(list(zip(names,ages)))

new_list = {names: ages for (names,ages) in zip(names,ages)}
print(new_list)