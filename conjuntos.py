"""
Si el problema dice                        Operación          Simbolo/Método

"Lo que tienen en común" o "Se cruzan" 	   Intersección	      & o .interseccion()
"El total de elementos" o "Combinar"	   Unión	          | o .union()
"Lo que tiene uno que el otro no"	       Diferencia	      - o .diferencia()
"Lo que no comparten" (exclusivos)	       Dif. Simétrica	  ^ o .dif_simetrica()
"¿Tiene todos los permisos/elementos?"	   Subconjunto	      <= o .es_subconjunto()


Pregunta 1 (Seguridad): Tienes un rol_invitado y un rol_editor.
¿Cómo verificas si el editor tiene al menos todos los permisos del invitado?
Respuesta: Usando invitado <= editor (o invitado.es_subconjunto(editor)).
Si devuelve True, el editor es "superior" o igual al invitado.


Pregunta 2 (Netflix/Similitud): ¿Para qué sirve el Índice de Jaccard y
por qué dividimos la Intersección entre la Unión?
Respuesta: Sirve para medir qué tan parecidos son dos conjuntos.
Dividimos entre la Unión para "normalizar" el resultado entre 0 y 1.
Si solo usáramos la intersección, dos películas con 100 géneros
parecerían más similares que dos con 3, aunque estas últimas fueran idénticas.


Pregunta 3 (Red Social): ¿Cómo sugieres amigos que "quizás conozcas"?
Respuesta: Tomas la Unión de todos los amigos de tus amigos,
y luego le aplicas una Diferencia con tu propio conjunto de amigos (y contigo mismo).
Lo que sobra es gente que tus amigos conocen pero tú no.

"""

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Conjunto:
    def __init__(self, elementos=None):
        self.cabeza = None
        self.tamaño = 0
        
        # Si al crear el conjunto pasas una lista [1,2,3], 
        # este bucle los agrega uno por uno automáticamente.
        if elementos:
            for e in elementos:
                self.agregar(e)
    
    # --- OPERACIONES BÁSICAS ---
    
    def esta_vacio(self):
        # Si la cabeza es None, no hay vagones en el tren.
        return self.cabeza is None
    
    def pertenece(self, x):
        """¿x ∈ Conjunto? (Búsqueda Lineal)"""
        actual = self.cabeza
        while actual:
            if actual.dato == x: # Si lo encuentra, termina y dice True
                return True
            actual = actual.siguiente # Pasa al siguiente nodo
        return False # Si sale del while y no lo vio, no existe.
    
    def agregar(self, x):
        """Regla de Oro: No duplicados"""
        # Primero verifica si YA existe usando la función de arriba
        if self.pertenece(x):
            return False # Si ya está, no hace nada y avisa con False
        
        # Si no está, crea el nodo y lo pone de PRIMERO (en la cabeza)
        nuevo = Nodo(x)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo
        self.tamaño += 1
        return True
    
    def eliminar(self, x):
        """Quitar x (Manejo de punteros)"""
        if self.esta_vacio():
            return False
        
        # CASO ESPECIAL: El elemento es la cabeza
        if self.cabeza.dato == x:
            self.cabeza = self.cabeza.siguiente
            self.tamaño -= 1
            return True
        
        # BUSQUEDA: Usamos 'actual' para mirar el dato del SIGUIENTE nodo
        actual = self.cabeza
        while actual.siguiente:
            if actual.siguiente.dato == x:
                # El "salto": el actual apunta al que seguía del que borramos
                actual.siguiente = actual.siguiente.siguiente
                self.tamaño -= 1
                return True
            actual = actual.siguiente
        return False
    
    # --- OPERACIONES ENTRE CONJUNTOS ---
    
    def union(self, otro):
        """A ∪ B: Meter todo en una bolsa nueva"""
        resultado = Conjunto()
        
        # Primero mete todos los de este conjunto (self)
        actual = self.cabeza
        while actual:
            resultado.agregar(actual.dato)
            actual = actual.siguiente
        
        # Luego mete todos los del otro conjunto
        # (El método .agregar evitará que se repitan los comunes)
        actual = otro.cabeza
        while actual:
            resultado.agregar(actual.dato)
            actual = actual.siguiente
        
        return resultado
    
    def interseccion(self, otro):
        """A ∩ B: Solo los que están en AMBOS"""
        resultado = Conjunto()
        actual = self.cabeza
        while actual:
            # Si el dato actual de A también está en B, lo guardo
            if otro.pertenece(actual.dato):
                resultado.agregar(actual.dato)
            actual = actual.siguiente
        return resultado
    
    def diferencia(self, otro):
        """A - B: Lo que está en A pero NO en B"""
        resultado = Conjunto()
        actual = self.cabeza
        while actual:
            # Si el dato de A NO está en B, es un dato único de A
            if not otro.pertenece(actual.dato):
                resultado.agregar(actual.dato)
            actual = actual.siguiente
        return resultado
    
    # --- RELACIONES ---
    
    def es_subconjunto(self, otro):
        """¿Todos mis elementos están en el otro?"""
        actual = self.cabeza
        while actual:
            #Si encuentro uno solo que NO esté allá, ya no soy subconjunto
            if not otro.pertenece(actual.dato):
                return False
            actual = actual.siguiente
        return True #Si revisé todos y todos estaban, soy subconjunto.

    def a_lista(self):
        """Utilidad para ver los datos en formato [1, 2, 3]"""
        res = []
        act = self.cabeza
        while act:
            res.append(act.dato)
            act = act.siguiente
        return res




