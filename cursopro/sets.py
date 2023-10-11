from datetime import datetime
set1 = {0,1,3,5,7,9}
set2 = {0,2,4,6,8}
print(set1)
print(set2)

print('union')
set3 = set1 | set2
print(set3)

print('interseccion')
set3 = set1 & set2
print(set3)

print('diferencia(resta)')
set3 = set1 - set2
print(set3)

print('simetrica(opuesto de inter)')
set3 = set1 ^ set2
print(set3)


def remove_duplicates(list):
    without_duplicates = []
    for element in list:
        if element not in without_duplicates:
            without_duplicates.append(element)
    return without_duplicates

def run():
    random_list = [1,1,1,2,2,3,4,4,4,4,5,5,6,7]
    print(remove_duplicates(random_list))
    print(random_list)
    list2 = list(set(random_list))
    print(list2)
    print()
    time = datetime.now()
    print(time)
    print('fecha formato latam')
    time2 = time.strftime('%d/%m/%Y')
    print(time2)
    print('fecha formato usa')
    time2 = time.strftime('%m/%d/%Y')
    print(time2)
    
    
    
if __name__ == '__main__':
    run()