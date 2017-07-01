def palabras5letras(cadena):
	"""Dada una cadena de palabras espaciadas, devuelve cuántas palabras tienen 5 o más letras."""
	contador = 0
	palabras = cadena.split()
	for elem in palabras:
		if len(elem) >= 5:
			contador += 1
	return contador

