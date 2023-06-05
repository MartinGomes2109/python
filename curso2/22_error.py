try:
    print (0 / 0)
except ZeroDivisionError as error:
    print(error)

try:
    assert 1 != 1 , 'uno no es igual que uno'
except AssertionError as error:
    print(error)
#encierra la parte del codigo que provoca el error en un bloque que lo imprime por pantalla y permite continuar con la ejecucion del resto del codigo si es posible
# se agrega el error en except y se lo asigna a una variable para podes mostrarla
try:
    age= 10
    if age < 18:
        raise Exception('no se permiten menores de eddad')
except Exception as error:
    print(error)

print('hola')