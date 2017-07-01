def mayor_producto(n1, n2, n3, n4):
	prod1 = n1 * n2
	prod2 = n1 * n3
	prod3 = n1 * n4
	prod4 = n2 * n3
	prod5 = n2 * n4
	prod6 = n3 * n4
	return max(prod1, prod2, prod3, prod4, prod5, prod6)


