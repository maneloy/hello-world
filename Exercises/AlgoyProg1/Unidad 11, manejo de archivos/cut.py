def cut(archivo, sep, campos):
	"""Recibe un archivo, un separador, y una lista
		de campos, e imprime en el archivo los campos
		separados por el separador indicado."""
	nueva_lista = []
	for x in campos:
		nueva_lista.append(str(x))
	nueva_cadena = sep.join(nueva_lista)
	recipiente = open(archivo, "w")
	recipiente.write(nueva_cadena)
	recipiente.close()

cut("c:\\users\\usuario\desktop\prueba.txt", "-", ["hola", 1, "chau", 2.32, "megamente"])