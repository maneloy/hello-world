def wc(archivo):
	"""Procesa el archivo dado e imprime por pantalla cuántas líneas, palabras y carácteres contiene"""
	with open(archivo) as file:
		cont_lineas = 0
		cont_caracteres = 0
		cont_palabras = 0
		for line in file:
			cont_lineas += 1
			cont_caracteres += len(line)
			cont_palabras += len(line.split())
	print("Nº de lineas: {} \nNº de palabras: {} \nNº de caracteres: {}". format(cont_lineas, cont_palabras, cont_caracteres))

wc("c:\\users\\usuario\desktop\martin_fierro.txt")