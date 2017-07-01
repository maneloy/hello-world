def plegar_texto(texto, longitud):
    texto_plegado = []
    cadena = ""
    i = -1
    j = None
    limite = -1
    contador = 0
    for c in texto:
        limite += 1
        i += 1
        if c == " ":
            j = i
        cadena += c
        if limite == longitud and texto[i+1] != " ":
            texto_plegado.append(texto[contador : j + 1]) # Ó podría concatenar la cadena acá con [contador : j+1], creo.
            cadena = texto[j+1 : i + 1]
            limite = 0
            contador = i - len(cadena) + 1
        if limite == longitud and texto[i+1] == " ":
            texto_plegado.append(texto[contador : i + 1])
            cadena = ""
            limite = 0 
            contador = i - len(cadena) + 1
    texto_plegado.append(texto[contador:])
    return texto_plegado


for elem in plegar_texto("Als Gregor Samsa eines Morgens aus unruhigen Träumen erwachte, fand er sich in seinem Bett zu einem ungeheueren Ungeziefer verwandelt.", 20):
	print(elem)
