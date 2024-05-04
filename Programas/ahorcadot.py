import tkinter as tk
import random

def inicializar_juego():
    global palabra_actual, letras_adivinadas, intentos, label_palabra, label_letras_usadas, label_intentos, label_mensaje

    palabra_actual, pista = random.choice(list(palabras.items()))
    palabra_actual = palabra_actual.upper()

    frame_palabra = tk.Frame(root)
    frame_palabra.pack()

    label_palabra = tk.Label(frame_palabra, text=obtener_palabra_oculta(palabra_actual, letras_adivinadas), font=("Helvetica", 18))
    label_palabra.pack()

    frame_info = tk.Frame(root)
    frame_info.pack()

    label_pista = tk.Label(frame_info, text=f"Pista: {pista}", font=("Helvetica", 12))
    label_pista.grid(row=0)

    label_intentos = tk.Label(frame_info, text=f"Intentos restantes: {intentos[0]}", font=("Helvetica", 12))
    label_intentos.grid(row=1)

    label_letras_usadas = tk.Label(frame_info, text="Letras usadas:", font=("Helvetica", 12))
    label_letras_usadas.grid(row=3)

    label_mensaje = tk.Label(root, text="", font=(14))
    label_mensaje.pack()

    frame_teclado = tk.Frame(root)
    frame_teclado.pack()

    letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(3):
        for j in range(9):
            letra_index = i * 9 + j
            if letra_index < len(letras):
                letra = letras[letra_index]
                btn_letra = tk.Button(frame_teclado, text=letra, font=("Helvetica", 14), command=lambda l=letra: verificar_letra(l, palabra_actual))
                btn_letra.grid(row=i, column=j)

def obtener_palabra_oculta(palabra, letras_adivinadas):
    return " ".join([letra if letra in letras_adivinadas else "_" for letra in palabra])

def verificar_letra(letra, palabra_actual):
    global letras_adivinadas, intentos, label_palabra

    if letra in letras_adivinadas:
        mostrar_mensaje("La letra ya fue seleccionada.")
        return

    letras_adivinadas.append(letra)

    if letra not in palabra_actual:
        intentos[0] -= 1
        if intentos[0] == 0:
            finalizar_juego(False, palabra_actual)
            return

    palabra_oculta = obtener_palabra_oculta(palabra_actual, letras_adivinadas)
    label_palabra.config(text=palabra_oculta)
    actualizar_info()

    if "_" not in palabra_oculta:
        finalizar_juego(True, palabra_actual)

def tecla_presionada(event):
    # Verificar si la tecla presionada es una letra
    if event.char and event.char.isalpha():
        letra = event.char.upper()
        verificar_letra(letra, palabra_actual)

def actualizar_info():
    global letras_adivinadas, label_letras_usadas, label_intentos

    letras_usadas = " ".join(letras_adivinadas)
    label_letras_usadas.config(text=f"Letras usadas: {letras_usadas}")
    label_intentos.config(text=f"Intentos restantes: {intentos[0]}")

def mostrar_mensaje(mensaje):
    global label_mensaje
    label_mensaje.config(text=mensaje)

def finalizar_juego(ganador, palabra_actual):
    mensaje = "¡Ganaste!" if ganador else "Perdiste. La palabra era: " + palabra_actual
    mostrar_mensaje(mensaje)

# Configuración inicial
root = tk.Tk()
root.geometry("400x300")

palabras = {
    "ALBERTINE": "Bruja Garabateadora",
    "CANDY": "Bruja Orejas de conejo",
    "CHARLOTTE": "Bruja de Dulces",
    "DURBAR": "Bruja Santa",
    "ETTEILLA": "Bruja Adivina",
    "GERTRUD": "Bruja del Jardin de Rosas",
    "ICHIZO": "Bruja Halcon Nocturno",
    "LUCY": "Bruja Errante",
    "MATASABURO": "Bruja de Chocolate",
    "PAOLA": "Bruja de Goma",
    "PATRICIA": "Bruja Presidenta",
    "RASPBERRY": "Bruja Critica",
    "REBECCA": "Bruja Oveja",
    "SHIN": "Bruja Ñiñera",
    "STACEY": "Bruja de la Azotea",
    "TERESA": "Bruja del Pendulo",
    "UHRMANN": "Bruja Canina",
    "ZENOBIA": "Bruja de la Caja de Arena"
}
palabra_actual = ""
intentos = [6]
letras_adivinadas = []

# Inicializar el juego
inicializar_juego()

# Agregar eventos de teclado
root.bind("<KeyPress>", tecla_presionada)

# Iniciar la aplicación
root.mainloop()
