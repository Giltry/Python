"""
import random

# Genera un número aleatorio entre 1 y 100
numero_secreto = random.randint(1, 100)

intentos_maximos = random.randint(5, 20)

print("¡Bienvenido al juego de adivinar el número!")

for intento in range(1, intentos_maximos + 1):
        # Solicitar al usuario que adivine el número
        guess = int(input(f"Intento {intento}/{intentos_maximos}: Adivina el número entre 1 y 100: "))
        
        # Comprobar si el número adivinado es igual al número secreto
        if guess == numero_secreto:
            print(f"¡Felicidades! Adivinaste el número {numero_secreto} en {intento} intentos.")
            break
        elif guess < numero_secreto:
            print("El número es MAYOR. ¡Sigue intentando!\n")
        else:
            print("El número es MENOR. ¡Sigue intentando!\n")

if intento == intentos_maximos and guess != numero_secreto:
    print(f"¡Agotaste tus {intentos_maximos} intentos! El número secreto era {numero_secreto}. ¡Mejor suerte la próxima vez!")
"""

"""
#------------------------------------------------------------------------------------------------
n = int(input("Introduce el número de filas para generar la serie de Fibonacci: "))

if n < 1:
    print("Por favor, ingresa un número mayor o igual a 1.")
else:
    a, b = 0, 1
    for fila in range(1, n + 1):
        print(a, end=" ")
        a, b = b, a + b
        if fila < n:
            print()
"""

"""
#------------------------------------------------------------------------------------------------
palabra = input("Ingresa una palabra: ")

# Eliminar espacios en blanco y convertir la palabra a minúsculas
palabra = palabra.replace(" ", "").lower()

es_palindromo = True

for i in range(len(palabra) // 2):
    if palabra[i] != palabra[-i - 1]:
        es_palindromo = False
        break

if es_palindromo:
    print("La palabra es un palíndromo.")
else:
    print("La palabra no es un palíndromo.")"""

"""
#------------------------------------------------------------------------------------------------
while True:
    puntos = 0
    
    for _ in range(100): 
        eleccion = input("Elige un camino (1 o 2) o presiona 'Q' para salir: ")
        
        if eleccion.lower() == 'q' or eleccion.upper() == 'Q':
            break
        elif eleccion == '1':
            puntos += 100
            print("¡Ganaste 100 puntos!\n")
        elif eleccion == '2':
            print("¡Terminaste el juego!\n")
            break
        else:
            print("Opción no válida. Por favor, elige 1 o 2.")
    
    print("Puntaje final:",puntos,"puntos")
    
    jugar_nuevamente = input("¿Quieres jugar de nuevo? (S/N): ")
    if jugar_nuevamente.lower() == 'n' or eleccion.upper() == 'N':
        break
    elif jugar_nuevamente.lower() == 's' or eleccion.upper() == 'S':
        continue
    else:
        print("Opción no válida. Por favor, elige 'S' o 'N'.")

"""

#------------------------------------------------------------------------------------------------
import modulo_validacion_nombre_usuario

nombre = input("Ingrese su nombre de usuario: ")

resultado = modulo_validacion_nombre_usuario.validar_nombre_usuario(nombre)

if resultado == True:
    print("Nombre de usuario válido.")
else:
    print(resultado)