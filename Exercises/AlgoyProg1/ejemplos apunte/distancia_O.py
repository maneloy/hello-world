def norma(x, y):
    return (x**2 + y**2) ** (1/2)

def distancia_o(x1, y1, x2, y2, x3, y3):
    
    n1 = norma(x1, y1)
    n2 = norma(x2, y2)
    n3 = norma(x3, y3)

    if max(n1,n2,n3) == n1:
        print('El más lejano al orígen es: ', x1, y1)
    if max(n1,n2,n3) == n2 and not (x1 == x2 and y1 == y2) :
        print('El más lejano al orígen es: ', x2, y2)
    if max(n1,n2,n3) == n3 and not ((x1 == x2 and y1 == y2) or (x1 == x3 and y1 == y3) or (x2 == x3 and y2 == y3)):
        print('El más lejano al orígen es: ', x3, y3)
 
                         
