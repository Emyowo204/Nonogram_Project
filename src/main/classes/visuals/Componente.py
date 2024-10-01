


class Componente:
    def __init__(self, x, y, width, height):
        self.image = None
        self.x = x
        self.y = y
        self.w = width
        self.h = height

    def setImage(self, image):
        self.image = image

    def setCoords(self, x, y):
        self.x = x
        self.y = y

    def setSize(self, width, height):
        self.w = width
        self.h = height

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))
