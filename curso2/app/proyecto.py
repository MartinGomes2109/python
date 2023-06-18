import matplotlib.pyplot as plt
import csv

def run(path):
    with open(path, 'r') as csvfile:
        lector = csv.reader(csvfile)
        header = next(lector)
        data = []
        for row in lector:
            iterable = zip(header,row)
            paises = {key: value for key,value in iterable}
            data.append(paises)
        return data

def numeros(lista):
    list = []
    list.append(int(lista['1970 Population']))
    list.append(int(lista['1980 Population']))
    list.append(int(lista['1990 Population']))
    list.append(int(lista['2000 Population']))
    list.append(int(lista['2010 Population']))
    
    list.append(int(lista['2015 Population']))
    list.append(int(lista['2020 Population']))
    list.append(int(lista['2022 Population']))
    return list

def generar_grafica(labels,values):
    fig, ax = plt.subplots()
    ax.bar(labels,values)
    plt.show()
            
if __name__ == '__main__':
    ent = int(input('ingrese un numero hasta 237: '))
    if ent > 237 :
        print('entrada fuera de rango')
    else:
        data = run('./population.csv')
        new_data = list(filter(lambda x: x['Rank'] == str(ent), data))
        new_data = new_data[0]
        print(new_data)
        labels = ['1970','1980','1990','2000','2010','2015','2020','2022']
        values = numeros(new_data)
        generar_grafica(labels,values)