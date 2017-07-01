def busqueda_a(lista, elemento):
	cont = 0
	for x in lista:
		if elemento == x:
			cont += 1
	return cont

def busqueda_b(lista, elemento):
	i = 0
	for x in lista:
		if x == elemento:
			return i
		i += 1
	return -1

def busqueda_c(lista, elemento):
	auxiliar = lista
	coincidencias = []
	i = 0
	while elemento in lista:
		coincidencias.append(busqueda_b(auxiliar, elemento))
		auxiliar.insert(busqueda_b(auxiliar,elemento), '*placeholder**#@')
		auxiliar.remove(elemento)
	return coincidencias

lista = [1, 3, 2, 3, 4, 5, 5, 6, 7, 6, 5, 0, 8, 0, 5, 9, 10, 12, 11, 12, 13, 6] #Prueba