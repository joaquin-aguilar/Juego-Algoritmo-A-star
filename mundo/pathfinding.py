import heapq
import math

# Heuristica de costo minimo para la navegacion
# Es importante conocer el costo minimo de navegacion para mejorar la eficiencia
COSTO_MINIMO = 1

# Reconstruccion de la ruta
def reconstruir_camino(origen, estado_actual):

    camino = [estado_actual]

    # Buscamos a los padres hasta encontrar al origen (sin padre)
    while estado_actual in origen:
        
        # Retroceder
        estado_actual = origen[estado_actual]
        # Guardar paso
        camino.append(estado_actual)

    # Como partimos desde el objetivo hacia el inicio invertimos la ruta.
    return camino[::-1]

# Heuristica de A* 
def distancia_objetivo(nodo_actual, nodo_objetivo):

    actual_x, actual_y = nodo_actual
    objetivo_x, objetivo_y = nodo_objetivo
    
    # Calculamos la distancia 
    return (math.dist((actual_x, actual_y),(objetivo_x, objetivo_y)) * COSTO_MINIMO)

# A*
def a_estrella(grafo, nodo_inicio, nodo_objetivo):

    nodos_pendientes = []
    heapq.heappush(nodos_pendientes,(0, nodo_inicio)) # ingresar a pila minima valores pequeños primero.
    nodos_visitados = set()

    origen = {} # Padres
    costo_real = {nodo_inicio: 0}

    while nodos_pendientes:
        _, nodo_actual = heapq.heappop(nodos_pendientes) # retirar de pila minima valores pequeños primero.

        # evitar revisitar nodos
        if nodo_actual in nodos_visitados:
            continue

        nodos_visitados.add(nodo_actual)

        # objetivo encontrado
        if nodo_actual == nodo_objetivo:
            camino = reconstruir_camino(origen, nodo_actual)
            costo_real = costo_real[nodo_actual]
            return (camino, costo_real)

        # explorar vecinos
        for nodo_vecino, costo_transicion in grafo[nodo_actual]:

            nuevo_costo = (costo_real[nodo_actual] + costo_transicion)

            if (nodo_vecino not in costo_real or nuevo_costo < costo_real[nodo_vecino]):
                
                origen[nodo_vecino] = nodo_actual # guardar padre
                costo_real[nodo_vecino] = nuevo_costo # actualizar costo real
                heuristica = (distancia_objetivo(nodo_vecino, nodo_objetivo)) # heurística

                prioridad = (nuevo_costo + heuristica) # prioridad total

                heapq.heappush(nodos_pendientes, (prioridad, nodo_vecino))

    return None
