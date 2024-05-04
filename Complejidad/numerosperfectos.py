num = int(input('ingrese numero: '))
array = []      
array = [i for i in range(1,num+1) if num % i == 0]
print(array)
ult_elem = array.index(num)
sum_array = 0
for i in range(ult_elem):
    sum_array = sum_array + array[i]
if num == sum_array:
    print(num, ' es numero perfecto')
else:
    print(num, ' no es numero perfecto')