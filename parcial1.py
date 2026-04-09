"""
1. VALOR 10%
Pregunta: ¿Cuál de las siguientes expresiones regulares coincide con
una dirección de correo
electrónico válida (e.g., usuario@dominio.com)?
a) ^\w+@\w+.\w+$
b) ^.\d+.@.*.[a-z]{2,4}$
c) ^[\w-]+(.[\w-]+)*@([\w-]+.)+[a-zA-Z]{2,7}$
d) ^\d+@\w+.\w+$
Respuesta Correcta: c) ^[\w-]+(.[\w-]+)*@([\w-]+.)+[a-zA-Z]{2,7}$
¿Por qué?: La opción a falla porque el punto . en RegEx significa "cualquier carácter",
a menos que se escape como \.. La opción c es la más robusta porque permite puntos
en el nombre de usuario y valida correctamente la extensión del dominio.



Pregunta: ¿Cuál de las siguientes expresiones regulares coincidiría con
un número de teléfono en el
formato +57 300 1234567?
a) ^\d{2} \d{3} \d{7}$
b) ^+\d{2} \d{3} \d{7}$
c) ^+\d{1,3} \d{3} \d{4,7}$
d) ^+57 \d{3} \d{7}$
Respuesta Correcta: b) ^\+\d{2} \d{3} \d{7}$
(Nota: en el texto original faltaba el escape \, pero es la que tiene la estructura correcta).
¿Por qué?: Debe empezar con el símbolo + (que debe escaparse),
seguido de 2 dígitos del país, espacio, 3 del operador, espacio y 7 del número.



2. VALOR 35%
Imagina que trabajas en una empresa de logística. Tienes un robot que
debe moverse desde la esquina superior izquierda de una bodega
(celda (0,0)) hasta la esquina inferior derecha (m, n).
El robot solo puede moverse hacia la derecha o hacia abajo.
def contar_rutas(m, n):
# Caso base: si está en la primera fila o columna, solo hay 1
ruta
if m == 0 or n == 0:
return 1
# Recursión: suma de rutas desde arriba y desde la izquierda
return contar_rutas(m - 1, n) + contar_rutas(m, n - 1)

# Ejemplo: una cuadrícula de 3x3
print(contar_rutas(3, 3)) # Resultado esperado: 20
Problema: esta versión recalcula muchas veces las mismas subrutas,
lo que hace que sea muy ineficiente para valores grandes (por
ejemplo, contar_rutas(15,15) tarda muchísimo). ¿Cómo podemos
mejorarlo? Implementa la solución.

def contar_rutas_optimizado(m, n, memoria={}):
    # Verificamos si ya calculamos esta posición antes
    if (m, n) in memoria:
        return memoria[(m, n)]
    
    # Caso base: celdas en los bordes
    if m == 0 or n == 0:
        return 1
    
    # Guardamos el resultado en la memoria antes de retornarlo
    memoria[(m, n)] = contar_rutas_optimizado(m - 1, n, memoria) + \
                      contar_rutas_optimizado(m, n - 1, memoria)
    
    return memoria[(m, n)]

# Ejemplo
print(contar_rutas_optimizado(15, 15)) # Ahora es instantáneo




3. VALOR 35%
Una plataforma de streaming ofrece dos planes diferentes:
Plan Cine (películas)
Plan Series (series)
Los usuarios pueden suscribirse a uno u otro, o incluso a los dos.
Queremos analizar la información para tomar decisiones de negocio.
plan_cine = {"Ana", "Luis", "Pedro", "Sofía", "Carlos", "Lucía"}
plan_series = {"Pedro", "Sofía", "Marta", "Andrés", "Lucía", "Valentina"}

Usuarios únicos en la plataforma
¿Qué operación en conjuntos usarías para obtener todos los usuarios
registrados sin duplicados?
Usuarios con ambos planes
¿Quiénes están suscritos tanto a Cine como a Series?
Usuarios solo en el plan Cine
¿Qué operación permite obtener los usuarios que solo tienen Cine,
pero no Series?
Usuarios exclusivos de un solo plan
¿Cómo obtendrías a los usuarios que están en solo uno de los planes
pero no en ambos?
Verificación rápida
¿Cómo verificar si un usuario específico (ej. "Carlos") pertenece al plan
de Series?
La empresa quiere lanzar un plan premium que combine Cine y
Series.
Sin embargo, antes de hacerlo quiere saber:
¿Qué porcentaje de los usuarios actuales ya estarían en el plan
premium porque tienen ambos servicios?
¿Qué porcentaje representa ese grupo respecto al total de usuarios
únicos de la plataforma?
plan_cine = {"Ana", "Luis", "Pedro", "Sofía", "Carlos", "Lucía"}
plan_series = {"Pedro", "Sofía", "Marta", "Andrés", "Lucía", "Valentina"}

# 1. Usuarios únicos (Unión)
todos = plan_cine | plan_series

# 2. Con ambos planes (Intersección)
ambos = plan_cine & plan_series

# 3. Solo Cine (Diferencia)
solo_cine = plan_cine - plan_series

# 4. Exclusivos de un solo plan (Diferencia Simétrica)
solo_uno = plan_cine ^ plan_series

# 5. Verificación rápida (Pertenencia)
esta_carlos = "Carlos" in plan_series

# --- CÁLCULOS DE NEGOCIO ---
total_u = len(todos)
total_premium = len(ambos)

# Porcentaje de usuarios que ya son premium
# (Respecto al total de la plataforma)
porcentaje_total = (total_premium / total_u) * 100

print(f"Usuarios únicos: {todos}")
print(f"Premium (ambos): {ambos}")
print(f"Porcentaje Premium: {porcentaje_total:.2f}%")



4. VALOR 20%

Determina la complejidad con la notación Big O del siguiento algoritmo:
def encontrar_pares(lista, objetivo):
n = len(lista)
for i in range(n):
for j in range(i + 1, n):
if lista[i] + lista[j] == objetivo:
print(f"Par encontrado: ({lista[i]}, {lista[j]})")
# Ejemplo de uso
numeros = [1, 3, 5, 7, 9]
objetivo = 10
encontrar_pares(numeros, objetivo)
¿Cómo se comporta el algoritmo si duplicamos el tamaño de la lista?
¿Existe una forma más eficiente de resolver este problema?
Complejidad Big O

Analizando el código de encontrar_pares:
    Complejidad: Es O(n2) (Cuadrática).
        ¿Por qué?: Tiene un ciclo for anidado dentro de otro.
        El primero recorre n y el segundo aproximadamente n/2 veces.
        En Big O, las constantes se ignoran, quedando n×n=n2.

    Si duplicamos el tamaño de la lista: El tiempo de ejecución no se duplica,
    se cuadriplica (22=4). Si la lista crece 10 veces, el tiempo crece 100 veces.

    ¿Forma más eficiente?: Sí, usando un Conjunto (Set) para buscar el complemento.
    Esto bajaría la complejidad a O(n) (Lineal).
"""