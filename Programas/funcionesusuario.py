"""
def suma(x, y):
    print(x+y)

def div1(x, y):
    return x/y

y = 1
x = 10
res = div1(y,x)
print(res)

res1 = div1(y=10, x=2)
print(res1)

res2 = div1(x, y=10)
print(res2)"""

def conversion_dec_bin(numero_decimal):
    # x es el numero base 10 y se convertira a binario
    binario = ''

    if numero_decimal == 0:
        binario = '0'

    while numero_decimal > 0:
        residuo = numero_decimal % 2
        binario = str(residuo) + binario
        numero_decimal = numero_decimal // 2

    return binario

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