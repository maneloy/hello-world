def empaquetar_lista(lista):
	contador = 1
	anterior = None
	lista_empaquetada = []
	for elem in lista:
		if anterior == None:
			anterior = elem
			continue
		if elem == anterior:
			contador += 1
		else:
			lista_empaquetada.append((anterior, contador))
			anterior = elem
			contador = 1
	lista_empaquetada.append((anterior, contador))
	return lista_empaquetada

print(empaquetar_lista([1, 1, 1, 3, 5, 1, 1, 3, 3])) #Prueba