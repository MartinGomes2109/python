def run():
    while True:
        print('calculadora')
        print('1. suma')
        print('2. resta')
        print('3. multiplicacion')
        print('4. division')
        print('escriba salir para terminar')
        opcion = input('ingrese una opcion: ')

        if opcion == 'salir':
            print('adios')
            break

        match opcion:
            case '1':
                print('ingrese 2 valores:')
                a = int(input())
                b = int(input())
                print(suma(a, b))
            case '2':
                print('ingrese 2 valores:')
                a = int(input())
                b = int(input())
                print(resta(a, b))
            case '3':
                print('ingrese 2 valores:')
                a = int(input())
                b = int(input())
                print(multiplicacion(a, b))
            case '4':
                print('ingrese 2 valores:')
                a = int(input())
                b = int(input())
                print(division(a, b))
            case _:
                print('opcion incorrecta')

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b
        
def multiplicacion(a, b):
    return a * b

def division(a, b):
    return a / b
    

if __name__ == '__main__':
    run()