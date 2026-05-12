import pygame

from principal.configuraciones import *
from principal.colores import *

class TileSet:

    def __init__(self):

        self.camino_sencillo = pygame.Surface((ESPACIO_RELATIVO, ESPACIO_RELATIVO))
        self.camino_sencillo.fill(VERDE)
        self.camino_dificil = pygame.Surface((ESPACIO_RELATIVO, ESPACIO_RELATIVO))
        self.camino_dificil.fill(AMARILLO)
        self.paredes = pygame.Surface((ESPACIO_RELATIVO, ESPACIO_RELATIVO))
        self.paredes.fill((20, 20, 20))
