import pygame

from principal.configuraciones import *
from graficos.sprites import SpriteSheet


class TileSet:

    def __init__(self):

        terreno = SpriteSheet("recursos/Tilemap.png")
        arbustos =  SpriteSheet("recursos/Bushes.png")
        agua = SpriteSheet("recursos/Water.png")
        jugador = SpriteSheet("recursos/Archer.png")
        enemigo = SpriteSheet("recursos/Warrior.png")

        self.camino_sencillo = terreno.obtener_sprite(64, 64, 64, 64, ESPACIO_RELATIVO, ESPACIO_RELATIVO)
        self.camino_dificil = arbustos.obtener_sprite(0, 0, 128, 128, ESPACIO_RELATIVO, ESPACIO_RELATIVO, recortar_transparencia=True)
        self.piso = terreno.obtener_sprite(322, 322, 64, 64, ESPACIO_RELATIVO, ESPACIO_RELATIVO)
        self.paredes = agua.obtener_sprite(0, 0, 64, 64, ESPACIO_RELATIVO, ESPACIO_RELATIVO)
        self.jugador = jugador.obtener_sprite(0, 0, 192, 192, ESPACIO_RELATIVO, ESPACIO_RELATIVO, recortar_transparencia=True)
        self.enemigo = enemigo.obtener_sprite(0, 0, 192, 192, ESPACIO_RELATIVO, ESPACIO_RELATIVO, recortar_transparencia=True)