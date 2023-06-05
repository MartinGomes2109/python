with open('./prueba.txt', 'w+') as file:
    for line in file:
        print(line)
    file.write('nuevas cosas en el archivo\n')
    file.write('otra linea\n')
    file.write('otra line man\n')
    
#el permiso r+ sirve para que el archivo pueda ser escrito y leido
#el permiso w+ sirve para leer y escribir el archivo pero sobreescribiendo el coontenido
#\n es el salto de linea
# r solo es solo lectura
# w solo es solo escritura