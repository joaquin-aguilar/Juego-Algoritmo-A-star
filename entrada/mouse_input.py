from principal.configuraciones import *

def get_grid_position(mouse_pos, tamanio_pantalla):

    mouse_x, mouse_y = mouse_pos

    pantalla_ancho, pantalla_alto = tamanio_pantalla

    scale_x = ANCHO_BASE / pantalla_ancho
    scale_y = ALTO_BASE / pantalla_alto

    mouse_x = int(mouse_x * scale_x)
    mouse_y = int(mouse_y * scale_y)

    grilla_x = mouse_x // ESPACIO_RELATIVO
    grilla_y = mouse_y // ESPACIO_RELATIVO

    return grilla_x, grilla_y
