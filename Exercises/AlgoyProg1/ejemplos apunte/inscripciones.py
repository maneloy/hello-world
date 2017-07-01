def inscribir_alumnos():
	"""Permite inscribir alumnos al curso"""

	print("Inscripción en el curso de Algoritmos y Programación I")
	inscriptos = []
	while True:
		continuar = "no"
		padron = int(input("Ingresa un padrón. (<=0 para terminar): "))
		if padron <= 0:
			break
		for i in range(len(inscriptos)):
			if padron in inscriptos[i]:
				print("Este padrón ya está en la lista")
				continuar = "si"
		if continuar == "si":
			continue	
		nombre = input("Ingrese el nombre del alumno: ")
		apellido = input("Ingrese el apellido del alumno: ")
		inscriptos.append((padron, nombre, apellido))

	return inscriptos

def borrar_alumnos():
	inscriptos2 = inscriptos
	while True:
		encontro = "no"
		padron_b = int(input("Ingrese el padrón que desea borrar (<=0 para salir): "))
		if padron_b <= 0:
			break
		for i in range(len(inscriptos2)):
			if padron_b in inscriptos2[i]:
				inscriptos2.remove(inscriptos2[i])
				encontro = "si"
				break
		if not encontro == "si":
			print("Ese padrón no figura en la lista")	
			continue	
	return inscriptos2

inscriptos = inscribir_alumnos()
print("La lista de inscriptos es:", inscriptos)

intencion = input("Desea borrar alumnos? <si-no>: ")
if intencion == "si":
	print("La nueva lista de inscriptos es:", borrar_alumnos())

input("Enter para salir")