# ==============================================================================
# CASO DE USO 6: INFRAESTRUCTURA CLOUD - REDUNDANCIA Y RIESGOS (AVANZADO)
# ==============================================================================
"""
Intersección Dinámica (Método 1):
Es muy común que te den una lista de conjuntos y te pidan la intersección de todos.
El truco del for sobre la lista de llaves es la forma más limpia de hacerlo.

Lógica de Vulnerabilidad (Método 4):
Aquí mezclas Diccionarios con Conjuntos.
Usas la unión |= para saber cuáles son todos los servicios existentes y luego recorres para contar.

Jaccard (Método 5): Lo incluí de nuevo porque, como te dije,
es la "pregunta fija" de similitud en cualquier examen de conjuntos.
"""
# DATOS: Servidores por ciudad y sus servicios activos
servidores = {
    "Bogotá": {"DB", "Web", "Auth", "Backup", "IA"},
    "Medellín": {"Web", "IA", "Cache", "DB"},
    "Cali": {"DB", "Auth", "Storage", "Backup"},
    "Cartagena": {"Web", "Cache", "CDN"},
    "Leticia": {"Backup"}
}

# ------------------------------------------------------------------------------
# MÉTODO 1: SERVICIOS GLOBALES (Intersección de N conjuntos)
# ------------------------------------------------------------------------------
def obtener_servicios_en_todos():
    """¿Qué servicios están presentes en ABSOLUTAMENTE TODAS las ciudades?"""
    ciudades = list(servidores.keys())
    # Empezamos con el conjunto de la primera ciudad
    resultado = servidores[ciudades[0]]
    
    # Vamos intersectando con cada una de las demás
    for i in range(1, len(ciudades)):
        resultado = resultado & servidores[ciudades[i]]
    return resultado

# ------------------------------------------------------------------------------
# MÉTODO 2: ANÁLISIS DE RIESGO ÚNICO (Diferencia Simétrica ^)
# ------------------------------------------------------------------------------
def detectar_servicios_sin_respaldo(ciudad_a, ciudad_b):
    """
    Encuentra servicios que están en A o en B, pero NO en ambos.
    Si una ciudad se cae, estos servicios son los que NO tienen espejo en la otra.
    """
    return servidores[ciudad_a] ^ servidores[ciudad_b]

# ------------------------------------------------------------------------------
# MÉTODO 3: COBERTURA DE EMERGENCIA (Subconjuntos <=)
# ------------------------------------------------------------------------------
def puede_cubrir_emergencia(ciudad_soporte, ciudad_caida):
    """¿Tiene la ciudad de soporte TODOS los servicios que necesita la ciudad caída?"""
    return servidores[ciudad_caida] <= servidores[ciudad_soporte]

# ------------------------------------------------------------------------------
# MÉTODO 4: MAPA DE ESCASEZ (Frecuencia de Servicios)
# ------------------------------------------------------------------------------
def analizar_vulnerabilidad_global():
    """Calcula en cuántas ciudades está cada servicio."""
    conteo = {}
    # Obtenemos el set de todos los servicios posibles (Unión de todos)
    todos_los_servicios = set()
    for s in servidores.values():
        todos_los_servicios |= s
        
    for servicio in todos_los_servicios:
        # Contamos en cuántos conjuntos aparece el servicio
        presencia = 0
        for ciudad_servs in servidores.values():
            if servicio in ciudad_servs:
                presencia += 1
        conteo[servicio] = presencia
    return conteo

# ------------------------------------------------------------------------------
# MÉTODO 5: ÍNDICE DE DISPONIBILIDAD (Jaccard entre Ciudades)
# ------------------------------------------------------------------------------
def similitud_infraestructura(c1, c2):
    """Qué tan parecidas son las configuraciones de dos ciudades."""
    inter = len(servidores[c1] & servidores[c2])
    union = len(servidores[c1] | servidores[c2])
    return inter / union if union > 0 else 0

# ==============================================================================
# EJECUCIÓN Y PRUEBAS
# ==============================================================================

print("--- REPORTE DE INFRAESTRUCTURA CLOUD ---")

# 1. Servicios Globales
globales = obtener_servicios_en_todos()
print(f"1. Servicios en toda la red: {globales if globales else 'Ninguno (Riesgo alto)'}")

# 2. Riesgo Único (Bogotá vs Cali)
riesgo = detectar_servicios_sin_respaldo("Bogotá", "Cali")
print(f"2. Servicios sin respaldo mutuo (Bog-Cali): {riesgo}")

# 3. Cobertura
if puede_cubrir_emergencia("Bogotá", "Leticia"):
    print("3. ✓ Bogotá puede respaldar totalmente a Leticia.")

# 4. Vulnerabilidad (El que menos está, es el más peligroso si se cae)
vulnerabilidad = analizar_vulnerabilidad_global()
# Ordenamos de menor a mayor presencia
servicio_critico = min(vulnerabilidad, key=vulnerabilidad.get)
print(f"4. Servicio más crítico: '{servicio_critico}' (Solo está en {vulnerabilidad[servicio_critico]} ciudad/es)")

# 5. Similitud
sim = similitud_infraestructura("Medellín", "Cartagena")
print(f"5. Similitud Medellín-Cartagena: {sim:.2f}")