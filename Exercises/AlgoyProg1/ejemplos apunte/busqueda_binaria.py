def busqueda_binaria(lista, x ):
	"""Búsqueda binaria

	Precondición: la lista está ordenada
	Devuelve -1 si x no está en la lista;
	Devuelve p tal que lista[p] == x, si x está en la lista
	"""

	izq = 0
	der = len(lista) - 1

	while izq <= der:
		medio = (izq + der) // 2 

		if lista[medio] == x:
			return medio

		elif lista[medio] > x:
			der = medio - 1

		else:
			izq = medio + 1

	return -1
