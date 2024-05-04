import random
import time

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

def radix_sort(arr):
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

def cocktail_sort(arr):
    n = len(arr)
    swapped = True
    start = 0
    end = n - 1
    while (swapped == True):
        swapped = False
        for i in range(start, end):
            if (arr[i] > arr[i + 1]):
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        if (swapped == False):
            break
        swapped = False
        end = end - 1
        for i in range(end - 1, start - 1, -1):
            if (arr[i] > arr[i + 1]):
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        start = start + 1

# Generar 50 números aleatorios
random_numbers = [random.randint(1, 1000) for _ in range(10000)]

print("\nArreglo original:", random_numbers)
# Aplicar radix sort
st = time.time()
radix_sort(random_numbers)
et = time.time()
print("Arreglo ordenado con Radix Sort:", random_numbers)
print(et - st)

random_numbers2 = [random.randint(1, 1000) for _ in range(10000)]
print("\nArreglo original:", random_numbers2)
# Aplicar cocktail sort
st2 = time.time()
cocktail_sort(random_numbers2)
et2 = time.time()
print("Arreglo ordenado con Cocktail Sort:", random_numbers2)
print(et2 - st2)
