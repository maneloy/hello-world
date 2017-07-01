def ordenar_nombres(lista):
	lista_auxiliar = lista[:]
	for i in range(len(lista_auxiliar)):
		lista_auxiliar[i] = (lista_auxiliar[i][1], lista_auxiliar[i][2], lista_auxiliar[i][0])
	for i in range(len(lista_auxiliar)):
		lista_auxiliar[i] = " ".join(lista_auxiliar[i])
	for i in range(len(lista_auxiliar)):
		contador_espacios = 0
		nueva_lista = ""
		for char in lista_auxiliar[i]:
			if char == " " and contador_espacios == 1:
				nueva_lista += ". "
				contador_espacios += 1
			elif char == " ":
				contador_espacios += 1
				nueva_lista += " "
			else:
				nueva_lista += char
		lista_auxiliar[i] = nueva_lista
	return lista_auxiliar

print(ordenar_nombres([("Verea", "Juan", "E"), ("Chavez", "Paula", "C"), ("Simpson", "Homero", "J")]))






