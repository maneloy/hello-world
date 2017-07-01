def area_rectangulo():
	x1 = int(input("Ingrese x1: "))
	x2 = int(input("Ingrese x2: "))
	y1 = int(input("Ingrese y1: "))
	y2 = int(input("Ingrese y2: "))
	area= abs((x2-x1)*(y2-y1))
	print("El area del rectángulo es", area)
	
area_rectangulo()
