numbers=[]
for element in range(1,11):
    numbers.append(element*2)
print(numbers)

#version simplificada
numberv2= [element * 2 for element in range(1,11)]
print(numberv2)

numbersv3=[i for i in range(1,31) if i % 2 == 0]
print(numbersv3)