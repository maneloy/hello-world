def devolver_listas_partidas(lista, k):
	lista_mayores = []
	lista_menores = []
	lista_iguales = []
	for elem in lista:
		if elem > k:
			lista_mayores.append(elem)
		elif elem < k:
			lista_menores.append(elem)
		else:
			lista_iguales.append(elem)
	return lista_mayores, lista_menores, lista_iguales

def devolver_multiplos(lista, k):
	lista_multiplos = []
	for elem in lista:
		if elem % k == 0:
			lista_multiplos.append(elem)
	return lista_multiplos

