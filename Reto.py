"""
RETO: Sistema de Matchmaking para Videojuego Online

Contexto:

Estás desarrollando el sistema de emparejamiento para un juego competitivo online.
Los jugadores tienen un nivel de habilidad que va de 0 a 3000.
Cuando un jugador quiere jugar, entra a una cola de espera
y el sistema debe emparejarlo con otro jugador de nivel similar.

Requisitos:

Los jugadores entran a la cola con su ID y nivel 
El sistema debe emparejar jugadores cuya diferencia de nivel sea máximo 150 puntos
Si hay varios candidatos válidos, priorizar al que lleva más tiempo esperando 
Si no hay pareja disponible, el jugador permanece en la cola
"""


class Jugador:
    def __init__(self, id, nivel):
        self.id = id
        self.nivel = nivel
        self.llegada = datetime.now() #Para priorizar al que más espera
        self.siguiente = None

class ColaMatchmaking:
    def __init__(self):
        self.frente = None
        self.final = None

    def encolar(self, id, nivel):
        nuevo = Jugador(id, nivel)
        if self.final is None:
            self.frente = self.final = nuevo
        else:
            self.final.siguiente = nuevo
            self.final = nuevo
        print(f"Jugador {id} (Nivel {nivel}) entró a la cola.")

    def buscar_pareja(self, jugador_nuevo):
        actual = self.frente
        anterior = None

        while actual:
            if abs(actual.nivel - jugador_nuevo.nivel) <= 150:
                if anterior is None:
                    self.frente = actual.siguiente 
                    if self.frente is None:
                        self.final = None
                else:
                    anterior.siguiente = actual.siguiente #Si estaba en la mitad
                    if actual == self.final:
                        self.final = anterior
                
                return actual
            
            anterior = actual
            actual = actual.siguiente
        
        return None

    def realizar_match(self, id, nivel):
        nuevo_jugador = Jugador(id, nivel)
        pareja = self.buscar_pareja(nuevo_jugador)
        
        if pareja:
            print(f"Partida encontrada")
            print(f"[{nuevo_jugador.id} vs {pareja.id}]")
            print(f"Diferencia de nivel: {abs(nuevo_jugador.nivel - pareja.nivel)}")
        else:
            self.encolar(id, nivel)