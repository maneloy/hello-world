def pedir_voto(nombres):
	'''Recibe nombres en forma de tupla y le pide a cada uno su voto'''
	for elem in nombres:
		if elem[1] == "m":
			print("Estimado {}, vote por mí.".format(elem[0]))
		elif elem[1] == "f":
			print("Estimada {}, vote por mí.".format(elem[0]))

def pedir_voto2(nombres, p, n):
	pedir_voto(nombres[p: p + n])

pedir_voto2((("Juan Perez", "m"), ("Maria Hacker", "f"), ("Emma Stone", "f"), ("Donald Trump", "m"), ("Robbie Rotten", "m")), 1, 3)

