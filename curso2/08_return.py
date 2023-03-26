def suma_rangos(min,max):
    sum = 0
    for x in range(min,max):
        sum += x
    print(sum)

suma_rangos(1,10)
suma_rangos(1,20)

def suma_rangos2(min,max):
    sum = 0
    for x in range(min,max):
        sum += x
    return(sum)

result=suma_rangos2(1,10)
print(result)
result=suma_rangos2(1,20)
print(result)

