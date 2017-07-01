def imprime_domino():
	n = int(input("Ingrese la cantidad máxima de puntos (siendo la cantidad normal para un domino igual a 6): "))
	for x in range(n+1):
		for y in range(x, n+1):
			print("{} {}".format(x, y))

imprime_domino()