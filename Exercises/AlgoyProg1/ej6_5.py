def devolver_primera_letra(cadena):
    nueva_cadena = ""
    if cadena[0] != " ":
        nueva_cadena += cadena[0]
    else:
        nueva_cadena += cadena[1]
    for i in range(1, len(cadena)):
        if cadena[i] == " ":
            nueva_cadena += cadena[i+1]
    return nueva_cadena

def devolver_primera_letra_mayusculas(cadena):
    nueva_cadena = ""
    if cadena[0] != " ":
        nueva_cadena += cadena[0].upper()
    else:
        nueva_cadena += cadena[1].upper()
    for i in range(1, len(cadena)):
        if cadena[i] == " ":
            nueva_cadena += cadena[i+1].upper()
    return nueva_cadena

def palabras_comienzan_a(cadena):
    nueva_cadena = ""
    index = 0

    if cadena[0] == "a" or cadena[0] == "A":    ##GUARDA CON ESTA SECCION
        while cadena[index] != " ":
            nueva_cadena += cadena[index]
            index += 1
            if index == len(cadena):
                break
        nueva_cadena += " "
    
    while index < len(cadena):
        
        while not (cadena[index] == " " and cadena[index + 1] == "a") and not (cadena[index] == " " and cadena[index + 1] == "A"):
            index += 1
            if index == len(cadena):
                return nueva_cadena
            
        index += 1
        
        while cadena[index] != " ":
            nueva_cadena += cadena[index]
            index += 1
            if index == len(cadena):
                break
            
        nueva_cadena += " "
        
    return nueva_cadena

print(palabras_comienzan_a('Antes de amigo alimania me encanta la albaca hola')) ##DEVUELVE CON UN ESPACIO AL FINAL; HAY QUE VER COMO ARREGLO ESO



