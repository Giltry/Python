# Programa para convertir segundos a dias, horas, minutos y segundos
# segundos: 400000
# 400000 segundos son: 4 dias, 15 horas, 6 minutos y 40 segundos

def convertir_se(segundos):
    dias = segundos // 86400

    segundos_r = segundos % 86400
    horas = segundos_r // 3600

    segundos_r %= 3600
    minutos = segundos_r // 60

    segundos_r %= 60

    return f"{segundos}s son: {dias} dias, {horas} horas, {minutos} minutos y {segundos_r} segundos"

#-----------------------------------------------------------------------------------------------------
segundos = int(input("Ingresa la cantidad de segundos: "))
print(convertir_se(segundos))
