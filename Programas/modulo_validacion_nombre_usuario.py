def validar_nombre_usuario(nombre_usuario):
    if len(nombre_usuario) < 6:
        return "El nombre de usuario debe contener al menos 6 caracteres"
    elif len(nombre_usuario) > 12:
        return "El nombre de usuario no puede contener más de 12 caracteres"
    else:
        for caracter in nombre_usuario:
            if not caracter.isalnum():
                return "El nombre de usuario puede contener solo letras y números"
        return True

while True:
    nombre = input("Ingrese su nombre de usuario: ")
    resultado = validar_nombre_usuario(nombre)

    if resultado == True:
        print("Nombre de usuario válido.")
        break  
    else:
        print(resultado)
        print("Por favor, vuelva a intentarlo.")
