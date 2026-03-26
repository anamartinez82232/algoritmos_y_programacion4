"""
═══════════════════════════════════════════════════════════════════════════════
CASO DE USO 1: SPOTIFY - PLAYLISTS COMPARTIDAS
Algoritmos y Programación 4 - Semana 6
═══════════════════════════════════════════════════════════════════════════════

ENUNCIADO:
----------
Spotify quiere implementar una función de "Playlists Compartidas".
Dados dos usuarios con sus canciones favoritas, el sistema debe:

1. Encontrar canciones que ambos disfrutan (para playlist compartida)
2. Sugerir canciones que uno tiene y el otro no
3. Mostrar el catálogo combinado de ambos
4. Verificar si un usuario escucha un subconjunto de lo que escucha otro

Implementar usando operaciones de conjuntos.

Cuando leas el enunciado del problema, asocia estas palabras clave con los símbolos de tu código:

    "Ambos", "Común", "Cruce" → Usa & (Intersección)

    "Combinar", "Total", "Unir" → Usa | (Unión)

    "Sugerir", "Faltante", "Solo de..." → Usa - (Diferencia)

    "Exclusivo", "No compartido" → Usa ^ (Diferencia Simétrica)

    "Contenido en", "Parte de" → Usa <= (Subconjunto)
"""

# ═══════════════════════════════════════════════════════════════════════════════
# DATOS
# ═══════════════════════════════════════════════════════════════════════════════
# Se usan llaves {} para definir sets (conjuntos). 
# Esto garantiza que no haya canciones repetidas en la lista de cada persona.
canciones_juan = {
    "Blinding Lights", "Bohemian Rhapsody", "Shape of You",
    "Despacito", "Hotel California", "Billie Jean",
    "Rolling in the Deep", "Smells Like Teen Spirit"
}

canciones_maria = {
    "Shape of You", "Despacito", "Bad Guy",
    "Blinding Lights", "Watermelon Sugar", "Levitating",
    "Rolling in the Deep", "drivers license"
}

# ═══════════════════════════════════════════════════════════════════════════════
# SOLUCIÓN
# ═══════════════════════════════════════════════════════════════════════════════

print("=" * 60)
print("   SPOTIFY - PLAYLISTS COMPARTIDAS")
print("=" * 60)

print(f"\nCanciones de Juan ({len(canciones_juan)}):")
for c in sorted(canciones_juan):
    print(f"  ♪ {c}")

print(f"\nCanciones de María ({len(canciones_maria)}):")
for c in sorted(canciones_maria):
    print(f"  ♪ {c}")


# 1. INTERSECCIÓN (&): "Lo que ambos tienen"
# Crea un conjunto con los elementos que aparecen en los DOS grupos.
# Uso: Ideal para encontrar gustos comunes o "Playlist Match".
compartidas = canciones_juan & canciones_maria
print(f"\n1. Playlist compartida ({len(compartidas)} canciones):")
for c in sorted(compartidas):
    print(f"  ♪ {c}")


# 2. DIFERENCIA (-): "Lo que uno tiene que al otro le falta"
# A - B significa: Toma todo lo de A y quítale lo que también esté en B.
# Uso: Recomendaciones. Lo que María conoce y Juan no (sugerencias para Juan).
sugerencias_para_juan = canciones_maria - canciones_juan
sugerencias_para_maria = canciones_juan - canciones_maria

print(f"\n2. Sugerencias para Juan ({len(sugerencias_para_juan)}):")
for c in sorted(sugerencias_para_juan):
    print(f"  → {c}")

print(f"\n   Sugerencias para María ({len(sugerencias_para_maria)}):")
for c in sorted(sugerencias_para_maria):
    print(f"  → {c}")


# 3. UNIÓN (|): "El catálogo total"
# Combina ambos conjuntos. Si una canción está en ambos, SOLO APARECE UNA VEZ.
# Uso: Crear una biblioteca familiar o compartida completa.
catalogo = canciones_juan | canciones_maria
print(f"\n3. Catálogo combinado ({len(catalogo)} canciones únicas):")
for c in sorted(catalogo):
    print(f"  ♪ {c}")


# 4. SUBCONJUNTO (<=): "Inclusión total"
# Devuelve True si TODOS los elementos del primer conjunto están en el segundo.
# Uso: Verificar si los gustos de Juan son una versión pequeña de los de María.
print(f"\n4. ¿Juan escucha subconjunto de María? {canciones_juan <= canciones_maria}")
print(f"   ¿María escucha subconjunto de Juan? {canciones_maria <= canciones_juan}")


# 5. DIFERENCIA SIMÉTRICA (^): "Lo que los hace únicos"
# Es el opuesto a la intersección. Devuelve lo que está en Juan o en María, 
# PERO NO en ambos. 
# Uso: Identificar canciones exclusivas de cada uno para evitar repetidas.
exclusivas = canciones_juan ^ canciones_maria
print(f"\n5. Canciones que solo uno de los dos escucha ({len(exclusivas)}):")
for c in sorted(exclusivas):
    print(f"  ♪ {c}")