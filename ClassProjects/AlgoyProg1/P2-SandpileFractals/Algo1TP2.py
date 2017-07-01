def auxiliar(lista, ancho, rv):
    """Función auxiliar que modifica la lista de valores del tablero usada en la función 'escribir_archivo'. 
	Modifica la lista de valores de tal forma que se respete la resolución vertical especificada por el usuario. Recibe la lista de valores (cada uno representando una posición),
        el ancho del tablero y la resolución vertical, y modifica la lista de manera acorde."""
    nueva_lista = []
    aux = []
    cont = 0
    for elemento in lista:
        cont += 1
        aux.append(elemento)
        if cont == ancho:
            nueva_lista += aux * rv
            aux = []
            cont = 0              
    return nueva_lista

def construir_tablero(ancho, alto):
    """Recibe el ancho y el alto especificados por el usuario, y genera un tablero vacío (sólo con valores 0),
	que luego podrá ser modificado por el usuario. El tablero consiste de un diccionario cuyas claves son posiciones (x,y), y sus valores son 
	los asociados al sandpile en cada posición."""
    tablero = {}
    for x in range(alto):
        for y in range(ancho):
            tablero[(x,y)] = 0
    return tablero

def modificar_tablero(tablero, coord_x, coord_y, valor):
    """Recibe un tablero, dos coordenadas y un valor, y modifica la posición del tablero en esas coordenadas
	reemplazando el valor original por el especificado por el usuario."""
    tablero[(coord_x, coord_y)] = valor
    return tablero

def estabilizar_tablero(tablero):
    """Recibe un tablero de sandpiles, e itera sobre el mismo siguiendo las reglas de los sandpiles hasta que
	el tablero se considere estable, es decir, que no tenga ningún valor por encima de 3."""
    while True:
        auxiliar = []
        estable = True
        for clave, valor in tablero.items():
            if valor >= 4:
                estable = False
                auxiliar.append(clave)
                tablero[clave] = valor % 4
                vecino = valor // 4
        if estable: break
        for coord in auxiliar:
            if (coord[0] - 1, coord[1]) in tablero:
                tablero[(coord[0] - 1, coord[1])] += vecino
            if (coord[0] + 1, coord[1]) in tablero:
                tablero[(coord[0] + 1, coord[1])] += vecino
            if (coord[0], coord[1] - 1) in tablero:
                tablero[(coord[0], coord[1] - 1)] += vecino
            if (coord[0], coord[1] + 1) in tablero:
                tablero[(coord[0], coord[1] + 1)] += vecino
    return tablero

def escribir_archivo(nombre_archivo, tablero, ancho, res_hor, alto, res_ver, colores_asignados):
    """Recibe la ruta y el nombre especificados por el usuario, un tablero junto con sus datos (ancho, alto, y resolución horizontal/vertical), la resolución de cada casillero del tablero
	especificada por el usuario y un diccionario con los colores asignados a cada valor entre 0 y 3, y escribe un archivo de tipo .ppm con la
	representación gráfica del tablero generado por el usuario."""
    claves_ordenadas = []
    for clave in tablero:
        claves_ordenadas.append(clave)
    claves_ordenadas.sort()
    archivo = open(nombre_archivo + ".ppm", "w")
    archivo.write("P3\n")
    archivo.write(str(ancho * res_hor) + " " + str(alto * res_ver) + "\n")
    archivo.write("255\n")
    for clave in auxiliar(claves_ordenadas, ancho, res_ver):
        valor = tablero[clave]
        for x in range(res_hor):
            archivo.write(colores_asignados[valor] + "\n")
    archivo.close()

def espejar_horizontalmente(nombre_archivo, ancho, res_hor, alto, res_ver, nh):
    """Recibe la localización de un archivo .ppm así como los datos del tablero que representa (ancho, alto, numero de reflexiones y resolución horizontal y vertical), y modifica el archivo
	de tal modo que se espeje horizontalmente el gráfico que representa tantas veces como indique el usuario."""
    lineas = []
    auxiliar = []
    archivo = open(nombre_archivo + ".ppm", "r")
    for linea in archivo: lineas.append(linea)
    archivo.close()
    archivo = open(nombre_archivo + ".ppm", "w")
    archivo.write("P3\n")
    archivo.write(str(ancho * res_hor * nh) + " " + str(alto * res_ver) + "\n") #2 es n (generalizar)
    archivo.write("255\n")
    for linea in lineas[3:]:  #Acá hay que modificar para agregar la posibilidad de elegir el numero de espejaciones
        archivo.write(linea)
        auxiliar.append(linea)
        if len(auxiliar) == ancho * res_hor:
            for x in range(nh - 1):
                if x%2 == 0:
                    for l in auxiliar[::-1]: archivo.write(l)
                else:
                    for l in auxiliar: archivo.write(l)
            auxiliar = []       
    archivo.close()

def espejar_verticalmente(nombre_archivo, ancho, res_hor, alto, res_ver, nh, nv):
    """Recibe la localización de un archivo .ppm así como los datos del tablero que representa (ancho, alto, reflexiones verticales a hacer, y resolución horizontal/vertical), además de
        la cantidad de reflexiones horizontales previamente hechas que deban ser tenidas en cuenta, y lo modifica
	espejando verticalmente el gráfico que representa tantas veces como se haya indicado."""
    lineas = []
    auxiliar = []
    archivo = open(nombre_archivo + ".ppm", "r")
    for linea in archivo: lineas.append(linea)
    archivo.close()
    archivo = open(nombre_archivo + ".ppm", "w")
    archivo.write(lineas[0])
    archivo.write(str(ancho * res_hor * nh) + " " + str(alto * res_ver * nv) + "\n") 
    archivo.write("255\n")
    for x in range(nv):
        if x%2 == 0:
            for linea in lineas[3:]:
                archivo.write(linea)
        else:
            for linea in lineas[:2:-1]:
                auxiliar.append(linea)
                if len(auxiliar) == ancho * res_hor * nh: 
                    for l in auxiliar[::-1]: archivo.write(l)
                    auxiliar = []
    archivo.close()
    
def main():
    """Función principal del programa. Pide al usuario todos los datos necesarios par la construcción del archivo .ppm, a saber:
	-Tamaño y resolución del tablero
	-Valores contenidos en el tablero
	-Reflexión vertical u horizontal
	-Configuración de colores
	-Ruta donde se guardará el archivo
	y genera un archivo .ppm con la representación pedida por el usuario."""
    tamanio_celda_horizontal = 1
    tamanio_celda_vertical = 1
    colores = {"negro" : "0 0 0", "blanco" : "255 255 255", "rojo" : "255 0 0", "verde" : "0 255 0", "azul" : "0 0 255", "amarillo" : "255 255 0", "cian" : "0 255 255", "magenta" : "255 0 255"}
    asignacion_colores = {0 : "255 0 255", 1 : "0 255 0", 2 : "0 0 255", 3 : "255 255 0"}
    numero_reflejos_h = 0
    numero_refjelos_v = 0

    while True: #Acá el usuario ingresa el tamaño del tablero.
        try:
            i = int(input("Ingrese el ancho del fractal: "))
            j = int(input("Ingrese el alto del fractal: "))
        except ValueError:
            print("Debe ingresar numeros enteros, intente nuevamente.")
            continue
        if i <= 0 or j <= 0:
            print("Debe ingresar como mínimo 1x1, intente nuevamente.")
            continue
        tablero = construir_tablero(i, j)
        break
    
    centinela = "si" #Acá el usuario ingresa los casilleros que desea modificar.
    while centinela.lower() != "no":
        while True:
            try:
                x = int(input("Ingrese el numero de fila que desea modificar: "))
                y = int(input("Ingrese el numero de columna que desea modificar: "))
            except ValueError:
                print("Debe ingresar numeros enteros, intente nuevamente.")
                continue
            if not (x > 0 and x < j) or not (y > 0 and y < i):
                print("Debe ingresar un par ordenado dentro del tablero que definió ({} x {}). Intente nuevamente: ".format(i, j))
                continue
            valor = int(input("Ingrese el valor que tendra la coordenada ({}, {}): ".format(x, y)))
            tablero = modificar_tablero(tablero, x, y, valor)
            break
        centinela = input("¿Desea continuar agregando sandpiles? <si - no>: ")
        while centinela.lower() not in ["si", "no"]:
            centinela = input("No se entiende ese comando. Desea continuar agregando sandpiles? <si-no>: ")       
            
        
    tablero_estabilizado = estabilizar_tablero(tablero) #Se estabiliza el tablero.
    
    nombre = input("Ingrese el nombre del archivo: ")
    
    modificar_colores = input("Desea modificar la asignacion de colores? (Por defecto: 0 -> magenta, 1 -> verde, 2 -> azul, 3 -> amarillo) <si-no>: ") #Acá el usuario decide si quiere usar los colores por defecto o asignar colores nuevos a cada valor.
    while modificar_colores.lower() not in ["si", "no"]:
        modificar_colores = input("No se entiende ese comando. Desea modificar la asignacion de colores? (Por defecto: 0 -> magenta, 1 -> verde, 2 -> azul, 3 -> amarillo) <si-no>: ")
    if modificar_colores.lower() == "si":
        seguir = "si"
        while seguir.lower() == "si":
            numero = input("Qué valor quiere reasignar? <0, 1, 2, 3>: ")
            while numero not in ["0", "1", "2", "3"]:
                numero = input("Debe elegir un numero entre 0 y 3 inclusive. Intente de nuevo: ")
            color = input("Qué color desea asignarle? <negro, blanco, rojo, verde, azul, amarillo, cian, magenta>: ")
            while color.lower() not in ["negro", "blanco", "rojo", "verde", "azul", "amarillo", "cian", "magenta"]:
                color = input("Debe elegir uno de los siguientes colores; <negro, blanco, rojo, verde, azul, amarillo, cian, magenta>. Intente nuevamente: ")
            asignacion_colores[int(numero)] = colores[color.lower()]
            seguir = input("Desea seguir modificando las asignaciones? <si-no>: ")
            while seguir.lower() not in ["si", "no"]:
                seguir = input("No se entiende ese comando. Desea seguir modificando las asignaciones? <si-no>: ")          
            
    modificar_celdas = input("Desea modificar el tamaño en pixeles de cada celda? (Por defecto: 1x1) <si-no>: ") #Acá el usuario modifica la resolucion de cada celda.
    while modificar_celdas.lower() not in ["si", "no"]:
        modificar_celdas = input("No se entiende ese comando. Desea modificar el tamaño en pixeles de cada celda? (Por defecto: 1x1) <si-no>: ")       
    if modificar_celdas.lower() == "si":
        while True:
            try:
                tamanio_celda_horizontal = int(input("Ingrese cuantos pixeles ocupa horizontalmente cada celda: "))
                tamanio_celda_vertical = int(input("Ingrese cuantos pixeles ocupa verticalmente cada celda: "))
            except ValueError:
                print("Debe ingresar numeros enteros. Intente nuevamente.")
                continue
            break
    
    escribir_archivo(nombre, tablero_estabilizado, i, tamanio_celda_horizontal, j, tamanio_celda_vertical, asignacion_colores) #Se escribe el archivo, sin espejar.
    
    pregunta_espejar1 = input("Desea espejar el fractal horizontalmente? <si-no>: ") #Acá se modifica el archivo espejándolo, según el usuario decida.
    while pregunta_espejar1.lower() not in ["si", "no"]:
        pregunta_espejar1 = input("No se entiende ese comando. Desea espejar el fractal horizontalmente? <si-no>: ")
    if pregunta_espejar1.lower() == "si":
        while True:
            try:
                numero_reflejos_h = int(input("Cuantas veces desea espejar la imagen horizontalmente?: "))
            except ValueError:
                numero_reflejos_h = int(input("Debe ingresar un numero entero. Intente de nuevo: "))
                continue
            break       
        espejar_horizontalmente(nombre, i, tamanio_celda_horizontal, j, tamanio_celda_vertical, numero_reflejos_h + 1) #tiene que decidir el usuario
    pregunta_espejar2 = input("Desea espejar el fractal verticalmente? <si-no>: ")
    while pregunta_espejar2.lower() not in ["si", "no"]:
        pregunta_espejar2 = input("No se entiende ese comando. Desea espejar el fractal verticalmente? <si-no>: ")
    if pregunta_espejar2 == "si":
        while True:
            try:
                numero_reflejos_v = int(input("Cuantas veces desea espejar la imagen verticalmente?: "))
            except ValueError:
                numero_reflejos_v = int(input("Debe ingresar un numero entero. Intente de nuevo: "))
                continue
            break       
        espejar_verticalmente(nombre, i, tamanio_celda_horizontal, j, tamanio_celda_vertical, numero_reflejos_h + 1, numero_reflejos_v + 1) #tiene que decidir el usuario

    print("La imagen se generó en la misma carpeta donde está ubicado el programa.")
    
    
main()