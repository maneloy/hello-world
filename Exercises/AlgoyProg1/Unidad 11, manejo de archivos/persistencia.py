def cargar_datos(arch):
	"""Recibe un archivo cuyo contenido tiene formato
		'clave, valor' y devuelve un diccionario cuyas claves y valores
		se corresponden con las del archivo"""
	d = {}
	with open(arch) as archivo:
		for linea in archivo:
			linea = linea.rstrip("\n")
			item = linea.split(",", 1)
			clave, valor = item
			d[clave] = valor
	return d

def guardar_datos(dic, arch):
	"""Recibe un diccionario y un archivo, y guarda los datos
		del diccionario y del archivo en el formato 'clave, valor'""" 
	archivo = open(arch, "w")
	for clave, valor in dic.items():
		archivo.write("{},{}\n".format(clave, valor))
	archivo.close()

guardar_datos({"valor" : 1, "valor2" : 15, "valor3" : [1, 2, 3]}, "c:\\users\\usuario\desktop\datos.txt")