text = 'hola, como estas, buen dia'
vocal = {c: text.count(c) for c in text if c in 'aeiou'}
print(vocal)
#text.count para contar cuantas veces aparece en el tecto la variable