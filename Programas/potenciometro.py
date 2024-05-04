import serial
import matplotlib.pyplot as plt
from drawnow import drawnow

# Inicializa la comunicación serial con Arduino
ser = serial.Serial('COM3', 9600)

# Almacena los datos del potenciómetro
datos_potenciometro = []

# Función para actualizar el gráfico en tiempo real
def actualizar_grafico():
    plt.plot(datos_potenciometro, label='Potenciómetro')
    plt.title('Gráfico en Tiempo Real')
    plt.xlabel('Muestras')
    plt.ylabel('Valor del Potenciómetro')
    plt.legend()
    plt.grid(True)

# Bucle principal
while True:
    while (ser.inWaiting() == 0):
        pass

    valor_potenciometro = int(ser.readline().decode('utf-8').strip())
    datos_potenciometro.append(valor_potenciometro)

    if len(datos_potenciometro) > 50:
        datos_potenciometro.pop(0)

    # Actualiza el gráfico en tiempo real
    drawnow(actualizar_grafico)
