def rot13(arch1, arch2):
	"""Recibe un archivo de texto y lo encripta
		sumándole 13 a cada caracter, y escribe 
		la  encriptación en el segundo archivo"""

	archivo1 = open(arch1)
	archivo2 = open(arch2, "w")
	for linea in archivo1:
		for caracter in linea:
			if caracter == " " or caracter == "\n":
				archivo2.write(caracter)
			else:
				nuevo = ord(caracter.lower()) + 13
				if nuevo > 122: nuevo -= 26
				archivo2.write(chr(nuevo))
	archivo1.close()
	archivo2.close()

rot13("c:\\users\\usuario\desktop\martin_fierro.txt", "c:\\users\\usuario\desktop\martin_fierro_encriptado.txt")