def binario_a_decimal(numero):
    decimal = 0
    for i in range(len(numero)):
        if int(numero[i]) == 1:
            decimal += 2 ** (len(numero) - (i+1))
    return decimal
