def imprimir_extremo(a, b, c):
	'''Asumimos a =/= 0'''
	y_ext = c - (b**2 / 4 * a)
	x_ext = -b / (2 * a)
	if a > 0:
		print("El mínimo es:", x_ext, y_ext)
	else:
		print("El máximo es:", x_ext, y_ext)
