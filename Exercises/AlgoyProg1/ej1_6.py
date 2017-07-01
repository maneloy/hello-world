def imprime_palabra_1000_veces():
	'''Imprime una palabra mil veces en la misma linea.'''
	palabra = input("Escriba una palabra: ")
	for x in range(1,1001):
		print(palabra, end=' ')

imprime_palabra_1000_veces()