def es_potencia_de_dos(n):
    if n == 1 or n == 2:
        return True
    if n<=0:
        return False
    if n%2!=0:
        return False
    num = 2
    while num < n:
        pot = 2 ** num
        if n == pot:
            return True
        num += 1
    return False

def suma_potencias_dos(a, b):
    suma = 0
    for x in range(a, b+1):
        if es_potencia_de_dos(x):
            suma += x
    return suma
