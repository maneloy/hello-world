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

def buscar(lista, elem): #lista debe estar ordenada
'''Busca el elemento indicado en la lista ordenada indicada. Si está, devuelve la posición. Si no está, lo inserta y devuelve esa nueva posición generada.'''

	posicion = busqueda_binaria(lista, elem)

	if posicion == -1:
		i = 0
		while lista[i] < elem:
			i += 1
		lista.insert(i, elem)
		return i

	return posicion

###### PRUEBA ######

listita = [0, 1, 2, 3, 4, 5, 7, 8, 9, 10, 11]

print(listita)

print(buscar(listita, 6))

print(listita)