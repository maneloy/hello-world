import soundPlayer as pysounds

class _Nodo:
    """Clase nodo. Contiene un dato, y la referencia al próximo nodo."""

    def __init__(self, dato = None, prox = None):
        """Crea un nodo."""

        self.dato = dato
        self.prox = prox

    def __str__(self):
        """Devuelve la representación en cadena del nodo."""

        return str(self.dato)

class _IteradorListaEnlazada: #Modificado para ir en ambas direcciones. ES POSIBLE QUE HAYA QUE MODIFICARLO PARA QUE DEVUELVA EL NODO
    
    def __init__(self, prim):
        self.actual = prim
        self.anteriores = Pila()              
        self.aux = False
        self.aux2 = False
        
    def __next__(self):
        if self.aux2:
            self.anteriores.apilar(self.actual)
            self.actual = self.actual.prox
            self.aux2 = False
        if self.actual is None:
            raise StopIteration()
        self.aux = True
        dato = self.actual.dato
        self.anteriores.apilar(self.actual)
        self.actual = self.actual.prox
        return dato

    def ant(self):
        if self.aux:
            self.anteriores.desapilar()
            self.aux = False
        if self.anteriores.esta_vacia():
            raise StopIteration()
        self.aux2 = True
        self.actual = self.anteriores.desapilar()
        dato = self.actual.dato
        return dato
    
class ListaEnlazada:
    """Modela una lista enlazada."""
    
    def __init__(self):
        """Crea una lista enlazada vacia."""

        #Referencia al primer nodo (None si la lista está vacia)
        self.prim = None
        self.ult = None
        #Cantidad de elementos de la lista
        self.len = 0
        #Referencia para el método 'next'
        self.actual = "No_inicializado"

    def __str__(self):
        """Devuelve una representación en forma de cadena de la lista enlazada."""

        s = ""
        while True:
            try:
                dato = self.next()
                cad = str(dato)
                s += cad + ", "
            except StopIteration:
                break
        return s

    def __len__(self):
        """Devuelve la longitud (cantidad de nodos) de la lista enlazada"""

        return self.len

    def __iter__(self):
        """Devuelve un iterador de la lista."""

        return _IteradorListaEnlazada(self.prim)

    def pop(self, i = None):
        """Elimina el nodo de la posición i, y devuelve el dato contenido.
            Si i está fuera de rango, se levanta la excepción IndexError.
            Si no se recibe la posición, devuelve el último elemento."""

        if i is None:
            i = self.len - 1

        if i < 0 or i >= self.len:
            raise IndexError("Índice fuera de rango")

        if i == 0:
            #Caso particular: saltear la cabecera de la lista
            dato = self.prim.dato
            self.prim = self.prim.prox

        else:
            #Buscar los nodos en las posiciones (i-1) e (i)
            n_ant = self.prim
            n_act = n_ant.prox
            for pos in range(1, i):
                n_ant = n_act
                n_act = n_ant.prox

            # Guardar el dato y descartar el nodo

            dato = n_act.dato
            n_ant.prox = n_act.prox

            if i == self.len - 1: #Se redefine el último elemento.
                self.ult = n_ant

        self.len -= 1

        if self.len == 0:
            self.ult = None

        return dato

    def remove(self, x):
        """Borra la primera aparición del valor x en la lista.
            Si x no está en la lista, levanta ValueError."""

        if self.len == 0:
            raise ValueError("Lista vacía")

        if self.prim.dato == x:
            #Caso particular: saltear la cabecera de la lista.
            self.prim = self.prim.prox
            
        else:
            #Buscar el nodo anterior al que contiene a x (n_ant)
            n_ant = self.prim
            n_act = n_ant.prox
            while n_act is not None and n_act.dato != x:
                n_ant = n_act
                n_act = n_ant.prox
            if n_act == None:
                raise ValueError("El valor no está en la lista.")
            #Descartar el nodo  	
            n_ant.prox = n_act.prox

            if n_ant.prox == None: #Se redefine el último elemento.
                self.ult = n_ant

        self.len -= 1

        if self.len == 0:
            self.ult = None

    def insert(self, i, x):
        """Inserta el elemento x en la posición i.
            Si la posición es inválida, levanta IndexError."""

        if i < 0 or i > self.len:
            raise IndexError("Posición inválida")

        nuevo = _Nodo(x)

        if i == 0:
            #Caso particular: insertar al principio
            nuevo.prox = self.prim
            self.prim = nuevo

        else:
            #Buscar el nodo anterior a la posición deseada
            n_ant = self.prim
            for pos in range(1, i):
                n_ant = n_ant.prox

            #Intercalar el nuevo nodo

            if n_ant.prox == None: #Se redefine el último elemento.
            	self.ult = nuevo

            nuevo.prox = n_ant.prox
            n_ant.prox = nuevo

        self.len += 1
        if self.len == 1:
            self.ult = self.prim

    def append(self, x): #Hecha por mí
        """Agrega un elemento nuevo al final de la lista."""

        nuevo = _Nodo(x)
        if self.len == 0:
            self.prim = nuevo
            self.ult = nuevo
        else:
            self.ult.prox = nuevo
            self.ult = nuevo

        self.len += 1

    def index(self, x): #Hecha por mí
        """Devuelve el índice del elemento especificado por el usuario. 
            Si el elemento no está en la lista, levanta IndexError."""

        i = 0
        
        if self.len == 0:
            raise ValueError("Lista vacía")

        if self.prim.dato == x:
            #Caso particular: saltear la cabecera de la lista.
            return i

        else:
            #Buscar el nodo que contiene a x
            n_act = self.prim
            while n_act.prox is not None and n_act.dato != x:
                i += 1
                n_act = n_act.prox
            if n_act.dato == x:
                return i
            else:
                raise ValueError("El valor no está en la lista.")
        
    def next(self):
        """Devuelve los datos de cada nodo, uno por uno, hasta llegar al final de la lista, en cuyo caso lanza una excepción StopIteration."""

        if self.actual == "No_inicializado":
            self.actual = self.prim   
        if self.actual == None:  # IMPORTANTE: Vuelve al principio al iterar el último elemento. No sé si esté bien, el ejercicio no lo pedía.
            self.actual = self.prim
            raise StopIteration()
        dato = self.actual.dato
        self.actual = self.actual.prox
        return dato

    def extend(self, otra):
        """Recibe otra lista enlazada, y agrega sus elementos a la lista actual."""
        
        if self.len == 0: return otra
        self.ult.prox = otra.prim
        self.len += otra.len
        self.ult = otra.ult

    def invertir(self):
        """Invierte el sentido de los nodos de la lista."""
        n_ant = self.prim
        n_act = n_ant.prox
        for pos in range(1, self.len):
            aux = n_act.prox 
            n_act.prox = n_ant
            n_ant = n_act
            n_act = aux
        self.prim, self.ult = self.ult, self.prim
        self.ult.prox = None

class Pila:
    """Representa una pila con operaciones de apilar, desapilar, y verificar si está vacía."""
    def __init__(self):
        """Crea una pila vacía."""
        self.items = []

    def __str__(self):
        s = ""
        for item in self.items:
            s += str(item) + ", "
        return s

    def apilar(self, x):
        """Apila el elemento x."""
        self.items.append(x)

    def desapilar(self):
        """Desapila el elemento x y lo devuelve.
           Si la pila está vacía, levanta una excepción."""
        if self.esta_vacia():
            raise ValueError("La pila está vacía") 
        return self.items.pop()

    def esta_vacia(self):
        """Devuelve True si la pila está vacía, False si no."""
        return len(self.items) == 0

class Track:
    
    def __init__(self, funcion, frecuencia, volumen, duty_cycle = 0):
        self.funcion = funcion
        self.frecuencia = frecuencia
        self.volumen = volumen
        self.duty_cycle = duty_cycle

class Mark:
    
    def __init__(self,duracion):
        self.duracion=duracion
        self.notas=[]

    def habilitar_track(self, num_track):
        self.notas[num_track - 1] = True # "-1" para relacionar el numero de track con el indice en la lista.

    def desabilitar_track(self, num_track):
        self.notas[num_track - 1] = False # "-1" para relacionar el numero de track con el indice en la lista.

class Cancion:
    
    def __init__(self):
        self.canales = None
        self.marcas = ListaEnlazada()
        self.tracks = []
        self.iterador = iter(self.marcas)

    def agregar_track(self, funcion, frecuencia, volumen, duty_cycle = 0):
        self.tracks.append(Track(funcion, frecuencia, volumen, duty_cycle))

    def borrar_track(self, num_track):
        self.tracks.remove(self.tracks[num_track - 1]) # "-1" para relacionar el numero de track con el indice en la lista.

    def agregar_marca(self, actual, duracion):
        marca = Mark(duracion)
        marca.notas = []
        for x in len(self.tracks):
            marca.notas.append(False)
        self.marcas.insert(actual, marca) #Actual vendría a ser el índice del nodo en el que está el cursor.

def plp_a_cancion(nombre):
    cancion = Cancion()
    archivo = open(nombre)
    linea = archivo.readline()
    cancion.canales = int(linea.split(",")[1])
    linea = archivo.readline()
    while linea:
        tipo = linea.split(",")
        while tipo[0] == "S":
            onda = tipo[1]
            caracteristicas = onda.split("|")
            func = caracteristicas[0]
            t_func = ""
            duty_cycle = "0"
            frecuencia = caracteristicas[1]
            volumen = caracteristicas [2]
            for char in func:
                if char.isdigit():
                    duty_cycle += char
                else:
                    t_func += char
            cancion.tracks.append(Track(t_func, float(frecuencia), float(volumen), float(duty_cycle)/100))
            linea = archivo.readline()
            tipo = linea.split(",")

        if tipo[0] == "T":
            duracion = float(tipo[1])
            linea = archivo.readline()
            tipo = linea.split(",")
        if tipo[0] == "N":
            habilitados = tipo[1]
            marca = Mark(duracion)
            for char in habilitados:
                if char == ".":                    #NO SIRVE EL PUNTO MEDIO
                    marca.notas.append(False)
                if char == "#":
                    marca.notas.append(True)
            cancion.marcas.append(marca)
        linea = archivo.readline()
    archivo.close()
    return cancion

def reproducir_cancion(cancion):
    tracks = []
    canales = cancion.canales
    sp = pysounds.SoundPlayer(canales)
    for elemento in cancion.tracks:
        funcion = elemento.funcion
        frecuencia = elemento.frecuencia
        volumen = elemento.volumen
        duty_cycle = elemento.duty_cycle
        if funcion == "SIN":
            tracks.append(pysounds.SoundFactory.get_sine_sound(frecuencia, volumen))
        if funcion == "TRIA":
            tracks.append(pysounds.SoundFactory.get_triangular_sound(frecuencia, volumen))
        if funcion == "SQ":
            tracks.append(pysounds.SoundFactory.get_square_sound(frecuencia, volumen, duty_cycle))
    iterador = iter(cancion.marcas)
    while True:
        try:
            marca = iterador.__next__()
            duracion = marca.duracion
            notas = marca.notas
            habilitados = []
            for i in range(len(notas)):
                if notas[i]:
                    habilitados.append(tracks[i])
            sp.play_sounds(habilitados, duracion)
        except StopIteration:
            break
    sp.close()


song = plp_a_cancion("musica_ejemplo_modificado.plp")
reproducir_cancion(song)