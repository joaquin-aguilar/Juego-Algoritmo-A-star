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
        self.boton_ok = None

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

    def render(self, player, npcs, game_over):

        self.surface.fill((0, 0, 0))
        self.surface.blit(self.fondo, (0, 0))

        # Camino jugador
        for px, py in player.ruta:

            rect = pygame.Rect(px * ESPACIO_RELATIVO + 8, py * ESPACIO_RELATIVO + 8, ESPACIO_RELATIVO - 16, ESPACIO_RELATIVO - 16)

            pygame.draw.rect(self.surface, AMARILLO, rect)

        # Jugador
        sprite = player.sprite
        x = player.x * ESPACIO_RELATIVO + (ESPACIO_RELATIVO - sprite.get_width()) // 2
        y = player.y * ESPACIO_RELATIVO + (ESPACIO_RELATIVO - sprite.get_height()) // 2
        self.surface.blit(sprite, (x, y))

        # NPC
    
        for npc in npcs:
            self.surface.blit(npc.sprite, (npc.x * ESPACIO_RELATIVO + 4, npc.y * ESPACIO_RELATIVO + 4))

        # Game Over

        if game_over:
            self.render_game_over()

        scaled = pygame.transform.scale(self.surface, self.pantalla.get_size())
        self.pantalla.blit(scaled, (0, 0))
        

    def render_game_over(self):

        overlay = pygame.Surface(self.surface.get_size(), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180))
        self.surface.blit(overlay, (0, 0))
        fuente = pygame.font.SysFont(None, 64)
        texto = fuente.render("GAME OVER", True, (255, 255, 255))

        x = (ANCHO_BASE - texto.get_width()) // 2
        y = ALTO_BASE // 3

        self.surface.blit(texto, (x, y))
        self.boton_ok = pygame.Rect(ANCHO_BASE // 2 - 60, ALTO_BASE // 2, 120, 50)
        pygame.draw.rect(self.surface, (200, 200, 200), self.boton_ok)
        pygame.draw.rect(self.surface, (0, 0, 0), self.boton_ok, 2)
        texto_ok = fuente.render("OK", True, (0, 0, 0))
        self.surface.blit(texto_ok, (self.boton_ok.centerx - texto_ok.get_width() // 2, self.boton_ok.centery - texto_ok.get_height() // 2))