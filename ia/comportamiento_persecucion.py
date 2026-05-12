from mundo.pathfinding import a_estrella


class ComportamientoPersecucion:
    def update(self, npc, player, tilemap):

        resultado = a_estrella(tilemap.grafo, npc.posicion, player.posicion)
        if resultado:
            npc.ruta, npc.path_cost = resultado
        else:
            npc.ruta = []