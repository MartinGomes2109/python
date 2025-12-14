#1 - pedir al usuario la ruta de un archivo de texto
#2 - leer el archivo de texto
#3 - separar en palabras
#4 - contar las palabras
#5 - mostrar las 5 palabras mas repetidas y su conteo

archivo = input('Ingrese la ruta del archivo de texto: ')
try:
    with open(archivo, 'r') as file:
        texto = file.read()
        palabras = texto.split()
        contador = {}
        for palabra in palabras:
            if palabra in contador:
                contador[palabra] += 1
            else:
                contador[palabra] = 1
        print(contador)
except FileNotFoundError:
    print('El archivo no existe')
    exit()
#separar el contenido en palabras
import re
palabras = re.findall(r'\b\w+\b', texto)
print(palabras)
#contar las palabras
contador = {}
for palabra in palabras:
    if palabra in contador:
        contador[palabra] += 1
    else:
        contador[palabra] = 1
print(contador)
#mostrar las 5 palabras mas repetidas
palabras_ordenadas = sorted(contador.items(), key=lambda x: x[1], reverse=True)
print(palabras_ordenadas[:5])