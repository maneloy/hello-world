def sumar_sucesion_naturales():
	n = int(input("Ingrese una sucesion de numeros naturales para sumar (-1 para salir): "))
	contador = 0
	total = 0
	while n != -1:
		if n <= 0:
			print("Debe ser natural")
			n = int(input("Ingrese un numero natural: "))
			continue
		if n == -1:
			break
		total += n
		contador += 1
		promedio = total/contador 
		n = int(input("Ingrese otro numero: "))
	print("Fueron ingresados {} numeros, la suma total es {} y el promedio es {}".format(contador, total, promedio))

sumar_sucesion_naturales()