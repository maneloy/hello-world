def promedio_notas():
	seguir = 'si'
	total = 0
	n = 0
	while seguir == 'si':
		n += 1
		nota = int(input('Ingrese una nota: '))
		total += nota
		promedio = total / n
		print('Promedio: ', promedio)
		seguir = input('Desea seguir? <si-no>: ')
		
promedio_notas()