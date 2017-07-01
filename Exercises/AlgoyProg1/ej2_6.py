def factorial(n):
	factorial = 1
	for x in range(1, n+1):
		factorial*=x
	return factorial

def main():
	m = int(input("Cuántos valores va a ingresar?: "))
	for i in range(1, m+1):
		y = int(input("Ingrese un valor: "))
		print("Orden {} - El factorial de {} es {}".format(i, y, factorial(y)))
		
main()
	