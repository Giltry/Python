"""print('Hola mundo')

Nombre = input('¿Como te llamas? ')
print(type(Nombre))
Edad = int(input('Introduce tu edad: '))
print(type(Edad))
Estatura = float(input('Cuanto mides: '))
print(type(Estatura))"""

#Programa que convierta °c a °f
# °f= 1.8 * centigrados + 32
"""c = float(input('Grados °C: '))
f = 1.8 * c + 32
print('°f:', f)"""

#Convertir dolares en pesos
"""dolar = float(input('Dolares: '))
peso = 16.74 * dolar
print('peso MXN:', peso)
"""

#Programa que calcula el perimetro y area de un circulo
"""from math import pi
r = float(input('introduce el radio: '))
per = 2* pi * r
area = pi * r ** 2
print("Area",area)
print("Perimetro",per)"""

#Ingresar nombre y apellido, irmpirmir en pantalla nombre + apellido
"""Nombre = input('¿Como te llamas? ')
Apellido = input('¿Cual es tu apellido? ')

print(Nombre, Apellido)"""

#Pedir un numero y poner True si es par y False si no es par
"""Numero = int(input('Numero: '))
print(bool(Numero % 2 == 0))
#print(valor)"""

"""if(valor % 2 == 0):
    print("el numero es par")
else:
    print("el numero es impar")"""

#Programa para definir tipo de licencia
#edad-int(Input("Ingrese su edad:"))

"""
si es menor a 16 años -- no licencia
si entre 16 y 18 se puede permiso
mayor de edad licencia
mayor de 65 licencia especial
"""

"""edad = int(input("Ingrese su edad:"))
if edad < 16:
    print("Licencia no permitida")
elif edad >= 16 and edad < 18:
    print("Licencia permitida")
elif edad >= 18 and edad < 65:
    print("Licencia aceptada")
elif edad >= 65:
    print("Licencia especial")
else:
    print("error")"""

#Programa que lea una letra e indique si es vocal
letra = input("Ingresa una letra: ")
if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
    print("es vocal")
else:
    print("no es vocal")

