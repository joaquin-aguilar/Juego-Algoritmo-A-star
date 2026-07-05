import pygame
import random

from principal.configuraciones import *
from principal.colores import *

from mundo.celulas_mapa import CelulasMapa
from mundo.mapa_grafo import MapaGrafo
from mundo.tilemap import TileMap
from mundo.pathfinding import a_estrella

from graficos.tiles import TileSet
from graficos.renderizador import Renderizador

from entidades.jugador import Jugador
from entidades.npc import NPC

from entrada.mouse_input import get_grid_position


class Game:

    def __init__(self):

        pygame.init()
        self.game_over = False

        self.screen = pygame.display.set_mode((ANCHO_BASE, ALTO_BASE), pygame.RESIZABLE)

        pygame.display.set_caption(f"Juego de Navegacion {SEMILLA}")

        self.clock = pygame.time.Clock()

        # Tiles
        self.tileset = TileSet()
        self.player_sprite = self.tileset.jugador
        self.npc_sprite = self.tileset.enemigo

        # Mundo
        generator = CelulasMapa()
        terreno = generator.generar()
        grafo = MapaGrafo.crear_grafo(terreno)
        self.tilemap = TileMap(terreno, grafo)
        self.renderer = Renderizador(self.screen, self.tileset)
        self.renderer.generar_fondo(self.tilemap)

        # Spawn jugador

        self.player = None
        for y in range(ALTO):
            for x in range(ANCHO):
                if self.tilemap.es_caminable(x, y):
                    self.player = Jugador(x, y, self.player_sprite)
                    break
            if self.player:
                break

        # Spawn NPCs

        self.npcs = []
        DISTANCIA_MINIMA = 10
        while len(self.npcs) < CANTIDAD_NPC:

            x = random.randint(0, ANCHO - 1)
            y = random.randint(0, ALTO - 1)

            if not self.tilemap.es_caminable(x, y):
                continue

            distancia = abs(x - self.player.x) + abs(y - self.player.y)

            if distancia < DISTANCIA_MINIMA:
                continue

            valido = True

            for npc in self.npcs:
                distancia = abs(x - npc.x) + abs(y - npc.y)
                if distancia < DISTANCIA_MINIMA:
                    valido = False
                    break

            if valido:
                self.npcs.append(NPC(x, y, self.npc_sprite))
        

    def run(self):

        running = True
        while running:
            dt = self.clock.tick(FPS)

            # Eventos
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    resultado = None
                    gx, gy = get_grid_position(pygame.mouse.get_pos(), self.screen.get_size())
                    if self.tilemap.es_caminable(gx, gy):
                        resultado = a_estrella(self.tilemap.grafo, self.player.posicion, (gx, gy))
                    
                    if resultado:
                        self.player.ruta, self.player.path_cost = resultado
                    
                    else:
                        self.player.ruta = []
                if self.game_over:

                    if event.type == pygame.MOUSEBUTTONDOWN:

                        mx, my = pygame.mouse.get_pos()
                        sx = self.screen.get_width() / ANCHO_BASE
                        sy = self.screen.get_height() / ALTO_BASE
                        mx /= sx
                        my /= sy

                        if self.renderer.boton_ok.collidepoint(mx, my):
                            running = False

                    continue
            # Update
            self.player.actualizar(dt)
            for npc in self.npcs:
                npc.update(dt, self.player, self.tilemap)
            
            for npc in self.npcs:
                if npc.posicion == self.player.posicion:
                    self.game_over = True

            # Render

            self.renderer.render(self.player, self.npcs, self.game_over)
            pygame.display.flip()
        pygame.quit()