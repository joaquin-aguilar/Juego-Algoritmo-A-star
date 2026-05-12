from entidades.entidad import Entidad
from principal.configuraciones import *

class Jugador(Entidad):

    def __init__(self, x, y, sprite):
        super().__init__(x, y, sprite)

    def actualizar(self, dt):
        self.velocidad_movimiento += dt
        if (self.ruta and self.velocidad_movimiento >= RETRAZO_MOVIMIENTO_JUGADOR):
            self.velocidad_movimiento = 0
            self.x, self.y = self.ruta.pop(0)