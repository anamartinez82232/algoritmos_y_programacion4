class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class ListaEnlazadaRecursiva:
    def __init__(self):
        self.cabeza = None
    
    def agregar(self, dato):
        """Agrega al final (iterativo para simplicidad)."""
        nuevo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo
    
    # === MÉTODOS RECURSIVOS ===
    
    def longitud(self, nodo=None):
        """Cuenta nodos recursivamente."""
        if nodo is None:
            nodo = self.cabeza
        if nodo is None:
            return 0
        return 1 + self.longitud(nodo.siguiente)
    
    def suma(self, nodo=None):
        """Suma todos los datos recursivamente."""
        if nodo is None:
            nodo = self.cabeza
        if nodo is None:
            return 0
        return nodo.dato + self.suma(nodo.siguiente)
    
    def buscar(self, dato, nodo=None, primera_llamada=True):
        """Busca un dato recursivamente."""
        if primera_llamada:
            nodo = self.cabeza
        if nodo is None:
            return False
        if nodo.dato == dato:
            return True
        return self.buscar(dato, nodo.siguiente, False)
    
    def imprimir(self, nodo=None, primera_llamada=True):
        """Imprime la lista recursivamente."""
        if primera_llamada:
            nodo = self.cabeza
        if nodo is None:
            print("None")
            return
        print(f"{nodo.dato} -> ", end="")
        self.imprimir(nodo.siguiente, False)