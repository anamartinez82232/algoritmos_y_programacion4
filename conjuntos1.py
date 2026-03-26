# 1. EL CATÁLOGO: Diccionario donde la CLAVE es la película (str) 
# y el VALOR es un CONJUNTO (set) de sus géneros.
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

# 2. ENCONTRAR PAREJAS SIMILARES (Comparación cruzada)
peliculas_con_generos_en_comun = [] 
peliculas = list(catalogo.keys()) # Sacamos los nombres a una lista para usar índices [i]
for i in range(len(peliculas)):
    # El j = i + 1 evita comparar una película consigo misma 
    # y evita comparar A vs B y luego B vs A (duplicados).
    for j in range(i + 1, len(peliculas)):
        p1, p2 = peliculas[i], peliculas[j]
        comunes = catalogo[p1] & catalogo[p2] # INTERSECCIÓN (&): Géneros que están en AMBAS películas.

        # FILTRO: Solo guardamos si comparten 2 o más géneros.
        if len(comunes) >= 2:
            # Guardamos una tupla con los nombres y los géneros comunes ordenados.
            peliculas_con_generos_en_comun.append((p1, p2, sorted(comunes)))

print(peliculas_con_generos_en_comun)

# 3. SISTEMA DE RECOMENDACIÓN PERSONALIZADO
favoritos = {"acción", "crimen", "aventura"} # Lo que le gusta al usuario
recomendaciones = []

for pelicula, generos in catalogo.items():
    # INTERSECCIÓN: ¿Qué géneros de esta película le gustan al usuario?
    generos_comunes = favoritos.intersection(generos)
    
    if generos_comunes:
        # CÁLCULO: (Cuántos le gustaron / Total de favoritos del usuario) * 100
        porcentaje_similitud = (len(generos_comunes) / len(favoritos)) * 100
        recomendaciones.append((pelicula, porcentaje_similitud))

# FUNCIÓN DE AYUDA: Le dice al sort que use el número (índice 1) para ordenar.
def obtener_porcentaje(elemento):
    return elemento[1]

# ORDENAR: reverse=True para que las de mayor porcentaje salgan de primero.
recomendaciones.sort(key=obtener_porcentaje, reverse=True)

# 4. EXTRACCIÓN DE CATEGORÍAS (Géneros únicos)
generos_unicos = set() # Empezamos con un conjunto vacío
for generos in catalogo.values():
    # UNIÓN: Vamos sumando los géneros de cada película sin repetir ninguno.
    generos_unicos = generos_unicos.union(generos)

# sorted() convierte el conjunto en una lista ordenada alfabéticamente.
generos_ordenados = sorted(generos_unicos)

# 5. ÍNDICE INVERTIDO (Agrupar películas por género)
peliculas_por_genero = {}

for pelicula, generos in catalogo.items():
    for genero in generos:
        # Si el género no está en el nuevo diccionario, lo creamos con un set vacío.
        if genero not in peliculas_por_genero:
            peliculas_por_genero[genero] = set()
        # Añadimos la película a la "bolsa" de ese género.
        peliculas_por_genero[genero].add(pelicula)

# 6. ÍNDICE DE JACCARD (Fórmula matemática de similitud)
def calcular_indice(p1, p2):
    g1 = catalogo[p1]
    g2 = catalogo[p2]

    interseccion = len(g1 & g2) # Comunes
    union = len(g1 | g2)        # Total de géneros diferentes entre las dos

    # Resultado entre 0.0 (nada igual) y 1.0 (idénticas)
    return interseccion / union 

# 7. DETECTOR DE PLAGIO (Análisis de texto)
STOPWORDS = {"el", "la", "de", "que", "y", "en", "a", "es", "son", "su"} # Palabras "vacías"

def limpiar_texto(texto):
    # .split() rompe el texto en palabras.
    # set() las hace únicas.
    # - STOPWORDS quita las palabras que no aportan significado.
    return set(texto.lower().split()) - STOPWORDS

def detectar_copia(texto1, texto2):
    palabras1 = limpiar_texto(texto1)
    palabras2 = limpiar_texto(texto2)

    # Aplicamos Jaccard sobre las palabras filtradas
    interseccion = palabras1.intersection(palabras2)
    union = palabras1.union(palabras2)

    if not union: return 0.0
    indice = len(interseccion) / len(union)

    # UMBRAL: Si comparten más del 60%, se considera copia.
    if indice > 0.6:
        print(f"Se copiaron. Indice : {indice:.2f}")
    else:
        print(f"No se copiaron. Indice : {indice:.2f}")
    return indice