def run():
    print('hola mundo')
    for i in range(10):
        print(i)
"""esta funcion escribe hola mundo 10 veces y luego imprime los numeros del 0 al 9
"""
#crear una lista con los cuadrados de los n primeros numeros naturales
def cuadrados(n):
    return [i**2 for i in range(1,n+1)]

def numeros_primos(n):
    """
    Encuentra todos los números primos menores o iguales a n.
    Versión optimizada usando la criba de Eratóstenes.
    """
    if n < 2:
        return []
    
    # Inicializar lista de booleanos (True = primo, False = no primo)
    es_primo = [True] * (n + 1)
    es_primo[0] = es_primo[1] = False  # 0 y 1 no son primos
    
    # Criba de Eratóstenes
    for i in range(2, int(n**0.5) + 1):
        if es_primo[i]:
            # Marcar todos los múltiplos de i como no primos
            for j in range(i*i, n + 1, i):
                es_primo[j] = False
    
    # Recopilar números primos
    primos = [i for i in range(2, n + 1) if es_primo[i]]
    return primos

def es_primo(numero):
    """
    Verifica si un número es primo (versión optimizada).
    """
    if numero < 2:
        return False
    if numero == 2:
        return True
    if numero % 2 == 0:
        return False
    
    # Solo verificar divisores impares hasta la raíz cuadrada
    for i in range(3, int(numero**0.5) + 1, 2):
        if numero % i == 0:
            return False
    return True

if __name__ == '__main__':
    run()
    print(cuadrados(100))
    print(numeros_primos(10))