import random
import numpy as np

from principal.configuraciones import *
from mundo.terreno import *

class CelulasMapa:

    def __init__(self):

        # Generador determinista usando semilla
        self.random = random.Random(SEMILLA)

    def generar(self):
        terreno = np.zeros((ALTO, ANCHO), dtype=int)

        # Ruido Inicial
        for y in range(ALTO):
            for x in range(ANCHO):

                # Bordes siempre bloqueados
                if (x == 0 or y == 0 or x == ANCHO - 1 or y == ALTO - 1):
                    terreno[y][x] = PARED
                    continue

                # 45% probabilidad de pared
                terreno[y][x] = (PARED if self.random.random() < 0.45 else TERRENO_LIGERO)

        # Automatas Celulares
        for _ in range(5):

            iteracion_automata = terreno.copy()

            for y in range(ALTO):
                for x in range(ANCHO):

                    paredes = self.contar_paredes(terreno, x, y)
                    # si una celda está rodeada de muchas paredes
                    # entonces se convierte en pared.
                    if paredes > 4:
                        iteracion_automata[y][x] = PARED

                    elif paredes < 4:
                        # 20% terreno costoso
                        if self.random.random() < 0.20:
                            iteracion_automata[y][x] = TERRENO_COSTOSO
                        
                        else:
                            iteracion_automata[y][x] = TERRENO_LIGERO
            terreno = iteracion_automata

        return terreno
    
    def contar_paredes(self, terreno, x, y):

        paredes = 0
        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):
                # Ignorar centro
                if dx == 0 and dy == 0:
                    continue
                nodo_x = x + dx
                nodo_y = y + dy
                # Fuera del mapa cuenta como pared (para tener siempre bordes)
                if (nodo_x < 0 or nodo_y < 0 or nodo_x >= ANCHO or nodo_y >= ALTO or terreno[nodo_y][nodo_x] == PARED):
                    paredes += 1

        return paredes
