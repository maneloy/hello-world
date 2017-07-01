def es_primo(n):
    if n == 0 or n == 1:
    	return False
    for i in range(2, n):
        if n%i == 0:
            return False
    return True

def factorial(n):
	factorial = 1
	for x in range(1, n + 1):
		factorial *= x 
	return factorial	

# "numeros" es una LISTA de numeros

def tomar_primos(numeros):
	primos = []
	for n in numeros:
		if es_primo(n):
			primos.append(n)
	return primos

def sumatoria_y_promedio(numeros):
	sumatoria = 0
	for n in numeros:
		sumatoria += n
	promedio = sumatoria / len(numeros)
	return sumatoria, promedio

def lista_factoriales(numeros):
	factoriales = []
	for n in numeros:
		factoriales.append(factorial(n))
	return factoriales

