def cuantos_multiplos(a, b):
	'''Recibe dos parametros numericos a y b, y devuelve cuantos multiplos de a hay, que sean menores que b'''
	contador = 0
	for x in range(2, b):
		mult = x
		if a * mult < b:
			contador += 1			
	return contador

def cuantos_multiplos2(a, b):
	mult = 2
	n = a * mult
	contador = 0
	while n < b:
		contador += 1
		mult += 1
		n = a * mult
	return contador

	

