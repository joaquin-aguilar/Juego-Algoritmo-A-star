class Entidad:

    def __init__(self, x, y, sprite):

        self.x = x
        self.y = y
        self.sprite = sprite

        self.ruta = []
        self.velocidad_movimiento = 0

    @property
    def posicion(self):
        return (self.x, self.y)
