def dcm(a, b):
    d = 1
    n = 1
    while n <= min(a, b):
        if a % n == 0 and b % n == 0:
            d = n
        n += 1
    return d

class Fraccion:
    
    def __init__(self, dividendo, divisor):
        self.dividendo = dividendo
        self.divisor = divisor

    def __str__(self):
        return ("{}/{}".format(self.dividendo, self.divisor))

    def sumar(self, otro):
        return Fraccion(self.dividendo * otro.divisor + otro.dividendo * self.divisor, self.divisor * otro.divisor)

    def multiplicar(self, otro):
        return Fraccion(self.dividendo * otro.dividendo, self.divisor * otro.divisor)

    def simplificar(self):
        div_comun_mayor = dcm(self.dividendo, self.divisor)
        self.dividendo = self.dividendo // div_comun_mayor
        self.divisor = self.divisor // div_comun_mayor