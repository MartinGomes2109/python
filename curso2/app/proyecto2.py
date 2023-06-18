import modulos
import graficas
import read_csv

def run():
    data = read_csv.read_csv('./population.csv')
    # para filtrar datos especificos y reducir la lista
    data = list(filter(lambda x: x['Continent'] == 'South America', data))
    list_values = modulos.get_datos_values(data)
    list_labels = modulos.get_datos_labels(data)
    if len(list_values and list_labels) > 0:
        graficas.generar_grafica_pie(list_labels,list_values)
#    country = input('escribe un pais : ')
#    result2 = modulos.paises(data,country)
    #si len es mayor a 0 es porque encontro un resulta, caso contrario no existe
#    if len(result2) > 0:
#        country = result2[0]
#        labels, values = modulos.get_poblacion(country)
#        graficas.generar_grafica_bar(labels, values)
    
if __name__ == '__main__':
    run()