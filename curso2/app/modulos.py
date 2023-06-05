def get_datos():
    keys = ['arg','col']
    values = [4343,2342]
    return keys,values

A = 'hola'

def paises(data,country):
    result = list(filter(lambda data: data['Country'] == country, data))
    return result