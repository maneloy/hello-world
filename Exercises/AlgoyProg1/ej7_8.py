def invertir_lista(lista):
	'''Devuelve una lista igual a la ingresada por el usuario, pero invertida.'''
	return lista[::-1]

def invertir_lista2(lista):
	'''Modifica la lista ingresada por el usuario, invirtiéndola.'''
	for i in range(len(lista)//2):
		lista[i], lista[-1-i] = lista[-1-i], lista[i]
	return lista

