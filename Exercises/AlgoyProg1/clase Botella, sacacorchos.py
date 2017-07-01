class Corcho:
    
    def __init__(self, bodega):
        self.bodega = bodega
    
class Botella:

    def __init__(self, corcho):
        self.corcho = corcho

class Sacacorchos:

    def __init__(self):
        self.contenedor = []

    def destapar(self, botella):
        if botella.corcho == None: raise Exception("Ya está destapada")
        self.contenedor.append(botella.corcho)
        botella.corcho = None

    def limpiar(self):
        if self.contenedor == []: raise Exception("Ya está vacio")
        corcho_sacado = self.contenedor[0]
        self.contenedor = []
        return corcho_sacado


    