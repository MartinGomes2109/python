from datetime import datetime

def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print('pasaron ' + str(time_elapsed.total_seconds()) + ' segundos')
    return wrapper

@execution_time    
def random_func():
    for _ in range(1, 100000000):
        pass

@execution_time
def suma(a,b):
    return a + b

@execution_time
def saludo(nom):
    print("hola " + nom)

def run():
    random_func()
#   suma(10,10)
#    saludo("cesar")
    
if __name__ == '__main__':
    run()
    
# agregar (*args, **kwargs) a la funcion envoltura sirve para que siga funcionando sin importar con que funcion se use, para que acepte cualquier argumento de cualquier funcion