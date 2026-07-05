import pygame

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

        self.screen = pygame.display.set_mode((ANCHO_BASE, ALTO_BASE), pygame.RESIZABLE)

        pygame.display.set_caption(f"Juego de Navegacion {SEMILLA}")

        self.clock = pygame.time.Clock()

        # Tiles
        self.tileset = TileSet()
        self.player_sprite = pygame.Surface((24, 24))
        self.player_sprite.fill(AZUL)
        self.npc_sprite = pygame.Surface((24, 24))
        self.npc_sprite.fill(ROJO)

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

        # Spawn NPC
        self.npc = None
        for y in range(ALTO - 1, -1, -1):
            for x in range(ANCHO - 1, -1, -1):
                if self.tilemap.es_caminable(x, y):
                    self.npc = NPC(x, y, self.npc_sprite)
                    break
            if self.npc:
                break

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

            # Update
            self.player.actualizar(dt)
            self.npc.update(dt, self.player, self.tilemap)

            # Render

            self.renderer.render(self.player, self.npc)
            pygame.display.flip()
        pygame.quit()