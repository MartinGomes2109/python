import random, time


num1 = int(input('ingrese cantidad de numeros distintos: '))
num2 = int(input('ingrese cantidad de numeros en el arreglo: '))
numeros = [random.randint(1, num1) for _ in range(num2)]

def calcular_tiempo_de_ejecucion(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        resultado = func(*args, **kwargs)
        end_time = time.time()
        print(f"Tiempo de ejecución de '{func.__name__}': {end_time - start_time} segundos")
        return resultado
    return wrapper

@calcular_tiempo_de_ejecucion
def elementoMayoritario():
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

# ORDENAMIENTO BURBUJA
#def ordenamiento(arr):
#    n = len(arr)
#    for i in range(n):
#        for j in range(0, n-i-1):
#            if arr[j] > arr[j+1]:
#                aux = arr[j]
#                arr[j] = arr[j+1]
#                arr[j+1] = aux

def run():   
    print('Array desordenado: ', numeros)
    elementoMayoritario()
#    ordenamiento()
#    print("Array ordenado:", numeros)

if __name__ == '__main__':
    run()