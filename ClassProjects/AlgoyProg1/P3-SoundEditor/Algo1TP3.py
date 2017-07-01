MENSAJE_MODO_INCORRECTO="Lo lamento, este comando solo funciona si usted se encuentra en el modo edición"
import soundPlayer as pysounds
import copy

class _Nodo:
    """Clase nodo. Contiene un dato, y la referencia al próximo nodo."""

    def __init__(self, dato = None, prox = None):
        """Crea un nodo."""

        self.dato = dato
        self.prox = prox

    def __str__(self):
        """Devuelve la representación en cadena del nodo."""

        return str(self.dato)

class _IteradorListaEnlazada:
    """Iterador para la clase ListaEnlazada."""
    
    def __init__(self, prim):
        """Constructor del iterador."""
        self.actual = prim
        self.anteriores = Pila()
        
    def __next__(self):
        """Devuelve el estado actual del iterador, y avanza al siguiente."""
        if self.actual==None:
            raise StopIteration
        dato=self.actual.dato
        self.anteriores.apilar(self.actual)
        self.actual = self.actual.prox
        return dato

    def hay_next(self):
        """Devuelve True si hay un elemento próximo, False si no."""
        return bool(self.actual.prox)

    def hay_back(self):
        """Devuelve True si hay un elemento anterior, False si no."""
        return not self.anteriores.esta_vacia()

    def back(self):
        """Retrocede el estado actual."""
        self.actual=self.anteriores.desapilar()

    def regenerar_pila(self,primero):
        """Reinicia el iterador."""
        self.anteriores=Pila()
        while primero!=self.actual:
            self.anteriores.apilar(primero)
            primero=primero.prox

    def dato_actual(self):
        """Devuelve el dato actual en el que se encuentra el iterador."""
        return self.actual.dato

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
        """Devuelve la representación en string de la pila."""
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
    def ver_tope(self):
        return self.items[-1]

class Track:
    """Modela el track de una canción."""

    def __init__(self, funcion, frecuencia, volumen, duty_cycle=None):
        self.funcion = funcion
        self.frecuencia = frecuencia
        self.volumen = volumen
        self.duty_cycle = duty_cycle


class Mark:
    """Modela la marca de una canción en la que se encuentra el cursor."""

    def __init__(self,duracion):
        """Constructor de la clase Mark."""
        self.duracion=duracion
        self.notas=[]

    def habilitar_track(self, num_track):
        """Habilita el track especificado de tal modo que suene en la marca."""
        self.notas[num_track - 1] = True # "-1" para relacionar el numero de track con el indice en la lista.

    def deshabilitar_track(self, num_track):
        """Silencia el track especificado en la marca."""
        self.notas[num_track - 1] = False # "-1" para relacionar el numero de track con el indice en la lista.


    def play(self, tracks, sp):
        """Reproduce el track."""
        self.play_seconds(tracks,sp,self.duracion)

    def play_seconds(self, tracks, sp, segundos):
        '''Funcion que recibe una lista de tracks, una constante sp y una cantidad de segundos,
        y reproduce la cantidad de segundos los tracks que son True'''
        habilitados = []
        for i in range(len(self.notas)):
            if self.notas[i]:
                habilitados.append(tracks[i])
        sp.play_sounds(habilitados, segundos)

class Cancion:
    """Modela el objeto Canción."""
    
    def __init__(self):
        """Constructor de la clase Canción."""
        self.marcas = ListaEnlazada()
        self.tracks = []
        self.iterador = None

    def agregar_track(self, funcion, frecuencia, volumen):
        """Recibe la funcion, frecuencia y volumen y agrega un track a la canción."""
        track=Track(funcion,frecuencia,volumen)
        self.tracks.append(track)
        actual=self.marcas.prim
        while actual:
            actual.dato.notas.append(False)
            actual=actual.prox

    def borrar_track(self, num_track):
        """Elimina el track indicado de la canción."""
        self.tracks.pop(num_track - 1) # "-1" para relacionar el numero de track con el indice en la lista.
        actual=self.marcas.prim
        while actual:
            actual.dato.notas.pop(num_track-1)
            actual=actual.prox

    def agregar_marca(self, posicion, duracion):
        """Agrega una nueva marca a la canción, especificando la duración y la posición."""
        marca = Mark(duracion)
        for x in range(len(self.tracks)):
            marca.notas.append(False)
        self.marcas.insert(posicion, marca)
        if not self.iterador:
            self.iterador=_IteradorListaEnlazada(self.marcas.prim)
        else:
            if posicion<=self.dar_posicion(self.iterador.dato_actual()):
                self.iterador.regenerar_pila(self.marcas.prim)

    def dar_posicion(self,marca):
        """Recibe una marca e indica en qué posición está."""
        actual=self.marcas.prim       
        posicion=0
        while actual:
            if marca==actual.dato:
                return posicion
            actual=actual.prox
            posicion+=1
        return -1

    def get_tracks(self):
        '''Función devuelve la lista de tracks de la canción actual'''
        tracks = []
        for elemento in self.tracks:
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
        return tracks

    def play(self):
        """Reproduce la canción entera."""
        sp = pysounds.SoundPlayer(len(self.tracks))
        tracks=self.get_tracks()
        iterador = iter(self.marcas)
        while True:
            try:
                marca = iterador.__next__()
                marca.play(tracks,sp)
            except StopIteration:
                break
        sp.close()

    def play_seconds(self, segundos):
        """Reproduce la cantidad de tiempo en segundos indicada a partir de la posición actual del iterador."""
        sp = pysounds.SoundPlayer(len(self.tracks))
        tracks=self.get_tracks()
        iterador = copy.deepcopy(self.iterador)
  
        while segundos > 0:
            try:
                marca = iterador.__next__()
                marca.play_seconds(tracks,sp,min([segundos, marca.duracion]))
                segundos=segundos-marca.duracion            
            except StopIteration:
                break
        sp.close()

    def play_marks(self,marcas):
        """Reproduce la cantidad de marcas indicadas a partir de la posición actual del iterador."""
        sp = pysounds.SoundPlayer(len(self.tracks))
        tracks=self.get_tracks()
        iterador = copy.deepcopy(self.iterador)
  
        while marcas >0:
            try:
                marca = iterador.__next__()
                marca.play(tracks,sp)
                marcas-=1
            except StopIteration:
                break
        sp.close()

def guardar_en_plp(cancion,archivo):
    """Función que recibe un objeto cancion y el nombre de un archivo de extensión plp, y guarda la canción en ese archivo."""
    with open (archivo,'w') as f:
        tracks=cancion.tracks
        f.write('FIELD,DATA\n')
        cantidad_de_tracks=len(tracks)
        f.write('C,'+str(cantidad_de_tracks)+"\n")
        for i in range (cantidad_de_tracks):
            if tracks[i].funcion=="SQ":
                f.write("S,{}{}|{}|{}\n".format(tracks[i].funcion,int(tracks[i].duty_cycle*100),tracks[i].frecuencia,tracks[i].volumen))
            else:
                f.write("S,{}|{}|{}\n".format(tracks[i].funcion,tracks[i].frecuencia,tracks[i].volumen))
        actual=cancion.marcas.prim
        valor=""
        f.write("T,{}\n".format(actual.dato.duracion))
        f.write("N,")
        for i in range(cantidad_de_tracks):
            if actual.dato.notas[i]:
                valor="#"
            else:
                valor="."
            if i==(cantidad_de_tracks-1):
                f.write("{}\n".format(valor))
            else:
                f.write(valor)
        anterior=actual
        actual=actual.prox
        while actual:
            if anterior.dato.duracion!=actual.dato.duracion:
                f.write("T,{}\n".format(str(actual.dato.duracion)))
            f.write("N,")
            for i in range (len(actual.dato.notas)):
                if actual.dato.notas[i]:
                    valor="#"
                else:
                    valor="."
                if i==(cantidad_de_tracks-1):
                    f.write("{}\n".format(valor))
                else:
                    f.write(valor)
            anterior=actual
            actual=actual.prox

def plp_a_cancion(nombre):
    """Función que recibe un archivo plp, y devuelve su conversión al objeto canción."""
    cancion = Cancion()
    try:
        archivo = open(nombre)
        archivo.readline()
        linea = archivo.readline()
        linea = archivo.readline()
        while linea:
            tipo = linea.split(",")
            while tipo[0] == "S":
                onda = tipo[1]
                caracteristicas = onda.split("|")
                func = caracteristicas[0]
                t_func = ""
                duty_cycle = ""
                frecuencia = caracteristicas[1]
                volumen = caracteristicas [2]
                for char in func:
                    if char.isdigit():
                        duty_cycle += char
                    else:
                        t_func += char
                if duty_cycle=="":
                    duty_cycle="0"
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
        if cancion.marcas.prim:
            cancion.iterador=_IteradorListaEnlazada(cancion.marcas.prim)
        return cancion
    except FileNotFoundError:
        print("Archivo no encontrado")


import cmd

class Shell(cmd.Cmd):
    intro = 'Bienvenido a mi programa.\nIngrese help o ? para listar los comandos.\nUsted se encuentra en modo reproduccion. Si quiere cambiar a modo edición ingrese MODO EDICION\n'
    prompt = '*>> '
    def __init__(self):
        """Constructor de la consola de comandos."""
        cmd.Cmd.__init__(self)
        self.cancion_actual=None
        self.modo_actual="REPRODUCCION"

    def do_REPRODUCIR(self,cancion):
        """Reproduce la canción actual."""
        if self.modo_actual!="REPRODUCCION":
            print("Lo lamento, este comando solo funciona si usted se encuentra en el modo reproducción")
        else:
            cancion_a_reproducir=plp_a_cancion(cancion)
            if cancion_a_reproducir:
                cancion_a_reproducir.play()

    def do_PLAY(self,nada):
        """Reproduce la marka actual en la que se encuentra el cursor."""
        if self.modo_actual!="EDICION":
            print(MENSAJE_MODO_INCORRECTO)
        elif not self.cancion_actual.iterador:
            print("No hay marcas de tiempo")
        else:
            sp = pysounds.SoundPlayer(len(self.cancion_actual.tracks))
            self.cancion_actual.iterador.dato_actual().play(self.cancion_actual.get_tracks(),sp)
            sp.close()

    def do_PLAYALL(self,nada):
        """Reproduce la canción en edición actual."""
        if self.modo_actual!="EDICION":
            print(MENSAJE_MODO_INCORRECTO)
        elif not self.cancion_actual.iterador:
            print("No hay marcas de tiempo")
        else:
            self.cancion_actual.play()

    def do_PLAYSECONDS(self,segundos):
        """Reproduce la cantidad de segundos indicada a partir de la posición actual del cursor."""
        if self.modo_actual!="EDICION":
            print(MENSAJE_MODO_INCORRECTO)
        elif not self.cancion_actual.iterador:
            print("No hay marcas de tiempo")
        else:
            try:
                sp = pysounds.SoundPlayer(len(self.cancion_actual.tracks))
                self.cancion_actual.play_seconds(float(segundos))
                sp.close()
            except ValueError:
                input("Ingrese correctamente los segundos")

    def do_PLAYMARKS(self,marcas):
        """Reproduce la cantidad de marcas indicada a partir de la posición actual del cursor."""
        if self.modo_actual!="EDICION":
            print(MENSAJE_MODO_INCORRECTO)
        elif not self.cancion_actual.iterador:
            print("No hay marcas de tiempo")
        else:
            try:
                sp = pysounds.SoundPlayer(len(self.cancion_actual.tracks))
                self.cancion_actual.play_marks(int(marcas))
                sp.close()
            except ValueError:
                input("Ingrese correctamente la cantidad de marcas")

    def do_MODO(self,modo):
        """Cambia al modo indicado."""
        if modo==self.modo_actual:
            print("Ya se encuentra en el modo {}".format(self.modo_actual))
        elif modo=="REPRODUCCION":
            self.modo_actual=modo
        elif modo=="EDICION":
            self.modo_actual=modo
            self.cancion_actual=Cancion()
        else:
            print("Modo inválido, por favor ingrese un modo válido (EDICION o REPRODUCCION)")

    def do_LOAD(self,cancion):
        """Carga un archivo plp y reemplaza la canción actual en edición."""
        if self.modo_actual!="EDICION":
            print(MENSAJE_MODO_INCORRECTO)
        else:
            self.cancion_actual=plp_a_cancion(cancion)
    def do_STORE(self,nombre):
        if self.modo_actual!="EDICION":
            print(MENSAJE_MODO_INCORRECTO)
        else:
            guardar_en_plp(self.cancion_actual,nombre)

    def do_STEP(self,parametro):
        """Avanza el cursor una marca hacia adelante."""
        if self.modo_actual!="EDICION":
            print(MENSAJE_MODO_INCORRECTO)
        else:
            if not self.cancion_actual.iterador:
                print("No hay marcas de tiempo")
            else:
                if self.cancion_actual.iterador.hay_next():
                    self.cancion_actual.iterador.__next__()
                    print("Has avanzado una marca")

    def do_BACK(self,line):
        """Retrocede el cursor una marca hacia atrás."""
        if self.modo_actual!="EDICION":
            print(MENSAJE_MODO_INCORRECTO)
        else:
            if not self.cancion_actual.iterador:
                print("No hay marcas de tiempo")
            else:
                if self.cancion_actual.iterador.hay_back():
                    self.cancion_actual.iterador.back()
                    print("Has retrocedido una marca")

    def do_STEPM(self,marcas):
        """Avanza el cursor tantas marcas hacia adelante como el usuario haya indicado."""
        if self.modo_actual!="EDICION":
            print(MENSAJE_MODO_INCORRECTO)
        else:
            if not self.cancion_actual.iterador:
                print("No hay marcas de tiempo")
            else:
                try:
                    if int(marcas)<1:
                        print("Ingrese un valor mayor o igual a 1")
                    else:
                        for x in range (int(marcas)):
                            if self.cancion_actual.iterador.hay_next(): 
                                self.cancion_actual.iterador.__next__()
                        
                except ValueError:
                    print("Ingrese un número válido")

    def do_BACKM(self,marcas):
        """Retrocede el cursor tantas marcas hacia atrás como el usuario haya indicado."""
        if self.modo_actual!="EDICION":
            print(MENSAJE_MODO_INCORRECTO)
        else:
            if not self.cancion_actual.iterador:
                print("No hay marcas de tiempo")
            else:
                try:
                    if int(marcas)<1:
                        print("Ingrese un valor mayor o igual a 1")
                    else:
                        for x in range (int(marcas)):
                            if self.cancion_actual.iterador.hay_back(): 
                                self.cancion_actual.iterador.back()

                except ValueError:
                    print("Ingrese un número válido")

    def do_TRACKADD(self,datos):
        """Agrega un track a la canción, siendo indicados los atributos del mismo."""
        if self.modo_actual!="EDICION":
            print(MENSAJE_MODO_INCORRECTO)
        else:
            try:
                datos=datos.split()
                if len(datos)!=3:
                    print("Ingrese los parámetros correctamente")
            
                elif not datos[0] =="SIN" and not datos[0] =="SQ" and not datos[0] =="TRIA":
                    print("El parámetro para la función es incorrecto")

                else:
                    self.cancion_actual.agregar_track(datos[0],float(datos[1]),float(datos[2]))
                    input("Nota agregada correctamente")
            except ValueError:
                print("Ingrese valores correctos")

    def do_TRACKDEL(self,track):
        """Elimina el track indicado de la función."""
        if self.modo_actual!="EDICION":
            print(MENSAJE_MODO_INCORRECTO)
        else:
            try:
                track=int(track)
                cantidad_de_tracks=len(self.cancion_actual.tracks)
                if track>cantidad_de_tracks:
                    print("Ingrese un valor menor o igual a {}".format(str(track)))
                self.cancion_actual.borrar_track(track)
                input("Nota borrada correctamente")
            except ValueError:
                print("Ingrese un valor numérico")

    def do_MARKADD(self,duracion):
        """Agrega una nueva marca con la duración indicada a la canción."""
        if self.modo_actual!="EDICION":
            print(MENSAJE_MODO_INCORRECTO)
        else:
            try:
                duracion=float(duracion)
                if self.cancion_actual.marcas.prim==None:
                    self.cancion_actual.agregar_marca(0,duracion)
                else:
                    marca_actual=self.cancion_actual.iterador.dato_actual()
                    posicion_actual=self.cancion_actual.dar_posicion(marca_actual)
                    self.cancion_actual.agregar_marca(posicion_actual,duracion)
                    self.cancion_actual.iterador.back()
                    input("Marca agregada correctamente")
            except ValueError:
                print("Ingrese un número válido")

    def do_MARKADDNEXT(self,duracion):
        """Agrega una nueva marca con la duración indicada inmediatamente después de la posición actual del cursor."""
        if self.modo_actual!="EDICION":
            print(MENSAJE_MODO_INCORRECTO)
        else:
            try:
                duracion=float(duracion)
                if self.cancion_actual.marcas.prim==None:
                    self.cancion_actual.agregar_marca(0,duracion)
                else:
                    marca_actual=self.cancion_actual.iterador.dato_actual()
                    posicion_actual=self.cancion_actual.dar_posicion(marca_actual)
                    self.cancion_actual.agregar_marca(posicion_actual+1,duracion)
                    input("Marca agregada correctamente")
            except ValueError:
                print("Ingrese un número válido")

    def do_MARKADDPREV(self,duracion):
        """Agrega una nueva marca con la duración indicada inmediatamente antes de la posición actual del cursor."""
        if self.modo_actual!="EDICION":
            print(MENSAJE_MODO_INCORRECTO)
        else:
            try:
                duracion=float(duracion)
                if self.cancion_actual.marcas.prim==None:
                    self.cancion_actual.agregar_marca(0,duracion)
                else:
                    marca_actual=self.cancion_actual.iterador.dato_actual()
                    posicion_actual=self.cancion_actual.dar_posicion(marca_actual)
                    self.cancion_actual.agregar_marca(posicion_actual,duracion)
                    input("Marca agregada correctamente")
            except ValueError:
                print("Ingrese un número válido")

    def do_TRACKON(self,track):
        """Habilita el track indicado en la marca actual."""
        if self.modo_actual!="EDICION":
            print(MENSAJE_MODO_INCORRECTO)
        else:
            try:
                numero_de_track=int(track)
                if numero_de_track>len(self.cancion_actual.tracks):
                    print("Track no encontrado")
                elif not self.cancion_actual.iterador:
                    print("No hay marcas de tiempo")
                else:
                    self.cancion_actual.iterador.dato_actual().habilitar_track(numero_de_track)
                    print("Nota activada")
            except ValueError:
                print("Ingrese un valor válido")

    def do_TRACKOFF(self,track):
        """Deshabilita el track indicado en la marca actual."""
        if self.modo_actual!="EDICION":
            print(MENSAJE_MODO_INCORRECTO)
        else:
            try:
                numero_de_track=int(track)
                if numero_de_track>len(self.cancion_actual.tracks):
                    print("Track no encontrado")
                elif not self.cancion_actual.iterador:
                    print("No hay marcas de tiempo")
                else:
                    self.cancion_actual.iterador.dato_actual().deshabilitar_track(numero_de_track)
                    print("Nota desactivada")
            except ValueError:
                print("Ingrese un valor válido")    

Shell().cmdloop()

