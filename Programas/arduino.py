import serial
import matplotlib.pyplot as plt

# Configuración del puerto serie (ajusta el puerto COMx según tu configuración)
ser = serial.Serial('COM3', 9600, timeout=1)

# Configuración de la gráfica
plt.ion()  # Modo interactivo
fig, ax = plt.subplots()
temperaturas = []

# Establecer rangos de los ejes
ax.set_xlim(0, 10)  # Ajusta según la cantidad de muestras que deseas mostrar
ax.set_ylim(0, 100)  # Ajusta según el rango de temperaturas esperado

try:
    while True:
        # Leer datos del puerto serie
        data = ser.readline().decode('utf-8').rstrip()

        # Convertir el dato a float (asegúrate de que el dato enviado desde Arduino sea un número)
        try:
            temperatura = float(data)
        
            # Añadir temperatura a la lista
            temperaturas.append(temperatura)

            # Limitar la cantidad de datos mostrados en la gráfica para evitar sobrecargarla
            if len(temperaturas) > 10:
                temperaturas.pop(0)

            # Limpiar la gráfica y dibujar los datos
            ax.clear()
            ax.scatter(range(len(temperaturas)), temperaturas)
            ax.set_title('Temperatura en tiempo real')
            ax.set_xlabel('Muestras')
            ax.set_ylabel('Temperatura (°C)')

            # Actualizar la gráfica en tiempo real
            plt.draw()
            plt.pause(0.1)  # Breve pausa para permitir la actualización

        except ValueError:
            print("Error")

except KeyboardInterrupt:
    # Detener la lectura cuando se presiona Ctrl+C
    ser.close()
    print("Lectura detenida.")
