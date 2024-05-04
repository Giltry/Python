Lista1 = []

Lista2 = [100, 1000, 'Carlos', 'Jueves']

print(Lista2[0])
print(Lista2[-4])

Lista2.append(5000)
print(Lista2)

Lista2.reverse()
print(Lista2)

Lista2.remove(1000)
print(Lista2)

Lista2.insert(2, 3000)
print(Lista2)

Lista3 = [1, 2, 3, [4, 5]]
print(Lista3[3][1])

vocales = ['a', 'e', 'i', 'o', 'u']
for letra in 'hermosa':
    if letra in vocales:
        print(letra)

valor = (1, 2, 3)
x, y, z = valor
print(x)

valor2 = valor, (4, 5, 6)
print(valor2)

diccionario = {
    "posicion": 1234,
    "posicion2": True,
    "posicion3": "Hola",
    "posicion4": [1, 2, 3, 4]
}

print(diccionario['posicion2'])

calificaciones = dict(Andres = 8, Omar = 10, Jesus = 9, Paty = 7)
print(calificaciones)

#Tarea: Juego del ahorcado