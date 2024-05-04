import funcionesusuario
"""
decimal = int(input("Ingrese un número decimal: "))
binario = bin(decimal)
print("El número binario es:", binario)
"""
#-----------------------------------------------------------

numero_decimal = int(input("Ingresa un número decimal: "))

print(funcionesusuario.conversion_dec_bin(numero_decimal))


""""
numero_decimal = int(input("Ingresa un número decimal: "))
base = int(input("Selecciona la base de conversión (2 para binario, 8 para octal, 16 para hexadecimal): "))

print(funcionesusuario.conversion_entrebases(numero_decimal, base))


if base == 2:
    resultado = ''
    if numero_decimal == 0:
        resultado = '0'
    while numero_decimal > 0:
        residuo = numero_decimal % 2
        resultado = str(residuo) + resultado
        numero_decimal = numero_decimal // 2
    print(f'El número binario equivalente es: {resultado}')

elif base == 8:
    resultado = ''
    if numero_decimal == 0:
        resultado = '0'
    while numero_decimal > 0:
        residuo = numero_decimal % 8
        resultado = str(residuo) + resultado
        numero_decimal = numero_decimal // 8
    print(f'El número octal equivalente es: {resultado}')

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
    print(f'El número hexadecimal equivalente es: {resultado}')

else:
    print('Base no válida. Debes seleccionar 2 para binario, 8 para octal o 16 para hexadecimal.')
"""