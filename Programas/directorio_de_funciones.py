import math

def conversion_entrebases(numero_decimal, base):
    if base == 2:
        resultado = ''
        if numero_decimal == 0:
            resultado = '0'
        while numero_decimal > 0:
            residuo = numero_decimal % 2
            resultado = str(residuo) + resultado
            numero_decimal = numero_decimal // 2
        return resultado

    elif base == 8:
        resultado = ''
        if numero_decimal == 0:
            resultado = '0'
        while numero_decimal > 0:
            residuo = numero_decimal % 8
            resultado = str(residuo) + resultado
            numero_decimal = numero_decimal // 8
        return resultado

    elif base == 16:
        resultado = ''
        if numero_decimal == 0:
            resultado = '0'
        while numero_decimal > 0:
            residuo = numero_decimal % 16
            if residuo < 10:
                resultado = str(residuo) + resultado
            else:
                resultado = chr(ord('A') + residuo - 10) + resultado
            numero_decimal = numero_decimal // 16
        return resultado

    else:
        return '\nBase no válida. Debes seleccionar 2 para binario, 8 para octal o 16 para hexadecimal.'

def fibonacci(n):
    if n < 1:
        return "Por favor, ingresa un número mayor o igual a 1."
    else:
        a, b = 0, 1
        for fila in range(1, n + 1):
            print(a, end=" ")
            a, b = b, a + b
            if fila < n:
                print()

def temperaturas(temperatura, unidad_entrada):
    if unidad_entrada == 'C' or unidad_entrada == 'c':
        fahrenheit = (temperatura * 9/5) + 32
        kelvin = temperatura + 273.15
        return f'{temperatura} grados Celsius son {fahrenheit} grados Fahrenheit y {kelvin} Kelvin.'
    elif unidad_entrada == 'F' or unidad_entrada == 'f':
        celsius = (temperatura - 32) * 5/9
        kelvin = (temperatura - 32) * 5/9 + 273.15
        return f'{temperatura} grados Fahrenheit son {celsius} grados Celsius y {kelvin} Kelvin.'
    elif unidad_entrada == 'K' or unidad_entrada == 'k':
        celsius = temperatura - 273.15
        fahrenheit = (temperatura - 273.15) * 9/5 + 32
        return f'{temperatura} Kelvin son {celsius} grados Celsius y {fahrenheit} grados Fahrenheit.'
    else:
        return 'Unidad de temperatura no válida. Debes ingresar C, F o K.'

def gradrad(val):
    grados = val
    radianes = grados * (math.pi / 180)
    print(f'{grados} grados son aproximadamente {radianes:.2f} radianes.')

    radianes = val
    grados = radianes * (180 / math.pi)
    return f'{radianes} radianes son aproximadamente {grados:.2f} grados.'

def IMCD(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def bisc(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return f'{ano} es un año bisiesto.'
    else:
        return f'{ano} no es un año bisiesto.'

def ene(n):
    if n <= 0:
        return 'Por favor, ingresa un número entero positivo.'
    else:
        suma_armónica = 0.0

        for i in range(1, n + 1):
            suma_armónica += 1 / i

        print(f'El n-ésimo número armónico H_{n} es aproximadamente: {suma_armónica:.5f}')
"""
n = int(input("Ingresa un número entero positivo (n) para calcular el n-ésimo número armónico: "))
"""

"""
#-----------------------------------------------------------
numero_decimal = int(input("Ingresa un número decimal: "))
base = int(input("Selecciona la base de conversión (2 para binario, 8 para octal, 16 para hexadecimal): "))
print(conversion_entrebases(numero_decimal, base))

#-----------------------------------------------------------
n = int(input("Introduce el número de filas para generar la serie de Fibonacci: "))
print(fibonacci(n))

#-----------------------------------------------------------
temperatura = float(input("Ingresa la temperatura: "))
unidad_entrada = input("Ingresa la unidad de temperatura (C/F/K): ")
print(temperaturas(temperatura, unidad_entrada))
"""
#-----------------------------------------------------------
val = int(input("Ingresa un número: "))
print(gradrad(val))
"""
#-----------------------------------------------------------
peso = float(input("Ingresa tu peso en kilogramos: "))
altura = float(input("Ingresa tu altura en metros: "))

print('Tu índice de masa corporal (IMC) es:', IMCD (peso, altura))

#-----------------------------------------------------------
ano = int(input("\nIngrese un año: "))
print(bisc(ano))

#-----------------------------------------------------------

"""