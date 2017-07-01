def es_primo(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, n):
        if n%i == 0:
            return False
    return True

def imprimir_primos(n):
	'''Recibe un numero natural e imprime todos los primos que hay hasta ese numero.'''
	if n == 0 or n == 1 or n == 2:
		print('No hay numeros primos antes del {}'.format(n))
		return None 
	contador = 2
	while contador < n:
		if es_primo(contador):
			print(contador)
		contador += 1
		

