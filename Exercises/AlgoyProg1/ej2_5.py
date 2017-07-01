def calc_num_tri(n):
	suma = 0
	for i in range(1, n+1):
		suma+=i
	return suma
	
def pedir_int():
	nro = int(input("Ingrese un número: "))
	return nro

def main():
	n = pedir_int()
	for i in range(1, n+1):
		print("{} - {}".format(i, calc_num_tri(i)))

main()