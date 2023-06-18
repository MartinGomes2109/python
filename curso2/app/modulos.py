def get_poblacion(lista):
    poblacion = {
        '1970' : int(lista['1970 Population']),
        '1980' : int(lista['1980 Population']),
        '1990' : int(lista['1990 Population']),
        '2000' : int(lista['2000 Population']),
        '2010' : int(lista['2010 Population']),
        '2015' : int(lista['2015 Population']),
        '2020' : int(lista['2020 Population']),
        '2022' : int(lista['2022 Population'])
    }
    labels = poblacion.keys()
    values = poblacion.values()
    return labels, values

def paises(data,country):
    result = list(filter(lambda data: data['Country/Territory'] == country, data))
    return result

def get_datos_values(data):
    values = list(map(lambda x: x['World Population Percentage'] ,data))
    return values

def get_datos_labels(data):
    labels = list(map(lambda x: x['Country/Territory'], data))
    return labels