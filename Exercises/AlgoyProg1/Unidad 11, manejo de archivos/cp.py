from pickle import dump

def cp(file1, file2, mode):
	if mode == "binario": 
		archivo1 = open(file1, "rb")
		archivo2 = open(file2, "wb")
		for sequence in archivo1.read(2000000):
			dump(sequence, archivo2)
	else:
		archivo1 = open(file1, "r")
		archivo2 = open(file2, "w")
		for line in archivo1.read(2000000):
			archivo2.write(line)	
	archivo1.close()
	archivo2.close()

ruta1 = input("Ingrese la ruta del archivo que desea copiar: \n")
ruta2 = input("Ingrese la ruta donde desea copiar los datos: \n")
modo = input("Ingrese si desea copiar como archivo de texto o binario <texto-binario>: ")
print()
cp(ruta1, ruta2, modo)
