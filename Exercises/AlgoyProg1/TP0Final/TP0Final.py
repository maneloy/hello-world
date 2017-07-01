def norma(x, y):
    '''Recibe el par ordenado (x, y) que representa el vector al orígen y devuelve la norma del vector en cuestión.'''
    norma = (x ** 2 + y ** 2) ** (1/2)
    return norma

def resta(x1, y1, x2, y2):
    '''Recibe dos pares ordenados (x1, y1) y (x2, y2) y devuelve la resta de los dos puntos, dando como resultado una transposición del vector que los une con orígen en (0,0).'''
    x_resta = x1 - x2
    y_resta = y1 - y2
    return x_resta, y_resta

def distancia(x1, y1, x2, y2):
    '''Recibe dos pares ordenados (x1, y1) y (x2, y2) representando dos puntos en el espacio y devuelve la distancia que los separa.'''
    xd, yd = resta(x1, y1, x2, y2)
    return norma(xd, yd)

def normalizado(x,y):
    '''Recibe un par ordenado (x, y) representando un vector al orígen, y lo normaliza, es decir, devuelve un vector de igual dirección y sentido, pero unitario.'''
    xn = x / norma(x,y)
    yn = y / norma(x,y)
    return xn, yn

def vec_dir_norm(x1, y1, x2, y2):
    '''Recibe dos pares ordenados (x1, y1) y (x2, y2) representando dos puntos en el plano, y devuelve un vector dirección unitario en relación a la recta que los une de izquierda a derecha.'''
    r1, r2 = resta(x1, y1, x2, y2)
    return normalizado(r1, r2)

def proyectar(x, y, dx, dy, cx, cy):
    '''Recibe un punto (x,y), una dirección (dx,dy), y un punto que pasa por la recta cuya dirección unitaria es (dx,dy), es decir (cx, cy). Devuelve la proyección del punto ingresado en la recta definida.'''

    a1 = x - cx
    a2 = y - cy

    p11 = dx ** 2
    p12 = dx * dy
    p21 = p12
    p22 = dy ** 2

    rx = p11 * a1 + p12 * a2
    ry = p21 * a1 + p22 * a2

    f1 = rx + cx
    f2 = ry + cy

    return f1, f2

def area_triangulo(base, altura):
    '''Recibe la base y la altura de un triángulo y devuelve el area del triángulo en cuestión.'''
    area = (base * altura) / 2
    return area

def tri_tres_pts(x1, y1, x2, y2, x3, y3):
    '''Recibe tres puntos (x1, y1), (x2, y2) y (x3, y3) y devuelve el area del triángulo que forman.'''
	
    d1 = distancia(x1, y1, x2, y2)
    d2 = distancia(x1, y1, x3, y3)
    d3 = distancia(x2, y2, x3, y3)
	
    base = max(d1, d2, d3)
	
    dir1x, dir1y = vec_dir_norm(x1, y1, x2, y2)
    dir2x, dir2y = vec_dir_norm(x1, y1, x3, y3)
    dir3x, dir3y = vec_dir_norm(x2, y2, x3, y3)
	
    proy1x, proy1y = proyectar(x1, y1, dir3x, dir3y, x2, y2)
    proy2x, proy2y = proyectar(x2, y2, dir2x, dir2y, x1, y1)
    proy3x, proy3y = proyectar(x3, y3, dir1x, dir1y, x2, y2)
    
    dist1 = distancia(x1, y1, proy1x, proy1y)
    dist2 = distancia(x2, y2, proy2x, proy2y)
    dist3 = distancia(x3, y3, proy3x, proy3y)
	
    altura = min(dist1, dist2, dist3)
	
    return area_triangulo(base, altura)