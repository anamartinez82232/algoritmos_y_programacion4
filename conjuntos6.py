"""
═══════════════════════════════════════════════════════════════════════════════
CASO DE USO 5: RED SOCIAL - ANÁLISIS DE CONEXIONES
Algoritmos y Programación 4 - Semana 6
═══════════════════════════════════════════════════════════════════════════════

ENUNCIADO:
----------
Una red social necesita analizar las conexiones entre usuarios.
Cada usuario tiene un conjunto de amigos. El sistema debe:

1. Encontrar amigos en común entre dos usuarios
2. Sugerir amigos (amigos de amigos que no conoces)
3. Encontrar grupos aislados (usuarios sin amigos en común)
4. Calcular el "grado de conexión" entre usuarios
5. Encontrar el usuario más conectado

Implementar usando operaciones de conjuntos.

Entender el "Salto": En el punto 2,
la clave es que entras al conjunto de un amigo (red[amigo]) para sacar información.
Eso es navegar un grafo usando diccionarios.

Diferencia entre & y isdisjoint:
    A & B te dice quiénes son los amigos comunes.
    A.isdisjoint(B) solo te dice si hay o no (es más rápido si solo necesitas un Sí/No).

Grado de conexión: Si te piden este cálculo, recuerda siempre la división:
Intersección / Unión. Es la respuesta técnica que esperan los profesores.
"""

# ═══════════════════════════════════════════════════════════════════════════════
# DATOS
# ═══════════════════════════════════════════════════════════════════════════════
# Es un diccionario donde la llave es una PERSONA y el valor es el CONJUNTO de sus amigos.
red = {
    "Ana": {"Carlos", "Diana", "Eduardo", "Fernanda"},
    "Carlos": {"Ana", "Diana", "Gabriel"},
    "Diana": {"Ana", "Carlos", "Eduardo", "Helena"},
    "Eduardo": {"Ana", "Diana", "Fernanda"},
    "Fernanda": {"Ana", "Eduardo", "Gabriel", "Helena"},
    "Gabriel": {"Carlos", "Fernanda", "Ivan"},
    "Helena": {"Diana", "Fernanda", "Ivan"},
    "Ivan": {"Gabriel", "Helena"},
}

# ═══════════════════════════════════════════════════════════════════════════════
# SOLUCIÓN
# ═══════════════════════════════════════════════════════════════════════════════

print("=" * 60)
print("   RED SOCIAL - ANÁLISIS DE CONEXIONES")
print("=" * 60)

print("\nConexiones:")
for usuario, amigos in red.items():
    print(f"  {usuario} ({len(amigos)} amigos): {sorted(amigos)}")


# 1. AMIGOS EN COMÚN (Intersección &)
# Igual que en Spotify, usamos '&' para ver quiénes están en ambos círculos sociales.
# Uso: Mostrar "X amigos en común" en el perfil de alguien.
print("\n" + "=" * 60)
print("1. AMIGOS EN COMÚN")
print("=" * 60)

pares = [("Ana", "Carlos"), ("Ana", "Gabriel"), ("Diana", "Fernanda")]
for u1, u2 in pares:
    comunes = red[u1] & red[u2]
    print(f"  {u1} y {u2}: {sorted(comunes) if comunes else 'ninguno'}")


# 2. Sugerir amigos (amigos de amigos que no conoces)
# Este es el algoritmo "Personas que quizá conozcas".
print("\n" + "=" * 60)
print("2. SUGERENCIAS DE AMISTAD")
print("=" * 60)

for usuario in sorted(red.keys()):
    amigos_de_amigos = set()
    # PASO A: Unión Acumulativa (|)
    # Recorremos a tus amigos y sumamos a TODOS sus amigos en una sola bolsa.
    for amigo in red[usuario]:
        amigos_de_amigos = amigos_de_amigos | red[amigo]
    

    # Quitar al usuario mismo y sus amigos actuales
    # PASO B: Limpieza (Resta -)
    # 1. Quitamos a tus amigos actuales (porque ya los conoces).
    # 2. Te quitamos a ti mismo (porque no puedes ser tu propio amigo sugerido).
    sugerencias = amigos_de_amigos - red[usuario] - {usuario}
    
    if sugerencias:
        print(f"  {usuario} → Sugerencias: {sorted(sugerencias)}")


# 3. Usuarios sin amigos en común (disjuntos)
# El método 'isdisjoint' devuelve True si la intersección es VACÍA.
# Uso: Encontrar personas que viven en "burbujas" sociales totalmente separadas.
print("\n" + "=" * 60)
print("3. USUARIOS SIN AMIGOS EN COMÚN")
print("=" * 60)

usuarios = list(red.keys())
for i in range(len(usuarios)):
    for j in range(i + 1, len(usuarios)):
        u1, u2 = usuarios[i], usuarios[j]
        if red[u1].isdisjoint(red[u2]):
            print(f"  {u1} y {u2} no tienen amigos en común")


# 4. GRADO DE CONEXIÓN (Índice de Jaccard)(amigos en común / total amigos)
# Es el mismo concepto de Netflix, pero aplicado a personas.
# Mide qué tan parecidos son los círculos sociales de dos personas.
# Fórmula: (Amigos en común) / (Unión de todos los amigos de ambos)
print("\n" + "=" * 60)
print("4. GRADO DE CONEXIÓN")
print("=" * 60)

u1, u2 = "Ana", "Diana"
comunes = red[u1] & red[u2]
total = red[u1] | red[u2]
grado = len(comunes) / len(total) if total else 0
print(f"  {u1} y {u2}:")
print(f"    Amigos en común: {sorted(comunes)}")
print(f"    Total amigos: {sorted(total)}")
print(f"    Grado de conexión: {grado:.2%}")


# 5. USUARIO MÁS CONECTADO (Cardinalidad len)
# Simplemente medimos el tamaño (len) de cada conjunto.
# El que tenga el número más alto es el "influencer" o el "hub" de la red.
print("\n" + "=" * 60)
print("5. USUARIO MÁS CONECTADO")
print("=" * 60)

ranking = []
for usuario, amigos in red.items():
    ranking.append((usuario, len(amigos)))

ranking.sort(key=lambda x: x[1], reverse=True)

for i, (usuario, num_amigos) in enumerate(ranking, 1):
    barra = "█" * num_amigos
    print(f"  {i}. {usuario:10} {barra} ({num_amigos} amigos)")