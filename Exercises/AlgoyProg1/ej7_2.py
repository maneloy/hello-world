def fichas_encajan(ficha1, ficha2):
	'''Indica si dos fichas de domino indicadas por tuplas encajan o no'''
	for elem in ficha1:
		if elem in ficha2:
			return True
	return False

def fichas_encajan2(ficha1, ficha2):
	'''Indica si dos fichas de domino indicadas por cadenas (numeros separados por '-') encajan o no'''
	lista1 = ficha1.split('-')
	lista2 = ficha2.split('-')
	for elem in lista1:
		if elem in lista2:
			return True
	return False

