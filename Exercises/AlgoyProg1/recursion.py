import random

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
    
def f():
    x = 50
    a = 20
    print("En f, x vale", x)

def g():
    x = 10
    b = 45
    print("En g, antes de llamar a f, x vale", x)
    f()
    print("En g, después de llamar a f, x vale", x)


def fun1(a):
    print(a+1)

def fun2(b):
    fun1(b + 5)
    print("Back to fun2")

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def potencia(b, n):
    
    if n <= 0:
        return 1

    if n % 2 == 0:
        p = potencia(b, n//2)
        return p * p

    else:
        p = potencia(b, (n - 1) // 2)
        return p * p * b

def fib_recurs(n):
    if n == 0 or n == 1:
        return n
    return fib(n - 1) + fib(n - 2)

def fib_iter(n):
    if n == 0 or n == 1:
        return n
    ant2 = 0
    ant1 = 1
    for i in range(2, n + 1):
        fibn = ant1 + ant2
        ant2 = ant1
        ant1 = fibn
    return fibn

def cant_digitos(n):
    if n / 10 < 1:
        return 1
    return 1 + cant_digitos(n//10)

def rata():
    camino = random.randrange(1, 4)
    if camino == 3:
        return 7
    if camino == 1:
        return 3 + rata()
    return 5 + rata()

def es_potencia(n, b):
    def _es_potencia(n, b, e):
        res = b ** e
        if e == n:
            return False
        if n == b ** e:
            return True
        return _es_potencia(n, b, e + 1)
    return _es_potencia(n, b, 0)

def posiciones_de(a, b):
    def _posiciones_de(a, b, ult_pos):
        aux = a[ult_pos:]
        if b not in aux:
            return []
        pos = aux.index(b) + ult_pos
        return [pos] + _posiciones_de(a, b, pos + 1)
    return _posiciones_de(a, b, 0)

def es_par(n):
    if n == 0:
        return True
    return es_impar(n - 1)

def es_impar(n):
    if n == 0:
        return False
    return es_par(n - 1)

def triangular(n):
    if n == 1:
        return n
    return n + triangular(n - 1)

def contar_pila(pila):
    if pila.esta_vacia():
        return 0		
    elemento = pila.desapilar()
    cont = 1 + contar_pila(pila)
    pila.apilar(elemento)
    return cont

def mayor_elemento(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        aux = mayor_elemento(lista[1:])
        if aux > lista[0]:
            return aux
        else:
            return lista[0]

def replicar(lista, n):
    if len(lista) == 0:
        return []
    return [lista[0]] * n + replicar(lista[1:], n)

pilita = Pila()
pilita.apilar(1)
pilita.apilar(2)
pilita.apilar(3)
pilita.apilar(4)
pilita.apilar(5)
pilita.apilar(6)
print(contar_pila(pilita))