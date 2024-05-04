import serial
import time

# Configura el puerto serie y la velocidad de comunicación
puerto_serie = serial.Serial('COM3', 9600)  # Asegúrate de cambiar 'COM3' al puerto correcto
time.sleep(2)  # Espera a que se establezca la conexión

while True:
    # Lee la línea de datos del puerto serie
    datos = puerto_serie.readline().decode().strip()

    # Separa los valores de los ejes X e Y
    valores = datos.split(',')
    if len(valores) == 2:
        eje_x, eje_y = map(int, valores)
        print(f'Eje X: {eje_x}, Eje Y: {eje_y}')

    # Puedes agregar más lógica aquí según tus necesidades

# Cierra el puerto serie al finalizar
puerto_serie.close()
