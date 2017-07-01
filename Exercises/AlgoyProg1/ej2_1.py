def a_pc(n):
	'''Convierte un número real de pesos en pesos y centavos'''
	cent = n * 100
	p = cent//100
	c = cent % 100
	return p, c

def interes():
	cap = float(input("Ingrese el capital inicial: "))
	interes = float(input("Ingrese la tasa de interés: "))
	n_an = float(input("¿Cuántos años?: "))
	
	Cn = cap * ((1 + interes/100) ** n_an)
	
	pesos, centavos = a_pc(Cn)
	
	pesitos = int(pesos)
	centavitos = int(centavos)
	
	print("El monto final a obtener es", pesitos, "pesos con", centavitos, "centavos.")
	
interes()