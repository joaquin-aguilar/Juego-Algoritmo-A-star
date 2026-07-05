import pygame


class SpriteSheet:

    def __init__(self, ruta):
        self.imagen = pygame.image.load(ruta).convert_alpha()

    def obtener_sprite(self, x, y, ancho, alto, ancho_final, alto_final=None, recortar_transparencia=False):

        if alto_final is None:
            alto_final = ancho_final

        sprite = pygame.Surface((ancho, alto), pygame.SRCALPHA)
        sprite.blit(self.imagen, (0, 0), pygame.Rect(x, y, ancho, alto))

        if recortar_transparencia:
            rect = sprite.get_bounding_rect()    
            if rect.width > 0 and rect.height > 0:
                sprite = sprite.subsurface(rect).copy()

        sprite = pygame.transform.smoothscale(sprite, (ancho_final, alto_final))

        return sprite