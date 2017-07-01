def esta_ordenada(secuencia):
	'''Recibe una secuencia e indica si está ordenada de menor a mayor o no'''
	anterior = secuencia[0]
	for elem in secuencia:
		if elem < anterior:
			return False
	return True		

'''print("La tupla (1, 1, 2, 3, 3, 4, 5) está ordenada?", esta_ordenada((1, 1, 2, 3, 3, 4, 5)))
print("La tupla (1, 2, 3, 4, 5) está ordenada?", esta_ordenada((1, 2, 3, 4, 5)))
print("La tupla (3, 2, 2, 6, 4, 4, 5) está ordenada?", esta_ordenada((3, 2, 2, 6, 4, 4, 5)))
print("La tupla (5, -3, 2, 3, 3, 4, 5) está ordenada?", esta_ordenada((5, -3, 2, 3, 3, 4, 5)))
print("La tupla (-2, 0, 1, 3, 6) está ordenada?", esta_ordenada((-2, 0, 1, 3, 6)))'''                  #PRUEBA (quitar comillas)

