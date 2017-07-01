def norma(x, y):
    return (x**2 + y**2) ** (1/2)

def distancia_o():
    n = int(input("Cuántos puntos va a ingresar?: "))

    x, y = eval(input("Ingrese un punto (x,y): "))
    for i in range(n-1):
        xa, ya = eval(input("Ingrese otro punto (x,y): "))
        if norma(xa,ya) > norma(x,y):
            x, y = xa, ya
    else:
        print(x,y)
    
 
                         
