def raices(a, b, c):
    '''https://es.wikipedia.org/wiki/Ecuaci%C3%B3n_de_segundo_grado#Discriminante'''
    if a == 0:
        print("a no puede ser cero, la ecuación debe ser cuadrática.")
        return
    discriminante = b**2 - 4*a*c
    if discriminante > 0:
        raiz_r1 = (-b + discriminante ** (1/2)) / (2*a)
        raiz_r2 = (-b - discriminante ** (1/2)) / (2*a)
        print("Las raices reales son", raiz_r1, "y", raiz_r2)
    elif discriminante == 0:
        raiz_r1 = (-b + discriminante ** (1/2)) / (2*a)
        print("La raíz única de doble multiplicidad es", raiz_r1)
    else:
        x_raiz = -b/(2*a)
        y_raiz = ((-discriminante)**(1/2))/(2*a)
        y_raiz_conj = -y_raiz
        print("Las raices imaginarias conjugadas son ({},{}) y ({},{})".format(x_raiz, y_raiz, x_raiz, y_raiz_conj))
	
	