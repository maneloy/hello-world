def maximo(lista):
    maxi = lista[0]
    i = -1
    for elem in lista:
        i += 1
        if elem > maxi: maxi = elem
    return (maxi, i)

