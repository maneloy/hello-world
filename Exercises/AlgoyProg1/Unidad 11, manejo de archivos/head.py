def head(file, n):
	"""Recibe la ruta de un archivo de texto, 
		o solo el nombre si se encuentra 
		en la misma carpeta que la consola,
		e imprime las primeras n lineas del archivo"""
	i = 0
	with open(file) as f:
		for line in f:
			line = line.rstrip("\n")
			print(line)
			i += 1
			if i == n: break

archivo = input("Ingrese la ruta del archivo: ")
numero = int(input("Ingrese cuantas lineas quiere imprimir: "))

print()
head(archivo, numero)

print()
input("Presione ENTER para salir\n")