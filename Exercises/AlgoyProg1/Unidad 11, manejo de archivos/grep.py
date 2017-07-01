def grep(file, exp):
	"""Recibe un archivo y una expresión e imprime las líneas del archivo que la contienen"""
	with open(file) as archivo:
		for linea in archivo:
			linea = linea.rstrip("\n")
			if exp in linea: print(linea)

grep("c:\\users\\usuario\desktop\martin_fierro.txt", "cantar")