"""
while condicion:
    instrucciones
"""
#Tabla de multiplicar (del 1 al 10) del numero introducido
"""n = int(input("Introduce un numero: "))
i = 1
while i < 11:
    print(n, "x", i, "=", i*n)
    i = i + 1"""

#Calculo de la suma de los primeros n numeros
"""n = int(input("Introduce un numero: "))
i = 0
suma = 0
while i <= n:
    suma = suma + i
    i = i+1
print(suma)"""

# estructura for
"""
for item in secuencia:
    instrucciones
"""

#programa que muestre las tablas de multiplicar (1 al 10) del numero introducido
"""n = int(input("Introduce un numero: "))
for i in range(1,11):
    print(n, "x", i,"=",i*n)"""

#Calculo de la suma de los primeros n numeros
n = int(input("Introduce un numero: "))
suma = 0
for i in range(n+1):
    suma = suma + i
print(suma)