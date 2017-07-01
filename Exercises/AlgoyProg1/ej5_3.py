from time import sleep

def pedir_contrasenia():
	intentos = 0
	sleep_time = 0
	INTENTOS_MAXIMOS = 3
	CONTRASENIA_VALIDA = 'huracangrandesenacenosehace'
	contrasenia_ingresada = input('Ingrese la contraseña: ')
	while contrasenia_ingresada != CONTRASENIA_VALIDA:
		intentos += 1
		sleep_time += 2
		if intentos == INTENTOS_MAXIMOS:
			print('Se alcanzó el número máximo de intentos.')
			return False
		contrasenia_ingresada = input('Contraseña inválida, ingrese la contraseña: ')
		sleep(sleep_time)
	return True

if pedir_contrasenia():
	print("Bienvenido")
