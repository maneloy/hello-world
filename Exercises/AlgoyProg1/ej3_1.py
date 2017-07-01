def a_segundos(intervalo):
	h, m, s = intervalo
    segundos = 3600 * h + 60 * m + s
    return segundos

def a_hms(segundos):
    h = segundos // 3600
    m = (segundos % 3600) // 60
    s = (segundos % 3600) % 60
    return h, m, s
    