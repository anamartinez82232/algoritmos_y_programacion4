"""
Sistema de Gestión de Tareas (To-Do List)
"""

class Tarea:
    def __init__(self, descripcion, prioridad):
        self.descripcion = descripcion
        self.prioridad = prioridad  # 1 a 5
        self.completada = False     # Por defecto inicia pendiente
        self.siguiente = None

    def __str__(self):
        estado = "[✓]" if self.completada else "[ ]"
        return f"{estado} Prio:{self.prioridad} - {self.descripcion}"

class ListaTareas:
    def __init__(self):
        self.cabeza = None

    #2: AGREGAR ORDENADO - RECURSIVO
    def agregar_tarea(self, desc, prio, nodo="inicio"):
        # Manejo de la primera llamada para actualizar la cabeza
        if nodo == "inicio":
            self.cabeza = self.agregar_tarea(desc, prio, self.cabeza)
            return

        # Caso Base1: Si la lista terminó o encontramos su lugar
        if nodo is None:
            return Tarea(desc, prio)

        # Caso Base2: Si la nueva tiene MAYOR prioridad, va ANTES que el nodo actual
        if prio > nodo.prioridad:
            nueva = Tarea(desc, prio)
            nueva.siguiente = nodo
            return nueva

        #Paso Recursivo: Si es menor o igual, intentamos insertar en el siguiente
        nodo.siguiente = self.agregar_tarea(desc, prio, nodo.siguiente)
        return nodo

    #3: CONTAR PENDIENTES
    def contar_pendientes(self, prio_buscada, nodo="inicio"):
        if nodo == "inicio":
            nodo = self.cabeza
            
        if nodo is None:
            return 0
        
        # Verificamos si cumple ambas condiciones: prioridad y no completada
        valido = 1 if (nodo.prioridad == prio_buscada and not nodo.completada) else 0
        
        return valido + self.contar_pendientes(prio_buscada, nodo.siguiente)

    #4: OBTENER URGENTES - RECURSIVO
    def obtener_urgentes(self):
        nueva_lista = ListaTareas()
        self._urgentes_recursivo(self.cabeza, nueva_lista)
        return nueva_lista

    def _urgentes_recursivo(self, nodo, nueva_lista):
        if nodo is None:
            return
        
        # Filtro: Prioridad 4 o 5 Y NO completada
        if nodo.prioridad >= 4 and not nodo.completada:
            # Importante: Usamos el método de agregar de la nueva lista
            nueva_lista.agregar_tarea(nodo.descripcion, nodo.prioridad)
            
        self._urgentes_recursivo(nodo.siguiente, nueva_lista)

    #5: LIMPIAR COMPLETADAS - RECURSIVO
    def limpiar_completadas(self, nodo="inicio"):
        if nodo == "inicio":
            self.cabeza = self.limpiar_completadas(self.cabeza)
            return

        if nodo is None:
            return None

        #Primero resolvemos el resto de la lista (de atrás hacia adelante)
        nodo.siguiente = self.limpiar_completadas(nodo.siguiente)

        #Si el nodo actual está completado, lo "saltamos"
        if nodo.completada:
            return nodo.siguiente
        
        return nodo

    #Método extra para mostrar la lista
    def imprimir_lista(self):
        if not self.cabeza:
            print("No hay tareas.")
            return
        temp = self.cabeza
        while temp:
            print(temp)
            temp = temp.siguiente

    #Método para simular completar una tarea (para probar el sistema)
    def completar_tarea(self, desc):
        temp = self.cabeza
        while temp:
            if temp.descripcion.lower() == desc.lower():
                temp.completada = True
                return True
            temp = temp.siguiente
        return False

"""
CONTEXTO:
Una startup te ha contratado para implementar un sistema de gestión de tareas.
Debes diseñar e implementar el sistema usando listas enlazadas.
Cada tarea tiene una prioridad del 1 (baja) al 5 (urgente).

INSTRUCCIONES:
--------------
1. Diseñar la clase Nodo (Tarea) con los atributos necesarios
2. Diseñar la clase Lista (ListaTareas) con los métodos requeridos
3. Usar RECURSIVIDAD en los métodos donde se indique
4. No usar listas de Python [], solo tu estructura de nodos
5. Tiempo: 90 minutos

PUNTO 1 (1.0): DISEÑO DE ESTRUCTURAS
-------------------------------------
Diseña las clases necesarias:

a) Clase NODO (Tarea):
- Debe almacenar: descripción, prioridad (1-5), estado (completada o no)
- Debe poder enlazarse con otra tarea

b) Clase LISTA (ListaTareas):
- Debe mantener referencia al inicio de la lista
- Las tareas deben mantenerse ORDENADAS por prioridad (mayor primero)


PUNTO 2 (1.0): AGREGAR TAREA ORDENADA - RECURSIVO
-------------------------------------------------
Implementa un método para agregar una nueva tarea.
- La tarea debe insertarse en la posición correcta según su prioridad
- Mayor prioridad va primero
- OBLIGATORIO usar recursividad

Ejemplo:
Si la lista tiene prioridades [5, 3, 1] y agregas prioridad 4
Debe quedar [5, 4, 3, 1]


PUNTO 3 (0.75): CONTAR PENDIENTES - RECURSIVO
---------------------------------------------
Implementa un método que cuente las tareas NO completadas
que tengan cierta prioridad.
- OBLIGATORIO usar recursividad

Ejemplo:
contar_pendientes(5) retorna cuántas tareas urgentes hay sin completar


PUNTO 4 (1.0): OBTENER URGENTES - RECURSIVO
-------------------------------------------
Implementa un método que retorne una NUEVA lista con las tareas
de prioridad 4 o 5 que NO estén completadas.
- OBLIGATORIO usar recursividad
- No modificar la lista original

Ejemplo:
urgentes = lista.obtener_urgentes()
# Nueva lista solo con tareas urgentes pendientes


PUNTO 5 (1.25): LIMPIAR COMPLETADAS - RECURSIVO
-----------------------------------------------
Implementa un método que elimine TODAS las tareas completadas.
- OBLIGATORIO usar recursividad
- Modificar la lista original

Ejemplo:
Antes: [✓]Tarea1 -> [○]Tarea2 -> [✓]Tarea3 -> [○]Tarea4
Después: [○]Tarea2 -> [○]Tarea4
"""

def menu():
    print("\n" + "="*35)
    print("      GESTIÓN DE TAREAS (STARTUP)")
    print("="*35)
    print("1. Agregar tarea (Ordenada)")
    print("2. Marcar tarea como completada")
    print("3. Ver todas las tareas")
    print("4. Contar pendientes por prioridad")
    print("5. Ver solo URGENTES (4 y 5)")
    print("6. Limpiar todas las completadas")
    print("7. Salir")
    print("="*35)

mi_lista = ListaTareas()

while True:
    menu()
    opcion = input("Seleccione: ")

    if opcion == "1":
        d = input("Descripción: ")
        p = int(input("Prioridad (1-5): "))
        mi_lista.agregar_tarea(d, p)
        print("Tarea agregada y ordenada.")

    elif opcion == "2":
        d = input("Descripción de la tarea terminada: ")
        if mi_lista.completar_tarea(d):
            print("¡Tarea completada!")
        else:
            print("No se encontró la tarea.")

    elif opcion == "3":
        print("\n--- LISTA DE TAREAS ---")
        mi_lista.imprimir_lista()

    elif opcion == "4":
        p = int(input("¿Prioridad a contar?: "))
        print(f"Tienes {mi_lista.contar_pendientes(p)} tareas pendientes con prioridad {p}.")

    elif opcion == "5":
        print("\n--- TAREAS URGENTES PENDIENTES ---")
        urgentes = mi_lista.obtener_urgentes()
        urgentes.imprimir_lista()

    elif opcion == "6":
        mi_lista.limpiar_completadas()
        print("Historial limpio (Completadas eliminadas).")

    elif opcion == "7":
        break


if __name__ == "__main__":
    print("=" * 60)
    print("         PRUEBAS DEL SISTEMA DE TAREAS")
    print("=" * 60)
    
    # Crear lista de tareas
    mis_tareas = ListaTareas()
    
    # Agregar tareas (deben quedar ordenadas por prioridad)
    mis_tareas.agregar("Comprar leche", 2)
    mis_tareas.agregar("Estudiar para parcial", 5)
    mis_tareas.agregar("Llamar al médico", 4)
    mis_tareas.agregar("Ver serie", 1)
    mis_tareas.agregar("Entregar proyecto", 5)
    mis_tareas.agregar("Hacer ejercicio", 3)
    
    print("\\n📋 Lista de tareas (ordenada por prioridad):")
    mis_tareas.mostrar()  # Implementa este método para visualizar
    print("   Esperado orden de prioridades: 5, 5, 4, 3, 2, 1")
    
    # Contar pendientes
    print("\\n🔢 Tareas urgentes (prioridad 5):", mis_tareas.contar_pendientes(5))
    print("   Esperado: 2")
    
    # Marcar algunas como completadas (implementa un método para esto)
    # mis_tareas.completar("Comprar leche")
    # mis_tareas.completar("Ver serie")
    # mis_tareas.completar("Estudiar para parcial")
    
    # Obtener urgentes
    print("\\n🚨 Tareas urgentes pendientes:")
    urgentes = mis_tareas.obtener_urgentes()
    urgentes.mostrar()
    
    # Limpiar completadas
    print("\\n🗑️ Eliminando tareas completadas...")
    mis_tareas.limpiar_completadas()
    mis_tareas.mostrar()
"""
