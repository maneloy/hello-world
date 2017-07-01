def examenes(cantidad, porcentaje_aprobacion):
	'''Dada la cantidad de ejercicios de un examen y el porcentaje de ejercicios necesarios para aprobar, muestra por pantalla el porcentaje de ejercicios resueltos e indica si el alumno aprobo.'''
	ejercicios_resueltos = input('Ingrese la cantidad de ejercicios resueltos por el alumno(* si no quedan examenes a revisar): ')
	while ejercicios_resueltos != '*':
		centinela = int(ejercicios_resueltos)
		porcentaje_resuelto = centinela * 100 / cantidad
		print('El porcentaje de ejercicios resueltos es {}%'.format(porcentaje_resuelto))
		if porcentaje_resuelto >= porcentaje_aprobacion:
			print('El alumno aprobo el examen')
		else:
			print('El alumno desaprobo el examen')
		ejercicios_resueltos = input('Ingrese la cantidad de ejercicios resueltos por el siguiente alumno(* si no quedan examenes a revisar): ')
	print('No se revisaran mas examenes')
			
examenes(5, 60) #En este caso se deben aprobar 3 ejercicios de 5