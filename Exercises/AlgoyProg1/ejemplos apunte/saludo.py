print('Se le preguntarán los nombres de sus amigos para saludarlos.')

n = int(input("A cuántos amigos quiere saludar?: "))

def saludo():
	print('Hola', nombre + "!")
		
for x in range(1,n+1):
	nombre = input("Escriba el nombre del " + str(x) + "° amigo: ")
	saludo()
	
print('Es todo por ahora.')

