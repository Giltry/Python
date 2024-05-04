import tkinter as tk
import random

class Ahorcado:
    def __init__(self, root):
        self.root = root

        self.palabras = {
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
            "PATRICIA": "Bruja Presidenta"
        }
        self.palabra_actual = ""
        self.intentos = 6
        self.letras_adivinadas = []

        self.inicializar_juego()

        # Agregar eventos de teclado
        self.root.bind("<KeyPress>", self.tecla_presionada)

    def inicializar_juego(self):
        self.palabra_actual, pista = random.choice(list(self.palabras.items()))
        self.palabra_actual = self.palabra_actual.upper()

        self.frame_palabra = tk.Frame(self.root)
        self.frame_palabra.pack()

        self.label_palabra = tk.Label(self.frame_palabra, text=self.obtener_palabra_oculta(), font=("Helvetica", 18))
        self.label_palabra.pack()

        self.frame_info = tk.Frame(self.root)
        self.frame_info.pack()

        self.label_letras_usadas = tk.Label(self.frame_info, text="Letras usadas:", font=("Helvetica", 12))
        self.label_letras_usadas.grid(row=3)

        self.label_intentos = tk.Label(self.frame_info, text=f"Intentos restantes: {self.intentos}", font=("Helvetica", 12))
        self.label_intentos.grid(row=1)

        self.label_pista = tk.Label(self.frame_info, text=f"Pista: {pista}", font=("Helvetica", 12))
        self.label_pista.grid(row=0)

        self.label_mensaje = tk.Label(self.root, text="", font=("Helvetica", 14))
        self.label_mensaje.pack()

        self.frame_teclado = tk.Frame(self.root)
        self.frame_teclado.pack()

        letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for i in range(3):
            for j in range(9):
                letra_index = i * 9 + j
                if letra_index < len(letras):
                    letra = letras[letra_index]
                    btn_letra = tk.Button(self.frame_teclado, text=letra, font=("Helvetica", 14), command=lambda l=letra: self.verificar_letra(l))
                    btn_letra.grid(row=i, column=j)

    def obtener_palabra_oculta(self):
        return " ".join([letra if letra in self.letras_adivinadas else "_" for letra in self.palabra_actual])

    def verificar_letra(self, letra):
        if letra in self.letras_adivinadas:
            self.mostrar_mensaje("La letra ya fue seleccionada.")
            return

        self.letras_adivinadas.append(letra)

        if letra not in self.palabra_actual:
            self.intentos -= 1
            if self.intentos == 0:
                self.finalizar_juego(False)
                return

        palabra_oculta = self.obtener_palabra_oculta()
        self.label_palabra.config(text=palabra_oculta)
        self.actualizar_info()

        if "_" not in palabra_oculta:
            self.finalizar_juego(True)

    def tecla_presionada(self, event):
        # Verificar si la tecla presionada es una letra
        if event.char and event.char.isalpha():
            letra = event.char.upper()
            self.verificar_letra(letra)

    def actualizar_info(self):
        letras_usadas = " ".join(self.letras_adivinadas)
        self.label_letras_usadas.config(text=f"Letras usadas: {letras_usadas}")
        self.label_intentos.config(text=f"Intentos restantes: {self.intentos}")

    def mostrar_mensaje(self, mensaje):
        self.label_mensaje.config(text=mensaje)

    def finalizar_juego(self, ganador):
        mensaje = "¡Ganaste!" if ganador else "Perdiste. La palabra era: " + self.palabra_actual
        self.mostrar_mensaje(mensaje)

root = tk.Tk()
ahorcado_game = Ahorcado(root)
root.mainloop()
