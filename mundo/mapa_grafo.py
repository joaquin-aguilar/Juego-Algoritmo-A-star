from principal.configuraciones import *
from mundo.terreno import *

class MapaGrafo:
    
    # Crear el grafo a partir de una matriz rectangular
    def crear_grafo(mapa):
        grafo = {} # almacen de nodos

        # tamanio de la matriz
        filas = len(mapa) 
        columnas = len(mapa[0])


        # movimientos posibles (topdown con los puntos cardinales e intermedios)
        direcciones = [

            (-1, -1),  # arriba-izquierda
            (-1,  0),  # arriba
            (-1,  1),  # arriba-derecha

            ( 0, -1),  # izquierda
            ( 0,  1),  # derecha

            ( 1, -1),  # abajo-izquierda
            ( 1,  0),  # abajo
            ( 1,  1)   # abajo-derecha
        ]

        for y in range(filas):

            for x in range(columnas):

                # Ignorar paredes
                if mapa[y][x] == PARED:
                    continue

                nodo = (x, y) # incluir a cada espacio navegable como un nodo
                grafo[nodo] = [] # incluir a las aristas de cada nodo

                for direccion_x, direccion_y in direcciones:

                    vecino_x = x + direccion_x
                    vecino_y = y + direccion_y

                    # Validar límites del arreglo para la posicion del vecino
                    if not (0 <= vecino_x < columnas and 0 <= vecino_y < filas):
                        continue

                    # No hacer conecciones con las paredes
                    if mapa[vecino_y][vecino_x] == PARED:
                        continue

                    # No atravezar diagonales que tengan terreno no navegable en sus componentes x,y
                    es_diagonal = (direccion_x != 0 and direccion_y != 0)
                    if es_diagonal:
                        if (mapa[y][vecino_x] == PARED or
                            mapa[vecino_y][x] == PARED):
                            continue

                    # Elegir el valor transitorio entre nodos mayor
                    costo_nodo_actual = mapa[y][x]
                    costo_nodo_vecino = mapa[vecino_y][vecino_x]
                    peso = max(costo_nodo_actual, costo_nodo_vecino)


                    # Aplicar un multiplicador de costos para movimientos laterales.
                    if es_diagonal:
                        peso *= FACTOR_DIAGONAL

                    # Finalmente incluir la arista con su peso.
                    grafo[nodo].append(((vecino_x, vecino_y), peso))

        return grafo
