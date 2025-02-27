#220 284
num1 = int(input('ingrese numero: '))
array = [] 
num2 = 0
aux = num1
for i in range(1,3):
    array = [i for i in range(1,aux + 1) if aux % i == 0]
    ult_elem = array.index(aux)
    sum_array = 0
    for j in range(ult_elem):
        sum_array = sum_array + array[j]
    num2 = aux
    aux = sum_array
if num1 == aux :
    print(num1,' y ',num2,' son numeros amigos')
    print('o numeros sociables de periodo 2')
else:
    print(num1,' no es numero amigo o sociable')