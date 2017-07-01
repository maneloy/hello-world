def imprimir_cuadrados():
	print("Se calcularán cuadrados de números")
	n1 = int(input("Ingrese un número entero: "))
	n2 = int(input("Ingrese otro número entero: "))
	
	for x in range(n1,n2):
		print('El cuadrado de', x, 'es', x**2)
		
	print("Es todo por ahora.")

imprimir_cuadrados()