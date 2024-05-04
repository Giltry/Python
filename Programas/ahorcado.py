import random

# Lista de palabras para adivinar
palabras = ["albertine", "candy", "charlotte", "durbar", "etteilla", "gertrud",
            "ichizo", "lucy", "matasaburo", "dorothy", "oshiti", "paola", "patricia",
            "raspberry", "rebecca", "shin", "stacey", "teresa", "uhrmann", "zenobia"]

# Función para elegir una palabra al azar
def seleccionar_palabra(palabras):
    return random.choice(palabras)

# Función para mostrar la palabra oculta con letras adivinadas
def mostrar_palabra(palabra, letras_adivinadas):
    palabra_mostrada = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            palabra_mostrada += letra
        else:
            palabra_mostrada += "_"
    return palabra_mostrada

# Función principal del juego
def jugar_ahorcado():
    palabra_secreta = seleccionar_palabra(palabras)
    letras_adivinadas = []
    intentos_restantes = 6

    print("Bienvenido al juego del ahorcado!")
    print("Nombres de Brujas del videojuego Magireco")
    print(mostrar_palabra(palabra_secreta, letras_adivinadas))

    while True:
        letra = input("\nAdivina una letra: ").lower()

        if letra in letras_adivinadas:
            print("Ya adivinaste esa letra antes.\n")
        elif letra in palabra_secreta:
            letras_adivinadas.append(letra)
            palabra_mostrada = mostrar_palabra(palabra_secreta, letras_adivinadas)
            print(palabra_mostrada)

            if palabra_mostrada == palabra_secreta:
                print("¡Felicidades! Has adivinado la palabra correctamente.\n")
                break
        else:
            letras_adivinadas.append(letra)
            intentos_restantes -= 1
            print(f"Letra incorrecta. Te quedan {intentos_restantes} intentos.\n")

            if intentos_restantes == 0:
                print(f"Has perdido. La palabra era: {palabra_secreta}.\n")
                break

# Iniciar el juego
jugar_ahorcado()