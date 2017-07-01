from random import randrange

def main():
	n = randrange(50)
	intento = int(input("Ingrese un numero: "))
	while intento != n:
		if intento>n:
			print('El numero {} es mayor que n'.format(intento))
		else:
			print('El numero {} es menor que n'.format(intento))
		intento = int(input("Intente de nuevo: "))
	print('Correcto!')
	
main()