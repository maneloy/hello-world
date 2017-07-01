def agenda(lista, cadena):
	coincidencias = []
	for elem in lista:
		if cadena in elem[0]:
			coincidencias.append(elem)
	return coincidencias


