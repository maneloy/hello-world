def anio_bisiesto(anio):
    '''Indica si el año ingresado es bisiesto.'''
    return anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)

def dias_en_mes(mes, anio):
    '''Indica cuántos días hay en un mes dado, tomando en consideración el año para definir los días de febrero.'''
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        return 31
    if mes == 4 or mes == 6 or mes == 9 or mes == 11:
        return 30
    if anio_bisiesto(anio) == True:
        return 29
    else:
        return 28

def fecha_valida(dia, mes, anio):
    '''Indica si la fecha ingresada por el usuario es válida.'''
    if dia <= 0 or mes <= 0 or mes > 12:
        return False    
    if dia > dias_en_mes(mes, anio):
        return False
    return True

def dias_faltantes_mes(dia, mes, anio):
    '''Dada una fecha, indica cuántos días faltan para llegar a fin de mes.'''
    if not fecha_valida(dia, mes, anio):
        print('Fecha inválida')
        return
    dias_faltantes = dias_en_mes(mes, anio) - dia
    return dias_faltantes

def dias_transcurridos(dia, mes, anio):
    '''Dada una fecha, indica cuántos días transcurrieron en el año hasta esa fecha.'''
    if not fecha_valida(dia, mes, anio):
        print('Fecha inválida')
        return
    dias_hasta_mes = 0
    if anio_bisiesto(anio) == True:
        dias_anio = 366
    else:
        dias_anio = 365
    for x in range(1, mes):
        dias_hasta_mes += dias_en_mes(x, anio)
    dias_hasta_fecha = dias_hasta_mes + dia
    return dias_hasta_fecha

def dias_faltantes_anio(dia, mes, anio):
    '''Dada una fecha, indica cuántos días faltan para llegar a fin de año.'''
    if not fecha_valida(dia, mes, anio):
        print('Fecha inválida')
        return
    if anio_bisiesto(anio) == True:
        dias_anio = 366
    else:
        dias_anio = 365
    dias_faltantes_anio = dias_anio - dias_transcurridos(dia, mes, anio)
    return dias_faltantes_anio

def tiempo_transcurrido(dia1, mes1, anio1, dia2, mes2, anio2):
    '''http://es.calcuworld.com/calendarios/calculadora-de-tiempo-entre-dos-fechas/'''
    dias_t = dias_transcurridos(dia2, mes2, anio2) - dias_transcurridos(dia1, mes1, anio1)
    meses_t = mes2 - mes1 #Si da negativo, significa que tenes una situacion tipo 20 diciembre - 10 enero del año siguiente
    dias_s = dia1 + (dias_en_mes(mes2,anio2) - dia2)
    anios_t = anio2 - anio1
    p = 0
    if meses_t<0:
        meses_t = 0
        anios_t-=1
        dias_t = dias_faltantes_anio(dia1, mes1, anio1) + dias_transcurridos(dia2, mes2, anio2)
        for x in range(mes1, 12): # No sé si es 12 o 13
            meses_t+=1
        for y in range(1, mes2):
            meses_t+=1
        return anios_t, meses_t, dias_t
    for x in range(mes1, mes2):
        p+= dias_en_mes(x, anio1)   #Se empieza a desfasar cuando pasan los años. Por qué?

    dias_t = dias_faltantes_mes(dia1, mes1, anio1) + dia2 + 1 
    
    return anios_t, meses_t, dias_t   
            
                

    