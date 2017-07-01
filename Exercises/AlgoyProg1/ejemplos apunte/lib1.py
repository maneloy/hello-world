from math import pi

v = 'aguante macri'

def area_circulo():
	''' Calcula e imprime el area de un círculo tras solicitar el radio al usuario'''
	radio = float(input('Escriba el radio de un círculo: '))
	area = pi * radio ** 2
	print('El area del círculo es', area)

