def pedir_int():
	nro = int(input("Ingrese un número: "))
	return nro

def par(n1, n2):
	n1 = n1 + n1%2
	for x in range(n1, n2+1, 2):
		print(x)
	
def main():
	ini = pedir_int()
	fin = pedir_int()
	print(par(ini, fin))
	
main()

