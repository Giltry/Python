# 1. Programa que muestre el valor absoluto de un número
"""print("valor absoluto")
numero = float(input("Ingrese un número: "))
valor_absoluto = abs(numero)
print("El valor absoluto de", numero, "es", valor_absoluto)"""

#------------------------------------------------------------------------------------------------
# 2. Programa para definir el monto a pagar#10 zapatos 10%, 20 zapatos 20%, mayor a 30 zapatos 40%
#Costo por par de zapatos $100

"""precio_por_zapato = 100
# Solicitar la cantidad de zapatos que el usuario quiere comprar
cantidad_zapatos = int(input("Ingrese la cantidad de zapatos que desea comprar: "))
# Calcular el monto total a pagar
monto_total = cantidad_zapatos * precio_por_zapato

if cantidad_zapatos >= 30:
    descuento = 0.4  # 40% de descuento
elif cantidad_zapatos >= 20:
    descuento = 0.2  # 20% de descuento
elif cantidad_zapatos >= 10:
    descuento = 0.1  # 10% de descuento
else:
    descuento = 0  # Sin descuento

monto_con_descuento = monto_total * (1 - descuento)

print("El monto total a pagar con descuento es: $",monto_con_descuento)"""

#------------------------------------------------------------------------------------------------
# 3. Programa para pedir tres números e indique cual es el mayor

"""numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
numero3 = float(input("Ingrese el tercer número: "))

if numero1 >= numero2 and numero1 >= numero3:
    mayor = numero1
elif numero2 >= numero1 and numero2 >= numero3:
    mayor = numero2
else:
    mayor = numero3

print("El número mayor es:",mayor)"""

#------------------------------------------------------------------------------------------------
# 4. Programa que muestra el signo zodiacal de una persona, al introducir su fecha de nacimiento

"""dia = int(input("Ingrese el día de su fecha de nacimiento: "))
mes = int(input("Ingrese el mes de su fecha de nacimiento (en números): "))

if (mes == 3 and dia >= 21) or (mes == 4 and dia <= 19):
    signo = "Aries"
elif (mes == 4 and dia >= 20) or (mes == 5 and dia <= 20):
    signo = "Tauro"
elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20):
    signo = "Géminis"
elif (mes == 6 and dia >= 21) or (mes == 7 and dia <= 22):
    signo = "Cáncer"
elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 22):
    signo = "Leo"
elif (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22):
    signo = "Virgo"
elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):
    signo = "Libra"
elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 21):
    signo = "Escorpio"
elif (mes == 11 and dia >= 22) or (mes == 12 and dia <= 21):
    signo = "Sagitario"
elif (mes == 12 and dia >= 22) or (mes == 1 and dia <= 19):
    signo = "Capricornio"
elif (mes == 1 and dia >= 20) or (mes == 2 and dia <= 18):
    signo = "Acuario"
else:
    signo = "Piscis"

print("Tu signo zodiacal es:", signo)
"""

#------------------------------------------------------------------------------------------------
# 5. Programa que pida dos números, e imprima en pantalla cual número es mayor, cual es menor o en su caso si son iguales

"""numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

if numero1 > numero2:
    print(numero1,"es mayor que",numero2)
elif numero1 < numero2:
    print(numero2,"es mayor que",numero1)
else:
    print(numero1,"y",numero2,"son iguales.")"""

#------------------------------------------------------------------------------------------------
# 5.5 Switch Case
"""
print("Lista de productos disponibles:")
print("Producto - - Codigo - - Precio")
print("Camisa - - - - 1 - - - - $100")
print("Cinturon - - - 2 - - - - $50")
print("Boxers - - - - 3 - - - - $75")
print("Tenis  - - - - 4 - - - - $70")
print("Falda  - - - - 5 - - - - $20")
print("Colcha - - - - 6 - - - - $150")
print("Pantalon - - - 7 - - - - $125")
print("Calcetin - - - 8 - - - - $10")
print("Zapato - - - - 9 - - - - $80")
print("Sudadera - - - 10  - - - $90")

producto = int(input(print("Ingrese el codigo del producto: ")))
cantidad = int(input(print("Ingrese la cantidad a comprar: ")))

if producto == 1:
    print("Su total a pagar es de:", cantidad * 100)
elif producto == 2:
    print("Su total a pagar es de:", cantidad * 50)
elif producto == 3:
    print("Su total a pagar es de:", cantidad * 75)
elif producto == 4:
    print("Su total a pagar es de:", cantidad * 70)
elif producto == 5:
    print("Su total a pagar es de:", cantidad * 20)
elif producto == 6:
    print("Su total a pagar es de:", cantidad * 150)
elif producto == 7:
    print("Su total a pagar es de:", cantidad * 125)
elif producto == 8:
    print("Su total a pagar es de:", cantidad * 10)
elif producto == 9:
    print("Su total a pagar es de:", cantidad * 80)
elif producto == 10:
    print("Su total a pagar es de:", cantidad * 50)
else:
    print("Error")"""

#------------------------------------------------------------------------------------------------
# 6. Programa que indique si un año es o no es un año bisiesto.

"""ano = int(input("Ingrese un año: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(ano,"es un año bisiesto.")
else:
    print(ano,"no es un año bisiesto.")"""

#------------------------------------------------------------------------------------------------
# 7. Programa que calcule el día de la semana en que cae una fecha cualquiera posterior a 1582

"""fecha = input("Ingrese la fecha en formato DD/MM/AAAA: ")

dia, mes, ano = map(int, fecha.split('/'))

if ano < 1582:
    print("El año debe ser posterior a 1582 para utilizar este algoritmo.")
else:
    A = (14 - mes) // 12
    B = ano - A
    C = mes + 12 * A - 2
    D = B // 4
    E = B // 100
    F = B // 400
    G = (31 * C) // 12
    H = dia + B + D - E + F + G
    I = H % 7

    if I == 0:
        print("La fecha", fecha, "cae en un Domingo")
    elif I == 1:
        print("La fecha", fecha, "cae en un Lunes")
    elif I == 2:
        print("La fecha", fecha, "cae en un Martes")
    elif I == 3:
        print("La fecha", fecha, "cae en un Miercoles")
    elif I == 4:
        print("La fecha", fecha, "cae en un Jueves")
    elif I == 5:
        print("La fecha", fecha, "cae en un Viernes")
    elif I == 6:
        print("La fecha", fecha, "cae en un Sabado")
    else:
        print("Error")"""