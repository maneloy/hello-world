def pedir_float():
	nro = float(input("Ingrese un número: "))
	return nro
	
def fac(n):
	cel = (n-32) * 5/9
	return cel
	
print(fac(pedir_float()))
