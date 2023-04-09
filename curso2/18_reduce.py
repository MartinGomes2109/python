import functools

number = [1,2,3,4,5]

new_list = functools.reduce(lambda contador,item: contador + item, number)

print(number)
print(new_list)