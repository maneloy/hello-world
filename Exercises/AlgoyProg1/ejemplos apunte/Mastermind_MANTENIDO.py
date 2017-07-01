import random

def mastermind():
	"""Funcion principal del juego Mastermind"""
	print("Bienvenido a Mastermind!")
	print("Tienes que adivinar un numero")
	
	codigo, propuesta, long = elegir_codigo()
	intentos = 1
	ME_DOY = "Me doy"
	
	while propuesta != codigo and propuesta != ME_DOY:
		intentos += 1
		aciertos, coincidencias = analizar_propuesta(propuesta, codigo, long)
		print("Tu propuesta {} tiene {} aciertos y {} coincidencias".format(propuesta, aciertos, coincidencias))
		propuesta = input("Propone otro codigo: ")
	
	if propuesta == ME_DOY:
		print("Mala suerte! El codigo era: {}".format(codigo))
	else:
		print("Felicitaciones! Adivinaste el codigo en {} intentos.".format(intentos))

def elegir_codigo():
	"""Devuelve un codigo de tantos digitos como el usuario haya ingresado la primera vez, elegido al azar"""
	digitos = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
	codigo = ''
	propuesta = input("Que codigo propones?: ")
	long = len(propuesta)
	for i in range(long):
		candidato = random.choice(digitos)
		codigo += candidato
	print("DEBUG EL CODIGO ES {}".format(codigo)) # DEBUG DEBUG DEBUG
	return codigo, propuesta, long
	
def analizar_propuesta(propuesta, codigo, long):
	"""Determina la cantidad de aciertos y coincidencias"""
	aciertos = 0
	coincidencias = 0
	for i in range(long):
		if propuesta[i] == codigo[i]:
			aciertos += 1
		elif propuesta[i] in codigo:
			coincidencias += contar_coincidencias(propuesta[i], codigo) ## HAY QUE VER QUÉ CRITERIO SE TIENE PARA LAS COINCIDENCIAS (SOLO UNA POR NUMERO??) 
	return aciertos, coincidencias
	
def contar_coincidencias(numero, secuencia):
	counter = 0
	for c in secuencia:
		if c == numero:
			counter += 1
	return counter

mastermind()

input("Presiona enter para salir.")