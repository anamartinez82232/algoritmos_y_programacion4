class Nodo:
    def __init__(self, documento, nombre):
        self.documento = documento
        self.nombre = nombre
        self.siguiente = None

class Listas:
    def __init__(self)
        self.cabeza = None

    def AgregarFinal (self, documento, nombre):
        nodo = Nodo(documento, nombre)

        if self.cabeza == None:
            self.cabeza = nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nodo


#Para cuando hay muchas entradas
"""
class Nodo:
    def __init__(self, documento, nombre):
        self.documento = documento
        self.nombre = nombre
        self.siguiente = None

class Listas:
    def __init__(self)
        self.cabeza = None
        self.cola = None

    def AgregarFinal (self, documento, nombre):
        nodo = Nodo(documento, nombre)

        if self.cabeza == None:
            self.cabeza = nodo
            self.cola = nodo
        else:
            self.cola.siguiente = nodo
            self.cola = nodo
"""