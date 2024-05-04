def convertir(segundos):
    resultado = []
    if segundos >= 86400:
        dias = segundos // 86400
        resultado.append(dias,"día(s)")
        segundos %= 86400
    elif segundos >= 3600:
        horas = segundos // 3600
        resultado.append(horas,"hora(s)")
        segundos %= 3600  # Actualiza los segundos restantes
    elif segundos >= 60:
        minutos = segundos // 60
        resultado.append(minutos,"minuto(s)")
        segundos %= 60  # Actualiza los segundos restantes
    elif segundos > 0:
        resultado.append(segundos,"segundo(s)")

    return resultado


segundos = int(input("Ingresa la cantidad de segundos: "))
print(convertir(segundos))
