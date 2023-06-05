file = open('./prueba.txt')
print (file.read())
# abre el archivo y lo lee por completo

#print(file.readline())
# lee una linea del archivo, la primero o siguiente

for line in file:
    print(line)

file.close()
#lee el archivo completo linea por linea, luego cuando termina cierra el archivo para no ocupar memoria

with open('./prueba.txt') as file:
    for line in file:
        print(line)

#lo mismo, abre el archivo lo lee por completo linea por linea y lo cierra, es la forma mas comun de usar