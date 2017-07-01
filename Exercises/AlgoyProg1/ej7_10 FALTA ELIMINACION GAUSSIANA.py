from math import ceil

def suma_vectores(vector1, vector2):
	nuevo_vector = []
	for i in range(len(vector1)):
		suma = vector1[i] + vector2[i]
		nuevo_vector.append(suma)
	return tuple(nuevo_vector)

def norma(vector):
	auxiliar = 0
	for elem in vector:
		auxiliar += elem ** 2
	return auxiliar ** (1/2)

def son_paralelos(vector1, vector2):
	dot_product = producto_escalar(vector1, vector2)
	norma1 = norma(vector1)
	norma2 = norma(vector2)
	prod_normas = norma1 * norma2
	return abs(dot_product) == ceil(prod_normas)

def producto_escalar(vector1, vector2):
	producto = 0
	for i in range(len(vector1)):
		producto += vector1[i] * vector2[i]
	return producto

def suma_matrices(matriz1, matriz2):
	'''Dadas dos matrices definidas por una lista de tuplas, siendo cada tupla una fila, devuelve la suma'''
	matriz_suma = []
	for i in range(len(matriz1)):
		fila = suma_vectores(matriz1[i], matriz2[i])
		matriz_suma.append(fila)
	return matriz_suma

def transponer_matriz(matriz):
	'''Toma una matriz en la forma de una lista con tuplas que representan cada fila, y devuelve otra lista cuyas tuplas representan las columnas'''
	matriz_por_columnas = []
	auxiliar = []
	j = 0
	while j < len(matriz[0]):
		for i in range(len(matriz)):
			auxiliar.append(matriz[i][j])
		matriz_por_columnas.append(tuple(auxiliar))
		auxiliar = []
		j += 1
	return matriz_por_columnas
		
def producto_matrices(matriz1, matriz2):
	'''Dadas dos matrices definidas por una lista de tuplas, siendo cada tupla una fila, devuelve el producto'''
	producto = []
	auxiliar = []
	matriz2_transpuesta = transponer_matriz(matriz2)
	c1 = 0
	while c1 < len(matriz1):		
		for j in range(len(matriz2_transpuesta)):
			auxiliar.append(producto_escalar(matriz1[c1], matriz2_transpuesta[j]))
		producto.append(tuple(auxiliar))
		auxiliar = []
		c1 += 1
	return producto
    
def son_linealmente_independientes(vectores):
	'''Recibe una lista de tuplas representando vectores e indica si son linealmente independientes'''
	anterior = vectores[0]
	for vector in vectores:
		if not son_paralelos(vector, anterior):
			return False
		anterior = vector
	return True

def eliminacion_gaussiana(matriz): #https://en.wikipedia.org/wiki/Gaussian_elimination#Pseudocode
	'''Triangula una matriz (dada por una lista de tuplas que representan filas) mediante el metodo de Gauss-Jordan'''
	m = len(transponer_matriz(matriz)[0]) #Filas
	n = len(matriz[0]) #Columnas
	for k in range(1, min(m, n)):
		

