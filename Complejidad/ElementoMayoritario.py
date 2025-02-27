import random, time

numeros = [random.randint(1, 100) for _ in range(100)]
print('Array desordenado: ', numeros)

# FORMA SUMAMENTE INEFICIENTE DE ENCONTRAR EL ELEMENTO MAYORITARIO
# contMayoritario = 0
# valorMayoritario = 0
# for numero in numeros:
#     contAux = 0
#     aux = numero
#     for numero in numeros:
#         if (aux == numero):
#             contAux += 1
#     if (contAux > contMayoritario):
#         valorMayoritario = aux
#         contMayoritario = contAux
# print(f'El elemento mayoritario es {valorMayoritario} y se repitio {contMayoritario} veces')

# DECORADORES PARA CALCULAR EL TIEMPO DE EJECUCION
def calcular_tiempo_de_ejecucion(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        resultado = func(*args, **kwargs)
        end_time = time.time()
        print(f"Tiempo de ejecución de '{func.__name__}': {end_time - start_time} segundos")
        return resultado
    return wrapper

@calcular_tiempo_de_ejecucion
def elementoMayoritarioMenosEficiente():
    contMayoritario = 0
    valorMayoritario = 0
    for numero in numeros:
        contAux = 0
        aux = numero
        for numero in numeros:
            if (aux == numero):
                contAux += 1
        if (contAux > contMayoritario):
            valorMayoritario = aux
            contMayoritario = contAux
    print(f'El elemento mayoritario es {valorMayoritario} y se repitio {contMayoritario} veces')

elementoMayoritarioMenosEficiente()

# ORDENAMIENTO BURBUJA
def bubble_sort(arr):
    n = len(arr)
    # Iterar sobre todos los elementos del array
    for i in range(n):
        # Últimos i elementos ya están en su lugar correcto
        for j in range(0, n-i-1):
            # Intercambiar si el elemento encontrado es mayor que el siguiente elemento
            if arr[j] > arr[j+1]:
                aux = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = aux

@calcular_tiempo_de_ejecucion
def elementoMayoritario():
    bubble_sort(numeros)
    print("Array ordenado:", numeros)
    contMayoritario = 0
    valorMayoritario = 0
    for numero in numeros:
        contAux = 0
        aux = numero
        for numero in numeros:
            if (aux == numero):
                contAux += 1
        if (contAux > contMayoritario):
            valorMayoritario = aux
            contMayoritario = contAux
    print(f'El elemento mayoritario es {valorMayoritario} y se repitio {contMayoritario} veces')

elementoMayoritario()