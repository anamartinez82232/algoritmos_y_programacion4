"""
IF
a = 2
if a == 1:
    print ("La variable es igual a 1")

print ("Aquí termina el condicional")

WHILE
a = 2
while a < 10:
    print ("Sigo en el ciclo")
    a = a + 1

print ("Aquí termina el condicional")

FOR
a = 2
for i in range (0, 10):
    print ("Sigo en el ciclo")
    print (i)

print ("Aquí termina el condicional")
"""

class Estudiante:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula

estudiante1 = Estudiante("Ana", 1111)
print (estudiante1.nombre)
