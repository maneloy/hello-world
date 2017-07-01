def separar_cadena(cadena, sep, inserciones_maximas):
    cadena_final = ""
    contador = 0
    maximo = 0
    for letra in cadena:
        if contador == len(cadena) - 1: 
            cadena_final += letra
        elif maximo < inserciones_maximas:
            maximo += 1
            cadena_final += letra + sep
        else:
            cadena_final += letra       
        contador += 1
    return cadena_final

def reemplazar_espacios(cadena, char, inserciones_maximas):
    cadena_final = ""
    maximo = 0
    for letra in cadena:        
        if letra != ' ':
            cadena_final += letra
        elif maximo < inserciones_maximas:
            maximo += 1
            cadena_final += char
        else:
            cadena_final += letra
    return cadena_final

def reemplazar_digitos(cadena, char, reemplazos_maximos):
    cadena_final = ""
    maximo = 0
    for letra in cadena:
        if letra.isdigit() and maximo < reemplazos_maximos:
            cadena_final += char
            maximo += 1
        else:
            cadena_final += letra
    return cadena_final

def insertar_caracter_cada3(cadena, char, inserciones_maximas):
    cadena_final = ""
    contador = 0
    maximo = 0
    for letra in cadena:
        if contador == 3 and maximo < inserciones_maximas:
            cadena_final += char
            contador = 0
            maximo += 1
        contador += 1
        cadena_final += letra
    return cadena_final
