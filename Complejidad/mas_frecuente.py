import time

arr5 = [46, 56, 99, 95, 1, 95, 74, 67, 24, 58, 11, 86, 48, 9, 96, 89, 8, 81, 70, 9, 93, 64, 42, 28, 61, 10, 44, 56, 4, 58, 40, 30, 21, 92, 64, 1, 57, 100, 32, 49, 30, 41, 8, 78, 56, 69, 64, 54, 82, 84,56]
def calculate_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time of '{func.__name__}': {execution_time} seconds")
        return result
    return wrapper

@calculate_execution_time
def moda(arr):
    dicc = {}
    for elem in arr:
        if elem in dicc:
            dicc[elem] += 1
        else:
            dicc[elem] = 1
    
    max_f = max(dicc.values())
    
    most_frequent_elements = [key for key, value in dicc.items() if value == max_f]
    
    return most_frequent_elements

@calculate_execution_time
def moda2(arr):
    while (len(arr) != 0):
        aux = []
        i = 0
        for elem in arr:
            if (elem in aux):
                i += 1
            else:
                aux.append(arr.pop(i))
    return aux


print(moda(arr5))