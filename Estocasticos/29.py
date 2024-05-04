import numpy as np
import matplotlib.pyplot as plt

# Datos de 10 personas -> [edad, ingresos]

# La razon por la que estan los datos en 0.0, es porque
# todos los datos de entrada deben estar normalizados
# es decir, que deben ser datos numericos entre 0 y 1
personas = np.array([[0.3, 0.4], [0.4, 0.4],
                     [0.3, 0.2], [0.4, 0.1],
                     [0.5, 0.2], [0.4, 0.8],
                     [0.6, 0.8], [0.5, 0.6],
                     [0.7, 0.6], [0.8, 0.5]])

# 1 : aprobada  0 : denegada

# la razon por la que estan las clases definidas asi
# es porque en el aprendizaje supervisado
# nosotros ya sabemos que los primeros 5 datos
# deberan arrojar un resultado "denegada"
# y los siguientes 5, arrojaran "aprobada"

clases = np.array([0, 0, 0, 0, 0, 1, 1, 1, 1, 1])

# Grafica de dispersion (edad, ahorro)

plt.figure(figsize = (7, 7))
plt.title("Candidatos a Tarjeta BBVA Credito", fontsize = 20)
plt.scatter(personas[clases == 0].T[0],
            personas[clases == 0].T[1],
            marker = "x", s = 180, color = "red",
            linewidths = 5, label = "Denegada")
plt.scatter(personas[clases == 1].T[0],
            personas[clases == 1].T[1],
            marker = "o", s = 180, color = "blue",
            linewidths = 5, label = "Aprovada")
plt.xlabel("Edad", fontsize = 15)
plt.ylabel("Ingresos", fontsize = 15)
plt.legend(bbox_to_anchor = (1.3, 0.15))
plt.box(False)
plt.xlim((0, 1.01))
plt.ylim((0, 1.01))
plt.grid()
plt.show()