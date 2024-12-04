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
            self.defaultImage = pygame.image.load('main/images/default.png')
            self.program_icon = pygame.image.load('main/images/icon_temp.png')
            self.volverNormal = pygame.image.load('main/images/botonVolverNormal.png')
            self.volverShaded = pygame.image.load('main/images/botonVolverShaded.png')
            self.resetNormal = pygame.image.load('main/images/botonResetNormal.png')
            self.resetShaded = pygame.image.load('main/images/botonResetShaded.png')
            self.opcionNormal = pygame.image.load('main/images/botonOpcionNormal.png')
            self.opcionShaded = pygame.image.load('main/images/botonOpcionShaded.png')
            self.hintNormal = pygame.image.load('main/images/botonHintNormal.png')
            self.hintShaded = pygame.image.load('main/images/botonHintShaded.png')
            self.nivelNormal = pygame.image.load('main/images/botonNivelesNormal.png')
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

    def getResNormal(self):
        return self.resetNormal

    def getResShaded(self):
        return self.resetShaded

    def getOpnNormal(self):
        return self.opcionNormal

    def getOpnShaded(self):
        return self.opcionShaded

    def getHintNormal(self):
        return self.hintNormal

    def getHintShaded(self):
        return self.hintShaded

    def getNvlNormal(self):
        return self.nivelNormal