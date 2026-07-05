import pygame
from principal.configuraciones import *
from principal.colores import *
from mundo.terreno import *

class Renderizador:

    def __init__(self, pantalla, tileset):

        self.pantalla = pantalla
        self.tileset = tileset

        self.surface = pygame.Surface((ANCHO_BASE, ALTO_BASE))
        self.fondo = pygame.Surface(self.surface.get_size())

    def generar_fondo(self, tilemap):

        self.fondo.fill((0, 0, 0))

        for y in range(ALTO):

            for x in range(ANCHO):

                tile = tilemap.terreno[y][x]
                pos = (x * ESPACIO_RELATIVO, y * ESPACIO_RELATIVO)

                if tile == TERRENO_LIGERO:
                    self.fondo.blit(self.tileset.camino_sencillo, pos)
                elif tile == TERRENO_COSTOSO:
                        self.fondo.blit(self.tileset.camino_sencillo, pos)
                        self.fondo.blit(self.tileset.camino_dificil, pos)
                else:
                    self.fondo.blit(self.tileset.paredes, pos)
                    if y > 0:
                        tile_superior = tilemap.terreno[y - 1][x]
                        if tile_superior == TERRENO_LIGERO or tile_superior == TERRENO_COSTOSO:
                            self.fondo.blit(self.tileset.piso, pos)

    def render(self, player, npc):

        self.surface.fill(VERDE)
        self.surface.fill((0, 0, 0))
        self.surface.blit(self.fondo, (0, 0))

        # Camino jugador
        for px, py in player.ruta:

            rect = pygame.Rect(px * ESPACIO_RELATIVO + 8, py * ESPACIO_RELATIVO + 8, ESPACIO_RELATIVO - 16, ESPACIO_RELATIVO - 16)

            pygame.draw.rect(self.surface, AMARILLO, rect)

        # Jugador
        self.surface.blit( player.sprite, (player.x * ESPACIO_RELATIVO + 4, player.y * ESPACIO_RELATIVO + 4))

        # NPC
        self.surface.blit(npc.sprite, (npc.x * ESPACIO_RELATIVO + 4, npc.y * ESPACIO_RELATIVO + 4))

        scaled = pygame.transform.scale(self.surface, self.pantalla.get_size())

        self.pantalla.blit(scaled, (0, 0))
