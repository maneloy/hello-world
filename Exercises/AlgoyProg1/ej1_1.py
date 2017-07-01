def saludar():
	'''Pregunta al usuario su nombre y luego lo saluda'''
	nombre = input("Cúal es su nombre? ")
	print("Hola",nombre + "!")
	
def producto():
	'''Pide al usuario que ingrese dos números y luego muestra su producto'''
	n1 = float(input("Ingrese un número: "))
	n2 = float(input("Ingrese otro número: "))
	print("El producto de", n1,"y", n2, "es", n1*n2)

saludar()
producto()
