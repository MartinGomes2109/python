def es_primo(num: int) -> bool:
    contador = 2
    if (num == 1) or (num== 2):
        return False
    else:
        while contador != num:
            if (num % contador) == 0:
                return False
            contador += 1
        return True

def run():
    numero = int(input('ingrese un numero: '))
    if es_primo(numero):
        print('el numero es primo')
    else:
        print('el numero no es primo')
        
if __name__=='__main__':
    run()
    