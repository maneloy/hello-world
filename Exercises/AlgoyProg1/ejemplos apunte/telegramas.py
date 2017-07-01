def procesar_telegrama(cadena, long_max):
	"""Genera un telegrama a partir de una cadena, acortando todas las palabras que sean mayores que el límite establecido e indicando con un @ las palabras que fueron acortadas"""
    palabras = cadena.split()
    for i in range(len(palabras)):
        if len(palabras[i]) > long_max:
            if "." in palabras[i]:
                palabras[i] = palabras[i][:long_max] + "@."
            else:
                palabras[i] = palabras[i][:long_max] + "@"
    for i in range(len(palabras) - 1):
        if "." in palabras[i]:
            palabras[i] = palabras[i][:len(palabras[i]) - 1] + " STOP"
    if "." in palabras[len(palabras) - 1]:
        palabras[len(palabras) - 1] = palabras[len(palabras) - 1][:len(palabras[len(palabras) - 1]) - 1] + " STOPSTOP"
    else:
        palabras[len(palabras) - 1] = palabras[len(palabras) - 1][:len(palabras[len(palabras) - 1])] + " STOPSTOP"

    return " ".join(palabras)
