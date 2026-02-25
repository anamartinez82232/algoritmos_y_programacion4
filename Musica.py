class Cancion:
    def __init__(self, titulo, artista, duracion_segundos):
        self.titulo = titulo
        self.artista = artista
        self.duracion_segundos = duracion_segundos
        self.siguiente = None
        self.anterior = None

    def duracion_formato(self):
        #Convierte segundos a MM:SS
        minutos = self.duracion_segundos // 60
        segundos = self.duracion_segundos % 60
        return f"{minutos}:{segundos:02d}"

class Playlist:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.actual = None

    def esta_vacia(self):
        return self.cabeza is None

    def agregar_cancion(self, titulo, artista, duracion_segundos):
        nueva = Cancion(titulo, artista, duracion_segundos)
        if self.esta_vacia():
            self.cabeza = nueva
            self.cola = nueva
            self.actual = nueva
        else:
            self.cola.siguiente = nueva
            nueva.anterior = self.cola
            self.cola = nueva
        
        # Mantenemos la conexión circular
        self.cola.siguiente = self.cabeza
        self.cabeza.anterior = self.cola
        print(f"Canción '{titulo}' agregada.")

    def mostrar_lista(self):
        #Muestra toda la lista marcando la actual
        if self.esta_vacia():
            print("La playlist está vacía.")
            return

        print("\n--- Mi Playlist ---")
        temp = self.cabeza
        total = self.__len__()
        vistas = 0
        
        while vistas < total:
            # Si el nodo que estamos visitando es el 'actual', le ponemos la marca
            marca = "<-- Reproduciendo" if temp == self.actual else ""
            print(f"{vistas + 1}. {temp.titulo} - {temp.artista} ({temp.duracion_formato()}) {marca}")
            temp = temp.siguiente
            vistas += 1

    def siguiente_cancion(self):
        if not self.esta_vacia():
            self.actual = self.actual.siguiente
            self.mostrar_actual()
        else:
            print("No hay canciones.")

    def anterior_cancion(self):
        if not self.esta_vacia():
            self.actual = self.actual.anterior
            self.mostrar_actual()
        else:
            print("No hay canciones.")

    def buscar_cancion(self, titulo):
        if self.esta_vacia():
            return None
        temp = self.cabeza
        vistas = 0
        total = self.__len__()
        while vistas < total:
            if temp.titulo.lower() == titulo.lower(): #.lower() sirve a que no importe mayúsculas
                return temp
            temp = temp.siguiente
            vistas += 1
        return None

    def eliminar_cancion(self, titulo):
        if self.esta_vacia():
            print("Nada que eliminar.")
            return False

        objetivo = self.buscar_cancion(titulo)
        if not objetivo:
            print("Canción no encontrada.")
            return False

        if self.cabeza == self.cola: #Si solo hay un dato
            self.cabeza = None
            self.cola = None
            self.actual = None
        else:
            #Desconectar el nodo
            objetivo.anterior.siguiente = objetivo.siguiente
            objetivo.siguiente.anterior = objetivo.anterior
            
            # Si era la cabeza o cola, mover los punteros principales
            if objetivo == self.cabeza:
                self.cabeza = objetivo.siguiente
            if objetivo == self.cola:
                self.cola = objetivo.anterior
            # Si era la que estábamos escuchando, pasar a la siguiente
            if objetivo == self.actual:
                self.actual = objetivo.siguiente

        print(f"'{titulo}' eliminada de la playlist.")
        return True

    def __len__(self):
        if self.esta_vacia(): 
            return 0
        contador = 1
        temp = self.cabeza
        while temp != self.cola:
            contador += 1
            temp = temp.siguiente
        return contador

    def mostrar_actual(self):
        if self.actual:
            print(f"\n>>> Escuchando ahora: {self.actual.titulo} ({self.actual.duracion_formato()})")
        else:
            print("Playlist vacía.")

def menu():
    print("\n" + "="*30)
    print("      REPRODUCTOR CIRCULAR")
    print("="*30)
    print("1. Agregar canción")
    print("2. Mostrar playlist completa")
    print("3. Reproducir actual")
    print("4. Siguiente canción >>")
    print("5. << Canción anterior")
    print("6. Eliminar canción")
    print("7. Buscar canción")
    print("8. Salir")
    print("="*30)

#Ejecución del programa

mi_playlist = Playlist()

while True:
    menu()
    opcion = input("Elige una opción: ")

    if opcion == "1":
        titulo = input("Nombre de la canción: ")
        artista = input("Nombre del artista: ")
        duracion = int(input("Duración en segundos: "))
        mi_playlist.agregar_cancion(titulo, artista, duracion)

    elif opcion == "2":
        mi_playlist.mostrar_lista()

    elif opcion == "3":
        mi_playlist.mostrar_actual()

    elif opcion == "4":
        mi_playlist.siguiente_cancion()

    elif opcion == "5":
        mi_playlist.anterior_cancion()

    elif opcion == "6":
        titulo = input("Canción que deseas eliminar: ")
        mi_playlist.eliminar_cancion(titulo)

    elif opcion == "7":
        titulo = input("Canción que deseas buscar: ")
        resultado = mi_playlist.buscar_cancion(titulo)
        if resultado:
            print(f"¡Encontrada! {resultado.titulo} de {resultado.artista} ({resultado.duracion_formato()})")
        else:
            print("Esa canción no está en la lista.")

    elif opcion == "8":
        print("Cerrando reproductor ¡Adiós!")
        break

    else:
        print("Opción no válida, intenta de nuevo.")