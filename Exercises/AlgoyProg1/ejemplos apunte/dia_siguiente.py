def anio_bisiesto(anio):
    '''Indica si el año ingresado es bisiesto.'''
    return anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)
	
def dia_siguiente(fecha):
	d, m, a = fecha
	if (m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12) and d == 31:
		if m == 12:
			ds = 1
			ms = 1
			a_s = a + 1
		else:
			ds = 1
			ms = m + 1
			a_s = a
	elif (m == 4 or m == 6 or m == 9 or m == 11) and d == 30:
		ds = 1
		ms = m + 1
		a_s = a
	
	elif m == 2 and ((anio_bisiesto(a) and d == 29) or (not anio_bisiesto(a) and d == 28)): 
			ds = 1
			ms = 3
			a_s = a		
	else: 
		ds = d + 1
		ms = m
		a_s = a
	
	return ds, ms, a_s
	
