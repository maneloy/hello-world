def pedir_interv():
    interv = eval(input("Ingrese un intervalo de tiempo en horas, minutos, segundos: "))
    return interv
    
def a_segundos(intervalo):
    h, m, s = intervalo
    segundos = 3600 * h + 60 * m + s
    return segundos

def a_hms(segundos):
    h = segundos // 3600
    m = (segundos % 3600) // 60
    s = (segundos % 3600) % 60
    return h, m, s
	
def main():
	interv1 = a_segundos(pedir_interv())
	interv2 = a_segundos(pedir_interv())
	total = interv1 + interv2
	horas, minutos, segundos = a_hms(total)
	print("El intervalo total de tiempo es de", horas, "horas,", minutos, "minutos y", segundos, "segundos.")
	
main()