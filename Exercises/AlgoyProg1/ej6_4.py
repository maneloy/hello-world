def separar_miles(cadena):
    contador = 0
    nueva_cadena = ""
    for i in range(len(cadena) - 1, -1, -1):
        if contador == 2:
            contador = 0
            nueva_cadena += cadena[i] + '.'
        else:
            nueva_cadena += cadena[i]
            contador += 1
    return nueva_cadena[::-1]
