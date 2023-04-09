import sys
print(sys.path)
#muestra la ruta del archivo y otros datos del sistema

import re
# re = expresion regular
test = 'mi 1numero1 es 232 543 876, el 1codigo22 de mi pais 54, mi numero favorito 4'
result = re.findall('[0-9]+',test)
# re.findall  => encuenta en la variable todos los string con las caracteristicas de la expresion regular en este caso todos los numeros de la variable, con el + junta los numeros de sus string, sin el + divide individualmente los numeros de sus strings
print(result)

import time
timestamp = time.time()
#muestra la hora de la maquina pero en el formato que utiliza la maquina para horientarse, para pasar al formato normal hay que hace una transformacion con time.localtime
print(timestamp)
local = time.localtime()
result2 = time.asctime(local)
print(result2)
#resultado final de la transformacion, no tira la hora de la pc, tira la hora del servidor donde se este ejecutando python

import collections
numbers = [1,1,2,3,4,4,5,6,7,8,8,8,9,9,9,9,'a','a',2,2,'b','b','ccc','e']
contador = collections.Counter(numbers)
print(contador)
# collections.counter funciona para mostrar la cantidad de veces qque se repite el string en la lista