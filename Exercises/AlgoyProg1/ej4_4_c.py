def interseccion(p1, a, p2, b):
    '''Recibe dos rectas descriptas por su pendiente y ordenada de orígen (p1, a) y (p2, b), y devuelve, si existe, la intersección entre ambas.'''
    if p1 == p2 and a != b:
        print("No existe la intersección.")
        return
    elif p1 == p2 and a == b:
        print("Ambas rectas son la misma (intersección = recta1 = recta2).")
        return
    else:
        x_int = (b - a) / (p1 - p2)
        y_int = (a - b*p1/p2) / (1 - p1/p2)
        return x_int, y_int

    