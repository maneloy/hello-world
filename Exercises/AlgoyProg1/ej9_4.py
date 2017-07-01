def maslarga(texto):
	d = {}
	palabras = texto.split()
	for c in texto:
		if c not in d: d[c] = ""
		for palabra in palabras:
			if c in palabra and len(palabra) > len(d[c]): d[c] = palabra
	return d

print(maslarga("hoy es domingo"))