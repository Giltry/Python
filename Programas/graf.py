import serial, time
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Configuración del puerto serie (asegúrate de cambiar el puerto COMx según tu configuración)
ser = serial.Serial('COM3', 9600, timeout=1)

try:
    while True:
        # Leer datos del puerto serie
        data = ser.readline().decode('utf-8').rstrip()

        # Imprimir los datos
        print(f'Temperatura: {data}°C')

        # Esperar un segundo antes de la siguiente lectura
        time.sleep(1)

except KeyboardInterrupt:
    # Detener la lectura cuando se presiona Ctrl+C
    ser.close()
    print("Lectura detenida.")
