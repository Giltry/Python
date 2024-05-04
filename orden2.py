import random

def cocktail_sort(arr):
    n = len(arr)
    swapped = True
    start = 0
    end = n-1
    while (swapped == True):
        swapped = False
        for i in range(start, end):
            if (arr[i] > arr[i + 1]):
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        if (swapped == False):
            break
        swapped = False
        end = end-1
        for i in range(end-1, start-1, -1):
            if (arr[i] > arr[i + 1]):
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        start = start + 1

def radix_sort(arr):
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

# Generar 50 números aleatorios
random_numbers = random.sample(range(1, 100), 50)

# Mostrar números aleatorios sin ordenar
print("Números aleatorios sin ordenar:")
print(random_numbers)

# Ordenar con Cocktail Sort
cocktail_sort(random_numbers)
print("\nNúmeros ordenados con Cocktail Sort:")
print(random_numbers)

# Ordenar con Radix Sort
radix_sort(random_numbers)
print("\nNúmeros ordenados con Radix Sort:")
print(random_numbers)
