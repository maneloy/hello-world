class Vector:

    def  __init__(self, elementos):
        self.x = elementos[0]
        self.y = elementos[1]
        self.z = elementos[2]
        self.elementos = elementos

    def __str__(self):
        return "[{}, {}, {}]".format(self.x, self.y, self.z)

    def escalar(self, n):
        return Vector([self.x * n, self.y * n, self.z * n])

    def sumar(self, otro):
        if len(self.elementos) != len(otro.elementos):
            raise Exception("Deben tener la misma cantidad de elementos.")
        return Vector([self.x + otro.x, self.y + otro.y, self.z + otro.z])

    