"""
═══════════════════════════════════════════════════════════════════════════════
CASO DE USO 2: UNIVERSIDAD - CRUCE DE HORARIOS
Algoritmos y Programación 4 - Semana 6
═══════════════════════════════════════════════════════════════════════════════

ENUNCIADO:
----------
La universidad necesita un sistema para analizar la matrícula de estudiantes.
Dados los estudiantes inscritos en diferentes materias, el sistema debe:

1. Encontrar estudiantes que cursan ambas materias (para evitar cruces)
2. Encontrar estudiantes que solo cursan una materia
3. Total de estudiantes únicos entre todas las materias
4. Verificar si todos los de una materia están en otra
5. Encontrar estudiantes que cursan las 3 materias

Implementar usando operaciones de conjuntos.

Para "Cruce de Horarios": Siempre piensa en Intersección (&).
Si te piden el cruce de cualquier par de materias,
debes hacer las combinaciones: (A & B), (A & C), (B & C).

Para "Solo en una materia": Recuerda que debes restar todos los demás conjuntos.
No basta con A - B, debe ser A - B - C.

Diferencia entre len() y el conjunto: Si el profesor te pide el número de estudiantes,
usa len(conjunto). Si te pide los nombres, usa el conjunto directamente o sorted(conjunto).
"""

# ═══════════════════════════════════════════════════════════════════════════════
# DATOS
# ═══════════════════════════════════════════════════════════════════════════════
# Cada conjunto representa una lista de asistencia a una materia.
algoritmos = {
    "Ana", "Carlos", "Diana", "Eduardo", "Fernanda",
    "Gabriel", "Helena", "Ivan"
}

bases_datos = {
    "Carlos", "Diana", "Juan", "Karen",
    "Gabriel", "Luis", "Maria"
}

redes = {
    "Diana", "Eduardo", "Gabriel", "Karen",
    "Natalia", "Oscar", "Ivan"
}

# ═══════════════════════════════════════════════════════════════════════════════
# SOLUCIÓN
# ═══════════════════════════════════════════════════════════════════════════════

print("=" * 60)
print("   UNIVERSIDAD - CRUCE DE HORARIOS")
print("=" * 60)

print(f"\nAlgoritmos ({len(algoritmos)}): {sorted(algoritmos)}")
print(f"Bases de Datos ({len(bases_datos)}): {sorted(bases_datos)}")
print(f"Redes ({len(redes)}): {sorted(redes)}")


# 1. INTERSECCIÓN DE PARES (&): "Posibles Cruces de Horario"
# Encuentra estudiantes que están en DOS materias al mismo tiempo.
# Se usa el símbolo '&' entre los nombres de los conjuntos.
cruce_alg_bd = algoritmos & bases_datos
print(f"\n1. Cursan Algoritmos Y Bases de Datos: {sorted(cruce_alg_bd)}")

cruce_alg_redes = algoritmos & redes
print(f"   Cursan Algoritmos Y Redes: {sorted(cruce_alg_redes)}")

cruce_bd_redes = bases_datos & redes
print(f"   Cursan Bases de Datos Y Redes: {sorted(cruce_bd_redes)}")


# 2. DIFERENCIA MÚLTIPLE (-): "Los Exclusivos"
# A los de Algoritmos les RESTAMOS los que están en BD y también los de Redes.
# Resultado: Personas que SOLO ven Algoritmos y nada más.
# Uso: Saber quiénes tienen carga académica ligera.
solo_algoritmos = algoritmos - bases_datos - redes
solo_bd = bases_datos - algoritmos - redes
solo_redes = redes - algoritmos - bases_datos

print(f"\n2. Solo Algoritmos: {sorted(solo_algoritmos)}")
print(f"   Solo Bases de Datos: {sorted(solo_bd)}")
print(f"   Solo Redes: {sorted(solo_redes)}")


# 3. UNIÓN TOTAL (|): "Población Estudiantil"
# Une los 3 conjuntos. No importa si alguien aparece en los 3, 
# en el resultado final (todos) solo aparecerá una vez.
todos = algoritmos | bases_datos | redes
print(f"\n3. Total estudiantes únicos: {len(todos)}")
print(f"   Estudiantes: {sorted(todos)}")


# 4. SUBCONJUNTO (<=): "Validación de Grupos"
# algoritmos <= bases_datos pregunta: "¿Están TODOS los de Algoritmos en BD?"
# cruce_alg_bd <= algoritmos: Esta siempre será True, porque el cruce es 
# por definición una parte del grupo original.
# 4. ¿Todos los de Algoritmos están en Bases de Datos?
print(f"\n4. ¿Algoritmos ⊆ Bases de Datos? {algoritmos <= bases_datos}")
print(f"   ¿Cruce Alg-BD ⊆ Algoritmos? {cruce_alg_bd <= algoritmos}")


# 5. INTERSECCIÓN TRIPLE (& &): "Los más ocupados"
# Solo los nombres que aparecen en los TRES conjuntos simultáneamente.
# Si el resultado es un conjunto vacío, nadie tiene ese cruce triple.
en_las_tres = algoritmos & bases_datos & redes
print(f"\n5. Cursan las 3 materias: {sorted(en_las_tres)}")


# --- RESUMEN POR ESTUDIANTE (Iteración y Pertenencia) ---
# Este bucle recorre a todos los estudiantes únicos y usa 'in' 
# para verificar en qué conjunto está cada uno.
print("\n" + "=" * 60)
print("RESUMEN POR ESTUDIANTE")
print("=" * 60)
for estudiante in sorted(todos):
    materias = []
    if estudiante in algoritmos: # Hacer algo si está en Algoritmos
        materias.append("Algoritmos")
    if estudiante in bases_datos:
        materias.append("BD")
    if estudiante in redes:
        materias.append("Redes")
    print(f"  {estudiante}: {', '.join(materias)} ({len(materias)} materias)")