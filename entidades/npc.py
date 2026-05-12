from entidades.entidad import Entidad
from principal.configuraciones import *
from ia.comportamiento_persecucion import ComportamientoPersecucion

class NPC(Entidad):

    def __init__(self, x, y, sprite):
        super().__init__(x, y, sprite)
        self.behavior = ComportamientoPersecucion()
        self.timer_movimiento = 0
        self.timer_ruta = 0

    def update(self, dt, player, tilemap):
        self.timer_ruta += dt
        self.timer_movimiento += dt

        if self.timer_ruta >= RETRAZO_CAMBIO_RUTA_NPC:
            self.timer_ruta = 0
            self.behavior.update(self, player, tilemap)

        if self.ruta and self.timer_movimiento >= RETRAZO_MOVIMIENTO_NPC:
            self.timer_movimiento = 0
            self.x, self.y = self.ruta.pop(0)