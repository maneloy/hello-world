def separar_cadena(cadena, sep):
    cadena_final = ""
    contador = 0
    for letra in cadena:
        if contador == len(cadena) - 1: 
            cadena_final += letra
        else:
            cadena_final += letra + sep
        contador += 1
    return cadena_final

def reemplazar_espacios(cadena, char):
    cadena_final = ""
    for letra in cadena:
        if letra != ' ':
            cadena_final += letra
        else:
            cadena_final += char
    return cadena_final

def reemplazar_digitos(cadena, char):
    cadena_final = ""
    for letra in cadena:
        if letra.isdigit():
            cadena_final += char
        else:
            cadena_final += letra
    return cadena_final

def insertar_caracter_cada3(cadena, char):
    cadena_final = ""
    contador = 0
    for letra in cadena:
        if contador == 3:
            cadena_final += char
            contador = 0
        contador += 1
        cadena_final += letra
    return cadena_final
