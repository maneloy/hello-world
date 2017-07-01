def es_entero(cadena):
    cifras = '0123456789'
    for c in cadena:
        if not c in cifras:
            return False
    return True

def aux(valor_aux, min, max):
    while es_entero(valor_aux) == False:
        valor_aux = input('Debe ser entero, ingrese otro valor: ')
        if es_entero(valor_aux) == True:
            while not int(valor_aux) >= min or not int(valor_aux) <= max:
                valor_aux = input('Debe estar entre el minimo y el maximo, ingrese otro valor: ')
                while es_entero(valor_aux) == False:
                    valor_aux = input('Debe ser entero, ingrese otro valor: ')
    return valor_aux

def pedir_entero(mensaje, min, max):
    print(mensaje)
    valor = input('Ingrese un valor: ')
    valor = aux(valor, min, max)
    if not int(valor) >= min or not int(valor) <= max:
        valor = input('Debe estar entre el minimo y el maximo, ingrese otro valor: ')
        valor = aux(valor, min, max)       
    return valor
     
