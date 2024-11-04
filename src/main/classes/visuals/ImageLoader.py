import pygame.image

class ImageLoader:

    _instancia = None
    _inicializado = False
    def __new__(cls, *args, **kwargs):
        if cls._instancia is None:
            cls._instancia = super(ImageLoader, cls).__new__(cls)
        return cls._instancia

    def __init__(self):
        if not self._inicializado:
            self.defaultImage = pygame.image.load('../images/default.png')
            self.program_icon = pygame.image.load('../images/icon_temp.png')
            self.volverNormal = pygame.image.load('../images/botonVolverNormal.png')
            self.volverShaded = pygame.image.load('../images/botonVolverShaded.png')
            self.opcionNormal = pygame.image.load('../images/botonOpcionNormal.png')
            self.opcionShaded = pygame.image.load('../images/botonOpcionShaded.png')
            self.nivelNormal = pygame.image.load('../images/botonNivelesNormal.png')
            self.numButtonsImage = []

            ImageLoader._inicializado = True

    def getDefaultImage(self):
        return self.defaultImage

    def getIcon(self):
        return self.program_icon

    def getVolNormal(self):
        return self.volverNormal

    def getVolShaded(self):
        return self.volverShaded

    def getOpnNormal(self):
        return self.opcionNormal

    def getOpnShaded(self):
        return self.opcionShaded

    def getNvlNormal(self):
        return self.nivelNormal