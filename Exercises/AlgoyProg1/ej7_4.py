def producto_escalar(vector1, vector2):
	producto = 0
	for i in range(len(vector1)):
		producto += vector1[i] * vector2[i]
	return producto

def son_ortogonales(vector1, vector2):
	return producto_escalar(vector1, vector2) == 0

def aux(a, b): # Para "son_paralelos"
	n = 1
	contador = 0
	while True:
		if b[0] * n == a[0]:
			multiplicador = n
			break
		else:
			n += 1
	while contador < len(a):
		if b[contador] * multiplicador == a[contador]:
			contador += 1
			if contador == len(a):
				return True
		else:
			return False

def son_paralelos(vector1, vector2):
	if vector1[0] % vector2[0] == 0:
		return(aux(vector1, vector2))
	if vector2[0] % vector1[0] == 0:
		return(aux(vector2, vector1))
	return False

def norma(vector):
	auxiliar = 0
	for elem in vector:
		auxiliar += elem ** 2
	return auxiliar ** (1/2)


