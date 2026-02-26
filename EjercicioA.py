class Pagina:
    def __init__(self, url, titulo, tiempo):
        self.url = url
        self.titulo = titulo
        self.tiempo = tiempo
        self.siguiente = None

    def tiempo_formato(self):
        minutos = self.tiempo // 60
        segundos = self.tiempo % 60
        return f"{minutos}:{segundos:02d}"

class Historial:
    def __init__(self):
        self.cabeza = None

    def esta_vacia(self):
        return self.cabeza is None

    #2: Agregar al inicio O(1)
    def agregar_pagina(self, url, titulo, tiempo):
        nueva = Pagina(url, titulo, tiempo)
        nueva.siguiente = self.cabeza
        self.cabeza = nueva

    #3: Tiempo Total - RECURSIVO
    def tiempo_total(self, nodo="inicio"):
        if nodo == "inicio":
            nodo = self.cabeza        
        if nodo is None: #Caso base
            return 0        
        return nodo.tiempo + self.tiempo_total(nodo.siguiente)

    #4: Buscar por dominio - RECURSIVO
    def buscar_por_dominio(self, texto):
        nueva_lista = Historial()
        self.buscar_recursivo(self.cabeza, texto, nueva_lista)
        return nueva_lista

    def buscar_recursivo(self, nodo, texto, nueva_lista):
        if nodo is None: #Caso base
            return
        
        if texto.lower() in nodo.url.lower():
            #Agregamos a la nueva lista
            nueva_lista.agregar_pagina(nodo.url, nodo.titulo, nodo.tiempo)
        
        self.buscar_recursivo(nodo.siguiente, texto, nueva_lista)

    #5: Eliminar páginas rápidas - RECURSIVO
    def eliminar_rapidas(self, limite_tiempo, nodo="inicio"):
        if nodo == "inicio":
            self.cabeza = self.eliminar_rapidas(limite_tiempo, self.cabeza)
            return
        if nodo is None: #Caso base
            return None

        #Llamada recursiva: primero resolvemos el resto de la lista
        nodo.siguiente = self.eliminar_rapidas(limite_tiempo, nodo.siguiente)

        # Si el nodo actual es "rápido", lo saltamos (eliminamos)
        if nodo.tiempo < limite_tiempo:
            return nodo.siguiente        
        return nodo

    #Método extra para mostrar los resultados
    def mostrar_historial(self):
        if self.esta_vacia():
            print("El historial está vacío.")
            return
        temp = self.cabeza
        while temp:
            print(f"[{temp.tiempo_formato()}] {temp.titulo} - {temp.url}")
            temp = temp.siguiente

"""
EXAMEN A Sistema de Historial de Navegador Web
CONTEXTO:

Google Chrome te ha contratado para implementar el historial de navegación.
Debes diseñar e implementar el sistema usando listas enlazadas.

INSTRUCCIONES:
1. Diseñar la clase Nodo (Pagina) con los atributos necesarios
2. Diseñar la clase Lista (Historial) con los métodos requeridos
3. Usar RECURSIVIDAD en los métodos donde se indique
4. No usar listas de Python [], solo tu estructura de nodos
5. Tiempo: 90 minutos

REQUERIMIENTOS DEL SISTEMA

PUNTO 1 (1.0): DISEÑO DE ESTRUCTURAS
-------------------------------------
Diseña las clases necesarias:

a) Clase NODO (Pagina):
   - Debe almacenar: URL, título de la página, tiempo en segundos
   - Debe poder enlazarse con otra página
   
b) Clase LISTA (Historial):
   - Debe mantener referencia al inicio de la lista
   - Las páginas más recientes van al INICIO


PUNTO 2 (0.75): AGREGAR PÁGINA
------------------------------
Implementa un método para agregar una nueva página visitada.
- La página más reciente debe quedar al INICIO de la lista
- Complejidad esperada: O(1)


PUNTO 3 (1.0): TIEMPO TOTAL - RECURSIVO
---------------------------------------
Implementa un método que calcule el tiempo total de navegación.
- OBLIGATORIO usar recursividad
- Retorna la suma de segundos de todas las páginas

Ejemplo:
    Si hay páginas con tiempos [30, 120, 45] segundos
    Debe retornar 195


PUNTO 4 (1.0): BUSCAR POR DOMINIO - RECURSIVO
---------------------------------------------
Implementa un método que retorne una NUEVA lista con páginas
que contengan cierto texto en su URL.
- OBLIGATORIO usar recursividad
- No modificar la lista original

Ejemplo:
    buscar_por_dominio("youtube") 
    Retorna nueva lista con páginas cuya URL contiene "youtube"


PUNTO 5 (1.25): ELIMINAR PÁGINAS RÁPIDAS - RECURSIVO
----------------------------------------------------
Implementa un método que elimine páginas donde el usuario
estuvo menos de X segundos (probablemente clicks accidentales).
- OBLIGATORIO usar recursividad
- Modificar la lista original

Ejemplo:
    eliminar_rapidas(10)
    Elimina todas las páginas con tiempo < 10 segundos

═══════════════════════════════════════════════════════════════════════════════
ESCRIBE TU CÓDIGO AQUÍ ABAJO
═══════════════════════════════════════════════════════════════════════════════
"""

# --- MENÚ DE PRUEBA ---
def menu():
    print("\n" + "="*35)
    print("      HISTORIAL GOOGLE CHROME")
    print("="*35)
    print("1. Visitar nueva página")
    print("2. Ver historial completo")
    print("3. Ver tiempo total de navegación")
    print("4. Buscar por dominio (Youtube, etc)")
    print("5. Limpiar clicks accidentales (Eliminar rápidas)")
    print("6. Salir")
    print("="*35)

mi_historial = Historial()

while True:
    menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        u = input("URL: ")
        t = input("Título: ")
        s = int(input("Segundos de permanencia: "))
        mi_historial.agregar_pagina(u, t, s)
        print("Página registrada.")

    elif opcion == "2":
        print("\n--- HISTORIAL RECIENTE ---")
        mi_historial.mostrar_historial()

    elif opcion == "3":
        total = mi_historial.tiempo_total()
        print(f"\nTiempo total en el navegador: {total} segundos.")

    elif opcion == "4":
        dom = input("Texto a buscar en URL: ")
        resultados = mi_historial.buscar_dominio(dom) if hasattr(mi_historial, 'buscar_dominio') else mi_historial.buscar_por_dominio(dom)
        print("\n--- RESULTADOS DE BÚSQUEDA ---")
        resultados.mostrar_historial()

    elif opcion == "5":
        seg = int(input("Eliminar páginas con menos de cuántos segundos?: "))
        mi_historial.eliminar_rapidas(seg)
        print(f"Limpieza completada (Páginas < {seg}s eliminadas).")

    elif opcion == "6":
        print("Cerrando navegador...")
        break
# PUNTO 1a: Clase Nodo (Pagina)
# TODO: Diseñar e implementar


# PUNTO 1b: Clase Lista (Historial)
# TODO: Diseñar e implementar con los métodos de los puntos 2-5


# ═══════════════════════════════════════════════════════════════════════════════
# CÓDIGO DE PRUEBA - NO MODIFICAR
# (Descomenta cuando tengas tu implementación lista)
# ═══════════════════════════════════════════════════════════════════════════════

"""
if __name__ == "__main__":
    print("=" * 60)
    print("         PRUEBAS DEL HISTORIAL DE NAVEGACIÓN")
    print("=" * 60)
    
    # Crear historial
    historial = Historial()
    
    # Agregar páginas (la más reciente queda primero)
    historial.visitar("https://www.google.com/search", "Búsqueda Google", 15)
    historial.visitar("https://www.youtube.com/watch", "Video YouTube", 300)
    historial.visitar("https://www.github.com/repo", "GitHub Repo", 180)
    historial.visitar("https://www.youtube.com/home", "YouTube Home", 45)
    historial.visitar("https://www.google.com/maps", "Google Maps", 5)
    
    print("\\n📋 Historial inicial:")
    historial.mostrar()  # Implementa este método para visualizar
    
    # Prueba tiempo total
    print("\\n⏱️ Tiempo total:", historial.tiempo_total(), "segundos")
    print("   Esperado: 545 segundos")
    
    # Prueba buscar por dominio
    print("\\n🔍 Páginas de YouTube:")
    youtube = historial.buscar_por_dominio("youtube")
    youtube.mostrar()
    
    # Prueba eliminar rápidas
    print("\\n🗑️ Eliminando páginas < 30 segundos...")
    historial.eliminar_rapidas(30)
    historial.mostrar()
    print("   (Google Maps y Búsqueda Google deberían estar eliminadas)")
"""
