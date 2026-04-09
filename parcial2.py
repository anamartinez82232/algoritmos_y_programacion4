1. VALOR 20%

Completa las funciones de validación usando expresiones regulares.

import re

def validar_placa_vehiculo(placa):
"""
Valida si una placa de vehículo colombiana tiene formato correcto.
Formato válido: 3 letras mayúsculas + 3 dígitos (ej: ABC123)
También válido con guion: ABC-123
Ejemplos:
validar_placa_vehiculo("ABC123") -> True
validar_placa_vehiculo("ABC-123") -> True
validar_placa_vehiculo("AB1234") -> False
validar_placa_vehiculo("abc123") -> False
"""
# TODO: Implementar con re.match o re.search
pass

def extraer_hashtags(texto):
"""
Extrae todos los hashtags de un texto.
Un hashtag empieza con # seguido de letras, números o guion bajo.
Ejemplo:
extraer_hashtags("Hola #python es #genial y #100dias")
-> ["#python", "#genial", "#100dias"]
"""
# TODO: Implementar con re.findall
pass
1. Expresiones Regulares (Validación y Extracción)

Para las placas, necesitamos opcionalidad (el guion) y límites estrictos.
Para los hashtags, buscamos el patrón # seguido de caracteres alfanuméricos.
import re

def validar_placa_vehiculo(placa):
    # ^[A-Z]{3} : Empieza con 3 letras mayúsculas
    # -?        : El guion es opcional (0 o 1 vez)
    # \d{3}$    : Termina con exactamente 3 dígitos
    patron = r"^[A-Z]{3}-?\d{3}$"
    return bool(re.match(patron, placa))

def extraer_hashtags(texto):
    # #         : Empieza con el símbolo numeral
    # \w+       : Seguido de uno o más caracteres alfanuméricos (letras, números, _)
    patron = r"#\w+"
    return re.findall(patron, texto)



2. VALOR 30%
Sistema de gestión de pedidos para un restaurante de domicilios.
Cada pedido tiene: cliente, dirección, valor y si está entregado.
Los pedidos se almacenan en una lista enlazada.
"""

class Pedido:
def __init__(self, cliente, direccion, valor, entregado=False):
self.cliente = cliente
self.direccion = direccion
self.valor = valor
self.entregado = entregado
self.siguiente = None
def __str__(self):
estado = "✓" if self.entregado else "○"
return f"[{estado}] {self.cliente} - ${self.valor:,} - {self.direccion}"

class ListaPedidos:
def __init__(self):
self.cabeza = None
def mostrar(self):
actual = self.cabeza
if actual is None:
print(" Sin pedidos")
return
while actual:
print(f" {actual}")
actual = actual.siguiente

def agregar(self, cliente, direccion, valor):
"""
Agrega un nuevo pedido al FINAL de la lista.
OBLIGATORIO usar recursividad.
"""
# TODO: Implementar
pass
def valor_pendiente(self):
"""
Retorna la suma de valores de pedidos NO entregados.
OBLIGATORIO usar recursividad.
Ejemplo:
Pedido1 (entregado, $25000) + Pedido2 (pendiente, $30000)
+ Pedido3 (pendiente, $15000)
-> Retorna 45000
"""
# TODO: Implementar
pass
def eliminar_entregados(self):
"""
Elimina todos los pedidos que ya fueron entregados.
OBLIGATORIO usar recursividad.
Modifica la lista original.
"""
# TODO: Implementar
pass
Punto Crítico: En recursividad de listas, el "caso base" suele ser cuando nodo es None o
nodo.siguiente es None.
class ListaPedidos:
    # ... (init y mostrar ya definidos)

    def agregar(self, cliente, direccion, valor):
        nuevo = Pedido(cliente, direccion, valor)
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            self._agregar_recursivo(self.cabeza, nuevo)

    def _agregar_recursivo(self, actual, nuevo):
        if actual.siguiente is None:
            actual.siguiente = nuevo
        else:
            self._agregar_recursivo(actual.siguiente, nuevo)

    def valor_pendiente(self):
        return self._valor_recursivo(self.cabeza)

    def _valor_recursivo(self, actual):
        if actual is None:
            return 0
        pago = actual.valor if not actual.entregado else 0
        return pago + self._valor_recursivo(actual.siguiente)

    def eliminar_entregados(self):
        self.cabeza = self._eliminar_recursivo(self.cabeza)

    def _eliminar_recursivo(self, actual):
        if actual is None:
            return None
        
        # Primero procesamos el resto de la lista (de atrás hacia adelante)
        actual.siguiente = self._eliminar_recursivo(actual.siguiente)
        
        # Si el actual está entregado, lo "saltamos" retornando el siguiente
        if actual.entregado:
            return actual.siguiente
        return actual



3. VALOR 20%

Un colegio tiene 3 clubes extracurriculares. Cada club tiene un conjunto
de estudiantes inscritos. Responde las preguntas usando operaciones de conjuntos.
"""
club_ciencias = {"Ana", "Carlos", "Diana", "Elena", "Felipe"}
club_deportes = {"Carlos", "Felipe", "Gabriel", "Hugo", "Isabel"}
club_arte = {"Ana", "Diana", "Gabriel", "Julia", "Karen"}

def estudiantes_en_todos():
"""
Retorna el conjunto de estudiantes inscritos en LOS TRES clubes.
(Intersección de los tres)
"""
# TODO: Implementar
pass

def solo_un_club():
"""
Retorna el conjunto de estudiantes que están en EXACTAMENTE un club.
Pista: Un estudiante está en exactamente un club si está en ese club
pero NO en los otros dos.
Ejemplo esperado: {"Elena", "Hugo", "Isabel", "Julia", "Karen"}
"""
# TODO: Implementar
pass

def clubes_de_estudiante(nombre):
"""
Retorna una lista con los nombres de los clubes a los que pertenece
el estudiante.
Ejemplo:
clubes_de_estudiante("Carlos") -> ["Ciencias", "Deportes"]
clubes_de_estudiante("Julia") -> ["Arte"]
"""
# TODO: Implementar
pass
3. Clubes y Conjuntos (Lógica de 3 Grupos)
Este ejercicio pide precisión quirúrgica en las restas de conjuntos.
club_ciencias = {"Ana", "Carlos", "Diana", "Elena", "Felipe"}
club_deportes = {"Carlos", "Felipe", "Gabriel", "Hugo", "Isabel"}
club_arte = {"Ana", "Diana", "Gabriel", "Julia", "Karen"}

def estudiantes_en_todos():
    # Intersección triple
    return club_ciencias & club_deportes & club_arte

def solo_un_club():
    # Solo en ciencias (pero no en los otros dos)
    solo_c = club_ciencias - club_deportes - club_arte
    # Solo en deportes
    solo_d = club_deportes - club_ciencias - club_arte
    # Solo en arte
    solo_a = club_arte - club_ciencias - club_deportes
    # La unión de estos tres resultados
    return solo_c | solo_d | solo_a

def clubes_de_estudiante(nombre):
    resultado = []
    if nombre in club_ciencias: resultado.append("Ciencias")
    if nombre in club_deportes: resultado.append("Deportes")
    if nombre in club_arte: resultado.append("Arte")
    return resultado



4. VALOR 30%

Tienes una escalera de N escalones. En cada paso puedes subir 1 o 2 escalones.
¿De cuántas formas distintas puedes llegar al escalón N?
Ejemplo:
N=1: 1 forma → [1]
N=2: 2 formas → [1+1, 2]
N=3: 3 formas → [1+1+1, 1+2, 2+1]
N=4: 5 formas → [1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2]
"""
def escalones_sin_memo(n):
"""
Calcula de cuántas formas se puede subir una escalera de n escalones.
En cada paso puedes subir 1 o 2 escalones.
Implementar con recursividad pura (sin memorización).
Casos base:
n == 0 -> 1 (hay una forma de "no subir")
n == 1 -> 1
Caso recursivo:
escalones(n) = escalones(n-1) + escalones(n-2)
"""
# TODO: Implementar
pass

def escalones_con_memo(n, memo=None):
"""
Misma función pero usando un diccionario para guardar resultados
ya calculados y evitar recalcular.
Ejemplo:
escalones_con_memo(10) -> 89
escalones_con_memo(30) -> 1346269 (sin memo esto tardaría mucho)
"""
# TODO: Implementar
pass
4. Recursión con Memoización (Escalones)
Este es el problema clásico de Fibonacci disfrazado.
Subir n escalones de 1 en 1 o de 2 en 2 sigue la secuencia: f(n)=f(n−1)+f(n−2).
def escalones_con_memo(n, memo=None):
    if memo is None:
        memo = {}
    
    # Si ya lo calculamos, lo devolvemos de la memoria
    if n in memo:
        return memo[n]
    
    # Casos base
    if n == 0 or n == 1:
        return 1
    
    # Cálculo recursivo guardando en el diccionario
    memo[n] = escalones_con_memo(n - 1, memo) + escalones_con_memo(n - 2, memo)
    return memo[n]