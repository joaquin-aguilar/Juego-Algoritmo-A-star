import pygame

from principal.configuraciones import *
from graficos.sprites import SpriteSheet


class TileSet:

    def __init__(self):

        terreno = SpriteSheet("recursos/Tilemap.png")
        arbustos =  SpriteSheet("recursos/Bushes.png")
        agua = SpriteSheet("recursos/Water.png")

        self.camino_sencillo = terreno.obtener_sprite(64, 64, 64, 64, ESPACIO_RELATIVO, ESPACIO_RELATIVO)
        self.camino_dificil = arbustos.obtener_sprite(0, 0, 128, 128, ESPACIO_RELATIVO, ESPACIO_RELATIVO, recortar_transparencia=True)
        self.paredes = agua.obtener_sprite(0, 0, 64, 64, ESPACIO_RELATIVO, ESPACIO_RELATIVO)
        self.piso = terreno.obtener_sprite(322, 322, 64, 64, ESPACIO_RELATIVO, ESPACIO_RELATIVO)