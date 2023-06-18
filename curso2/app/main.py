import modulos
import graficas
import read_csv

def run():
    data = read_csv.read_csv('./population.csv')
    country = input('escribe un pais : ')
    result2 = modulos.paises(data,country)
    #si len es mayor a 0 es porque encontro un resulta, caso contrario no existe
    if len(result2) > 0:
        country = result2[0]
        labels, values = modulos.get_poblacion(country)
        graficas.generar_grafica_bar(labels, values)
    
if __name__ == '__main__':
    run()