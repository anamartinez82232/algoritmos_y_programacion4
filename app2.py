class Nodo:
    def __init__(self, dato, nombre):
        self.dato = dato
        self.

class Lista:
    def __init__(self):
        self.cabeza = None


    def agregar(self, dato):
        nuevo = Nodo (dato)

        if not self.cabeza
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente != None
                actual = actual.siguiente
            actual.siguiente = nuevo


    def sumar(self, nodo= None):
        if nodo is None:
            nodo = self.cabeza
        if nodo.siguiente is None
            return 0
        return sumar(nodo.siguiente) + nodo.dato


        def buscar(self, nodo=None, dato, primera_llamada=True)
            if primera_llamada:
                nodo = self.cabeza
            if nodo is None:
                return False

            if nodo.dato == dato:
                return True
            return buscar(nodo.siguiente, dato, False)


        def suma_digito(n):
            if n == 0:
                return 0
            else:
                return(n%10)+suma_digito(n//10)
        print(suma_digito(1503))

        #Busqueda binaria
        