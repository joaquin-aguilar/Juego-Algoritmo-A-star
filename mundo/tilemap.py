from principal.configuraciones import *
from mundo.terreno import *


class TileMap:

    def __init__(self, terreno, grafo):
        self.terreno = terreno
        self.grafo = grafo

    def es_caminable(self, x, y):

        if (x < 0 or y < 0 or x >= ANCHO or y >= ALTO):
            return False
        return (self.terreno[y][x] != PARED)