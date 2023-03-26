def A(num):
    return num + 1

result = A(10)
print(result)

B = lambda num2 : num2 + 2
result2 = B(10)
print(result2)

full_name = lambda name, last_name: f'full name is {name.title()} {last_name.title()}'
val1 = input('nombre: ')
val2 = input('apellido: ')
result3 = full_name(val1, val2)
print(result3)