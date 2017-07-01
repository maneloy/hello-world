def a_segundos(horas, minutos, segundos):
	"""Transforma en segundos una medida de tiempo expresada en horas, minutos y segundos"""
	return 3600 * horas + 60 * minutos + segundos

def main():
	"""El usuario ingresa la tarifa por segundo, cuántas comunicaciones se realizaron, y la duración de cada comunicación expresada en horas, minutos y segundos. Como resultado se informa la duración en segundos de cada comunicación y su costo."""
	total = 0
	p = float(input("¿Cuánto cuesta 1 segundo de comunicación?: "))
	n = int(input("¿Cuántas comunicaciones hubo?: "))
	for x in range (n):
		h = int(input("¿Cuántas horas?: "))
		m = int(input("¿Cuántos minutos?: "))
		s = int(input("¿Cuántos segundos?: "))
		duracion = a_segundos(h,m,s)
		costo = duracion * p
		cent = costo * 100
		pe = int(cent // 100)
		ce = int(cent % 100)
		print("Duración:", duracion, "segundos. Costo:", pe, "pesos con", ce, "centavos." )
		total += costo
		tcent = total * 100
		tpe = tcent // 100
		tce = tcent % 100
	print("El total facturado en la corrida es de", tpe, "pesos con", tce, "centavos.") 

main()

