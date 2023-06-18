import csv
#modulo nativo de paiton para trabajar con archivos csv
def read_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        #se delimita con una coma porque asi esta en el archivo original, si viene con ; se coloca ;
        header = next(reader)
        data = []
        for row in reader:
            iterable = zip(header,row)
            country_c = {key : value for key,value in iterable}
            data.append(country_c)
        return data

if __name__ == '__main__':
    data = read_csv('./population.csv')
    for i in range(0,10):
        print(data[i])
        
        
        
#para que vaya acumulando info
#reader = csv.reader(csvfile)
#for date in reader
#sum += int(date[1])