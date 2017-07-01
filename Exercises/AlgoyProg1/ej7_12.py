def map(f, list):
	'''Devuelve una lista compuesta de los elementos de 'list' evalaudos en f'''
	nlist = []
	for elem in list:
		nlist.append(f(elem))
	return nlist

def filter(f, list):
	'''Dada una lista y una funcion booleana, devuelve los elementos de la lista que cumplan la funcion'''
	nlist = []
	for elem in list:
		if f(elem):
			nlist.append(elem)
	return nlist
