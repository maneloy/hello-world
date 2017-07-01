def a_segundos(horas,minutos,segundos):
	"""Transforma en segundos una medida de tiempo expresada en horas, minutos y segundos"""
	return 3600 * horas + 60 * minutos + segundos

def main():
	"""Lee tres tiempos expresados en horas, minutos y segundos, y muestra en pantalla la conversión a segundos"""
	for x in range(3):
		h = int(input("Cuántas horas?: "))
		m = int(input("Cuántos minutos?: "))
		s = int(input("Cuántos segundos?: "))
		print("Son", a_segundos(h,m,s), "segundos")
		
main()

