def positivo():
    s = input("Ingrese un número: ")
    if not s:
        print("Es cadena vacía.")
        return
    n = int(s)
    if n > 0:
        print("Número positivo")
    elif n == 0:
        print("Igual a 0")
    else:
        print("Número no positivo")
