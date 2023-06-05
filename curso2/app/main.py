import python.curso2.app.modulos as modulos

result = modulos.get_datos()
print(result)

print(modulos.A)

data = [
    {
        'Country': 'colombia',
        'Population': 500
    },
    {
        'Country': 'Argentina',
        'Population': 700
    },
    {
        'Country': 'mexico',
        'Population': 300
    },
    {
        'Country': 'peru',
        'Population': 400
    }
]

def run():
    Country = input('escribe un pais de latam : ')
    result2 = modulos.paises(data,Country)
    if result2 == []:
        print('pais no se encuentra en la base de datos')
    else:
        print(result2)
        
if __name__ == '__main__':
    run()