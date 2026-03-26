"""
═══════════════════════════════════════════════════════════════════════════════
CASO DE USO 3: NETFLIX - SISTEMA DE RECOMENDACIONES
Algoritmos y Programación 4 - Semana 6
═══════════════════════════════════════════════════════════════════════════════

ENUNCIADO:
----------
Netflix quiere mejorar su sistema de recomendaciones usando conjuntos.
Cada película tiene un conjunto de géneros/etiquetas.
El sistema debe:

1. Encontrar películas similares (comparten géneros)
2. Recomendar películas según los géneros favoritos del usuario
3. Encontrar géneros únicos en el catálogo
4. Agrupar películas por género
5. Calcular un "puntaje de similitud" entre películas

Implementar usando operaciones de conjuntos.

Puntaje de Recomendación vs. Jaccard:
    El Puntaje (Punto 2) compara una película contra una lista de "deseos" (favoritos).
    Jaccard (Punto 5) compara dos películas entre sí para ver qué tan "gemelas" son.

¿Por qué usar union para los géneros únicos?
    Porque si usas una lista, tendrías "drama" repetido 50 veces.
    El conjunto (set) con la operación | garantiza que solo tengas una
    etiqueta por cada categoría existente.

El Umbral (Threshold):
    En el punto 1 se usa len(...) >= 2.
    Si el profesor te pide "hacer el filtro más estricto", simplemente subes ese número.
"""

# ═══════════════════════════════════════════════════════════════════════════════
# DATOS
# ═══════════════════════════════════════════════════════════════════════════════
# Un diccionario donde cada llave es una película y su valor es un conjunto de etiquetas.
catalogo = {
    "Inception": {"ciencia ficción", "acción", "thriller", "drama"},
    "The Matrix": {"ciencia ficción", "acción", "thriller"},
    "Titanic": {"romance", "drama", "histórica"},
    "The Notebook": {"romance", "drama"},
    "Avengers": {"acción", "ciencia ficción", "aventura"},
    "John Wick": {"acción", "thriller", "crimen"},
    "Interstellar": {"ciencia ficción", "drama", "aventura"},
    "The Godfather": {"crimen", "drama", "thriller"},
    "Toy Story": {"animación", "comedia", "aventura"},
    "Shrek": {"animación", "comedia", "aventura"},
}

# Géneros favoritos del usuario
favoritos_usuario = {"ciencia ficción", "acción", "thriller"}

# ═══════════════════════════════════════════════════════════════════════════════
# SOLUCIÓN
# ═══════════════════════════════════════════════════════════════════════════════

print("=" * 60)
print("   NETFLIX - SISTEMA DE RECOMENDACIONES")
print("=" * 60)

print("\nCatálogo:")
for pelicula, generos in catalogo.items():
    print(f"  {pelicula}: {generos}")


# 1. COMPARACIÓN PAREJA A PAREJA (Filtro por cantidad)
# Usamos un bucle anidado (i y j) para comparar cada película con todas las demás.
# La condición 'len(comunes) >= 2' es un umbral: 
# "Si no comparten al menos 2 géneros, no las consideres similares".
print("\n" + "=" * 60)
print("1. PELÍCULAS SIMILARES (comparten 2+ géneros)")
print("=" * 60)

peliculas = list(catalogo.keys())
for i in range(len(peliculas)):
    for j in range(i + 1, len(peliculas)):
        p1, p2 = peliculas[i], peliculas[j]
        comunes = catalogo[p1] & catalogo[p2] # Intersección
        if len(comunes) >= 2:
            print(f"  {p1} <-> {p2}")
            print(f"    Géneros comunes: {comunes}")


# 2. RECOMENDACIÓN POR PORCENTAJE
# No solo buscamos coincidencias, sino que calculamos qué tan cerca está la película 
# de los gustos totales del usuario.
# puntaje = (coincidencias / total_favoritos)
# Ejemplo: Si coinciden 2 de 3 géneros favoritos, el puntaje es 0.66 (66%).
print("\n" + "=" * 60)
print(f"2. RECOMENDACIONES (gustos: {favoritos_usuario})")
print("=" * 60)

recomendaciones = []
for pelicula, generos in catalogo.items():
    coincidencias = generos & favoritos_usuario
    if coincidencias:
        puntaje = len(coincidencias) / len(favoritos_usuario)
        recomendaciones.append((pelicula, puntaje, coincidencias))

# Ordenar por puntaje (mayor primero)
recomendaciones.sort(key=lambda x: x[1], reverse=True)

for pelicula, puntaje, coincidencias in recomendaciones:
    barra = "█" * int(puntaje * 10)
    print(f"  {pelicula:20} {barra} {puntaje:.0%} - {coincidencias}")


# 3. EXTRACCIÓN GLOBAL (Unión Acumulativa)
# 'todos_generos' empieza vacío. Con cada vuelta del ciclo, le unimos (|) 
# los géneros de la película actual. Al ser un conjunto, los repetidos se borran solos.
print("\n" + "=" * 60)
print("3. GÉNEROS ÚNICOS EN EL CATÁLOGO")
print("=" * 60)

todos_generos = set()
for generos in catalogo.values():
    todos_generos = todos_generos | generos

print(f"  Total: {len(todos_generos)} géneros")
for g in sorted(todos_generos):
    print(f"  • {g}")


# 4. AGRUPAMIENTO (Índice Invertido)
# Para cada género existente, revisamos todo el catálogo.
# Si el género 'está en' (in) los géneros de la película, la agregamos al grupo.
# Uso: Crear las secciones "Terror", "Comedia", etc., en la interfaz.
print("\n" + "=" * 60)
print("4. PELÍCULAS POR GÉNERO")
print("=" * 60)

for genero in sorted(todos_generos):
    peliculas_genero = set()
    for pelicula, generos in catalogo.items():
        if genero in generos:
            peliculas_genero.add(pelicula)
    print(f"  {genero}: {peliculas_genero}")


# 5. ÍNDICE DE JACCARD (La fórmula profesional)
# Es la forma más precisa de comparar dos conjuntos.
# Se define como: (Lo que comparten) / (El total de elementos únicos entre ambas).
# Evita el sesgo de películas que tienen muchísimas etiquetas.
print("\n" + "=" * 60)
print("5. SIMILITUD (índice de Jaccard)")
print("=" * 60)

def similitud_jaccard(pelicula1, pelicula2):
    """
    Índice de Jaccard = |A ∩ B| / |A ∪ B|
    1.0 = idénticos, 0.0 = nada en común
    """
    g1 = catalogo[pelicula1]
    g2 = catalogo[pelicula2]
    interseccion = len(g1 & g2)
    union = len(g1 | g2)
    return interseccion / union if union > 0 else 0 # Resultado siempre entre 0 y 1.


# 1. DEFINICIÓN DE PRUEBAS:
# Creamos una lista de tuplas con las películas que queremos comparar. 
# Esto sirve para verificar si nuestro algoritmo de Jaccard funciona con 
# casos lógicos (ej: Inception vs Matrix deberían ser muy parecidas).
pares = [
    ("Inception", "The Matrix"),
    ("Inception", "Titanic"),
    ("Toy Story", "Shrek"),
    ("The Godfather", "John Wick"),
]


# 2. CICLO DE PROCESAMIENTO:
# 'p1' tomará el primer nombre de la tupla y 'p2' el segundo.
for p1, p2 in pares:
    # Llama a la función que creaste antes. 
    # 'sim' será un número entre 0.0 y 1.0 (ej: 0.75).
    sim = similitud_jaccard(p1, p2)

    # 3. CREACIÓN DE LA BARRA VISUAL:
    # Multiplicamos el índice (0.0 a 1.0) por 20 para saber cuántos 
    # cuadritos pintar. 
    # Si sim es 0.5, pintará 10 cuadritos (0.5 * 20 = 10).
    barra = "█" * int(sim * 20)

    # 4. IMPRESIÓN FORMATEADA:
    # {p1:15} reserva 15 espacios para el texto (alineación).
    # {sim:.2f} muestra el número con solo 2 decimales.
    print(f"  {p1:15} vs {p2:15} → {barra} {sim:.2f}")