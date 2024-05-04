#from decorators import delta_time
import time, random

#@delta_time('GRUPO N8')
#def sociables(n):
num = [random.randint(1, 10) for _ in range(100)]

def calcular_tiempo_de_ejecucion(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        resultado = func(*args, **kwargs)
        end_time = time.time()
        print(f"Tiempo de ejecución de '{func.__name__}': {end_time - start_time} segundos")
        return resultado
    return wrapper

@calcular_tiempo_de_ejecucion
def mostFrequentElement(X, n):
    H = {}
    maxFreq = 1
    mostFrequent = -1
    for i in range(n):
        if X[i] in H:
            H[X[i]] = H[X[i]] + 1
            if maxFreq < H[X[i]]:
                maxFreq = H[X[i]]
                mostFrequent = X[i]
            elif maxFreq == H[X[i]]:
                mostFrequent = min(mostFrequent, X[i])
        else:
            H[X[i]] = 1
    return mostFrequent



#return lista



if __name__ == '__main__':
    print('Array desordenado: ', num)
    print(mostFrequentElement(num,100))