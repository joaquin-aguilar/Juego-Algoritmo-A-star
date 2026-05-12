import pygame
from principal.configuraciones import *
from principal.colores import *
from mundo.terreno import *

class Renderizador:

    def __init__(self, pantalla, tileset):

        self.pantalla = pantalla
        self.tileset = tileset

        self.surface = pygame.Surface((ANCHO_BASE, ALTO_BASE))

    def render(self, tilemap, player, npc):

        self.surface.fill(NEGRO)

        # Tilemap
        for y in range(ALTO):
            for x in range(ANCHO):

                tile = tilemap.terreno[y][x]

                pos = (x * ESPACIO_RELATIVO, y * ESPACIO_RELATIVO)

                if tile == PARED:
                    self.surface.blit(self.tileset.paredes, pos)

                elif tile == TERRENO_COSTOSO:
                    self.surface.blit(self.tileset.camino_dificil, pos)

                else:
                    self.surface.blit(self.tileset.camino_sencillo, pos)

        # Path jugador
        for px, py in player.ruta:

            rect = pygame.Rect(px * ESPACIO_RELATIVO + 8, py * ESPACIO_RELATIVO + 8, ESPACIO_RELATIVO - 16, ESPACIO_RELATIVO - 16)

            pygame.draw.rect(self.surface, AZUL, rect)

        # Jugador
        self.surface.blit( player.sprite, (player.x * ESPACIO_RELATIVO + 4, player.y * ESPACIO_RELATIVO + 4))

        # NPC
        self.surface.blit(npc.sprite, (npc.x * ESPACIO_RELATIVO + 4, npc.y * ESPACIO_RELATIVO + 4))

        scaled = pygame.transform.scale(self.surface, self.pantalla.get_size())

        self.pantalla.blit(scaled, (0, 0))
