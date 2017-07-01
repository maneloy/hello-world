def analisis_numerico(digito, natural):
    '''Recibe un digito y un numero natural, y decide numericamente si el digito se encuentra en la notacion decimal del natural'''
    auxiliar = natural                          #
    cont_aux = 0                                #
    while auxiliar > 1:                         #Encuentra la cantidad de dígitos en el natural.
        auxiliar = natural/(10**cont_aux)       #               
        cont_aux += 1                           #
    contador = cont_aux                         #
    divisor = 10 ** (contador - 1)
    restador = (natural // 10 ** contador) * 10
    while contador > 0:
        if digito == natural//divisor - restador:
            return True
        contador -= 1
        divisor = 10 ** (contador - 1)
        restador = (natural // 10 ** contador) * 10
    return False
	
