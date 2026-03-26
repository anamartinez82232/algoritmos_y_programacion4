#Heap: padre menor que sus hijos
datos = [5, 3, 8, 1, 2, 9, 4]
import heapq
heapq.heapify(datos)
print("Heap: ", datos)

heapq.heappush(datos, 6)
print("Heap despues de agregar el 6: ", datos)

minimo = heapq.heappop(datos)
print("Elemento minimo extraido: ", minimo)
print("Heap después de extraer el minimo: ", datos)

minimo = heapq.heappushpop(datos, 7)
datos2 = [(2, 'A'), (1, 'B'), (3, 'C'), (2, 'B')]
heapq.heapify(datos2)
print("Heap con tuplas: ", datos2)


"""
EJERCICIO
Programa para un hospital
Cada paciente tiene prioridad de 1 a 3, 1 es la más importante
Las personas del hospital deben saber quien es el siguiente en atender
e indicar su nombre y prioridad
"""


class Paciente:
    def __init__(self, nombre, prioridad, turno):
        self.nombre = nombre
        self.prioridad = prioridad
        self.turno = turno

hospital = []
contador_turnos = 0

n = int(input("¿Cuántos pacientes desea ingresar? "))

for i in range(n):
    nombre = input(f"\nNombre del paciente {i+1}: ")
    prioridad = int(input(f"Prioridad de {nombre} (1-3): "))
    
    contador_turnos += 1 #Aumentamos el turno para el desempate
    
    #Creamos el objeto (opcional, pero buena práctica)
    p = Paciente(nombre, prioridad, contador_turnos)
    
    #Guardamos la tupla en el heap: (Prioridad, Turno, Nombre)
    heapq.heappush(hospital, (p.prioridad, p.turno, p.nombre))

print("\n" + "="*30)
print("     SISTEMA DE ATENCIÓN")
print("="*30)

#El ciclo 'while hospital' asegura que atendamos a TODOS hasta que quede vacío
while hospital:
    prio, t, nom = heapq.heappop(hospital)
    print(f"[Turno {t}] Atendiendo a {nom} (Prioridad: {prio})")

"""
EJERCICIO
Un programa que me permita programar tareas y me diga
cual es la siguiente tarea a realizar segun calendario
"""
from datetime import datetime, timedelta
