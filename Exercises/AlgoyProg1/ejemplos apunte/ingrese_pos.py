def ingrese_positivo1():
	seguir = 'si'
	while seguir == 'si':
		n = int(input('Ingrese un numero positivo: '))
		if n>0:
			print('Correcto.')
			break			
		else:
			print('El número ingresado no es positivo: ')
			seguir = input('Desea intentar de nuevo? <si-no>: ')

def ingrese_positivo2():
	centinela = int(input('Ingrese un número positivo: '))
	if centinela > 1:
		print('Correcto.')
		return 
	while centinela<=0:
		centinela = int(input('No es correcto. Ingrese un número positivo: '))
	print('Correcto.')
	return

def ingrese_positivo3():
	while True:
		n = int(input('Ingrese un número positivo: '))
		if n>0:
			print('Correcto.')
			break
		print('No es correcto.')		
		
ingrese_positivo3()
