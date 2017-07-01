def tarifador1():
	p = float(input('Ingrese la tarifa:' ))
	i = int(input('Cuántos llamados?: '))
	num_llamadas = 0
	costo_total = 0
	for j in range(i):
		num_llamadas += 1
		h = int(input('Cuántas horas?: '))
		m = int(input('Cuántos minutos?: '))
		s = int(input('Cuántos segundos?: '))
		duracion = h * 3600 + m * 60 + s
		costo = duracion * p
		costo_total += costo
		print('La duración es {} segundos y el costo es de {} pesos'.format(duracion, costo))
	print('La cantidad de llamadas es {} y el costo total es de {} pesos'.format(num_llamadas, costo_total))
		
def tarifador2():
	p = float(input('Ingrese la tarifa: '))
	seguir = 'Si'
	num_llamadas = 0
	costo_total = 0
	while seguir == 'Si':
			num_llamadas += 1
			h = int(input('Cuántas horas?: '))
			m = int(input('Cuántos minutos?: '))
			s = int(input('Cuántos segundos?: '))
			duracion = h * 3600 + m * 60 + s
			costo = duracion * p
			print('La duración es {} segundos y el costo es de {} pesos'.format(duracion, costo))
			seguir = input('Desea seguir? <Si-No>: ')
			costo_total += costo
	print('La cantidad de llamadas es {} y el costo total es de {} pesos'.format(num_llamadas, costo_total))
	
def tarifador3():
	p = float(input('Ingrese la tarifa: '))
	horas = input('Cuántas horas? (* para salir): ')
	num_llamadas = 0
	costo_total = 0
	while horas != '*':			
			num_llamadas += 1
			h = int(horas)
			m = int(input('Cuántos minutos?: '))
			s = int(input('Cuántos segundos?: '))
			duracion = h * 3600 + m * 60 + s
			costo = duracion * p
			costo_total += costo
			print('La duración es {} segundos y el costo es de {} pesos'.format(duracion, costo))
			horas = input('Cuántas horas? (* para salir): ')
	print('La cantidad de llamadas es {} y el costo total es de {} pesos'.format(num_llamadas, costo_total))
	
def tarifador4():
	p = float(input('Ingrese la tarifa: '))
	num_llamadas = 0
	costo_total = 0
	while True:			
			horas = input('Cuántas horas? (* para salir): ')
			if horas == "*":
				break
			num_llamadas += 1
			h = int(horas)	
			m = int(input('Cuántos minutos?: '))
			s = int(input('Cuántos segundos?: '))
			duracion = h * 3600 + m * 60 + s
			costo = duracion * p
			costo_total += costo
			print('La duración es {} segundos y el costo es de {} pesos'.format(duracion, costo))
	print('La cantidad de llamadas es {} y el costo total es de {} pesos'.format(num_llamadas, costo_total))		
	
tarifador4()

