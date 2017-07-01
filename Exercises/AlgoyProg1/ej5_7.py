def suma_divisores(n):
    if n == 0:
        print('No se puede.')
        return None
    suma = 0
    for x in range(1, n): #No incluyo n para poder encontrar perfectos
        if n%x == 0:
            suma+=x
    return suma

def primeros_num_perfectos(m):
    cota = 0
    n = 1
    while cota < m:
        if suma_divisores(n) == n:
            cota += 1
            print(n)
            n += 1
        else:
            n += 1
			
#Acá empieza el punto c

def buscar(a):
    b = a + 1
    while suma_divisores(b) != a and suma_divisores(a) > b:
        b += 1
    return b

def primeros_num_amigos(m):
    a = 0
    for c in range(m):
        a += 1
        while True:
            b = buscar(a)
            if suma_divisores(a) == b and suma_divisores(b) == a:
                print(a,b)
                break
            a += 1
            

                
    
    


                    

            
                    
                    