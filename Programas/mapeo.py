import numpy as np
import matplotlib.pyplot as plt

# Solicita al usuario ingresar los coeficientes
a1 = float(input("Ingrese el coeficiente a1 para la primera ecuación: "))
b1 = float(input("Ingrese el coeficiente b1 para la primera ecuación: "))
c1 = float(input("Ingrese el coeficiente c1 para la primera ecuación: "))

a2 = float(input("Ingrese el coeficiente a2 para la segunda ecuación: "))
b2 = float(input("Ingrese el coeficiente b2 para la segunda ecuación: "))
c2 = float(input("Ingrese el coeficiente c2 para la segunda ecuación: "))

# Define las ecuaciones del sistema
def ecuacion_1(x):
    return a1 * x + b1

def ecuacion_2(x):
    return a2 * x + b2

# Genera valores x
x_values = np.linspace(-5, 5, 100)

# Calcula los valores y para cada ecuación
y1_values = ecuacion_1(x_values)
y2_values = ecuacion_2(x_values)

# Grafica las ecuaciones
plt.plot(x_values, y1_values, label=f'{a1}x + {b1}')
plt.plot(x_values, y2_values, label=f'{a2}x + {b2}')

# Encuentra la intersección
intersection = np.linalg.solve([[a1, -1], [a2, -1]], [-c1, -c2])
intersection_x = intersection[0]
intersection_y = ecuacion_1(intersection_x)

# Marca la intersección
plt.scatter(intersection_x, intersection_y, color='red', label='Intersección')

# Configuración adicional del gráfico
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.title('Intersección de Ecuaciones')
plt.xlabel('x')
plt.ylabel('y')

# Muestra el gráfico
plt.show()
