import random
countries = ['Mex','Arg','Col','Pe']

population_v2 = {i: random.randint(1,100) for i in countries}
print(population_v2)

resultado = { c: population for (c,population) in population_v2.items() if population > 50}
print(resultado)

text = "Hola, como estas, buen dia"
vocal = {carac: carac.upper() for carac in text if carac in 'aeiou'}
print(vocal)