def pedir_intervalo():
	"""Solicita un intervalo de tiempo en horas, minutos y segundos."""
	h = int(input("¿Cuántas horas?: "))
	m = int(input("¿Cuántos minutos?: "))
	s = int(input("¿Cuántos segundos?: "))
	return h, m, s

def a_segundos(horas, minutos, segundos):
	"""Transforma en segundos una medida de tiempo expresada en horas, minutos y segundos"""
	return 3600 * horas + 60 * minutos + segundos

def calcula_costo(duracion, tarifa):
	"""Calcula el costo de una llamada mediante la duración de la misma y la tarifa que corresponde."""
	costo = duracion * tarifa
	return costo

def pesos_centavos(pes):
	"""Separa una cantidad total con decimales de pesos en pesos y centavos."""
	cent = pes * 100	
	pesos = cent // 100
	centavos = cent % 100
	return int(pesos), int(centavos)
	
def main():
	"""El usuario ingresa la tarifa por segundo, cuántas comunicaciones se realizaron, y la duración de cada comunicación expresada en horas, minutos y segundos. Como resultado se informa la duración en segundos de cada comunicación y su costo."""
	
	total_c = 0
	total_l = 0
	num_c = 0
	num_l = 0

	print("Tarifa de llamadas largas (una hora o más): 1.2 pesos por segundo. Tarifa de llamadas cortas (menos de una hora): 0.4 pesos por segundo")
	
	n = int(input("¿Cuántas comunicaciones hubo?: "))
	for x in range (n):
		h, m, s = pedir_intervalo()
		duracion = a_segundos(h,m,s)
		if duracion >= 3600:
			num_l += 1
			p = 0.4
			costo_l = calcula_costo(duracion, p)
			total_l += costo_l
		else:
			num_c += 1
			p = 0.1
			costo_c = calcula_costo(duracion, p)
			total_c += costo_c
	
	largas_pesos, largas_centavos = pesos_centavos(total_l)
	cortas_pesos, cortas_centavos = pesos_centavos(total_c)
	total = total_l + total_c
	total_pesos, total_centavos = pesos_centavos(total)
	
	print("Número de llamadas cortas: ", num_c, "Precio de llamadas cortas: ", int(cortas_pesos), " pesos con ", int(cortas_centavos), " centavos.")
	print("Número de llamadas largas: ", num_l, "Precio de llamadas largas: ", int(largas_pesos), " pesos con ", int(largas_centavos), " centavos.")
	print("Total facturado: ", int(total_pesos), " pesos con ", int(total_centavos), " centavos.")
	input("Presione enter para salir.")
	
main()

