def devuelve_solo_consonantes(cadena):
    vocales = "aeiou"
    nueva_cadena = ""
    for letra in cadena:
        if not letra in vocales:
            nueva_cadena += letra
    return nueva_cadena

def devuelve_solo_vocales(cadena):
    vocales = "aeiou "
    nueva_cadena = ""
    for letra in cadena:
        if letra in vocales:
            nueva_cadena += letra
    return nueva_cadena

def reemplazar_vocales(cadena):
    nueva_cadena = ""
    vocales = "aeiou"
    for letra in cadena:
        if letra in vocales:
            if letra == "a":
                nueva_cadena += "e"
            if letra == "e":
                nueva_cadena += "i"
            if letra == "i":
                nueva_cadena += "o"
            if letra == "o":
                nueva_cadena += "u"
            if letra == "u":
                nueva_cadena += "a"
        else:
            nueva_cadena += letra
    return nueva_cadena

def sacar_espacios(cadena): #AUXILIAR PARA FUNCION ES_PALINDROMO
    nueva_cadena = ""
    for letra in cadena:
        if letra != " ":
            nueva_cadena += letra
    return nueva_cadena

def es_palindromo(cadena):
    return sacar_espacios(cadena[:]) == sacar_espacios(cadena[::-1])