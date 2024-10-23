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
            self.numBotonsImage = []


            ImageLoader._inicializado = True

    def getDefaultImage(self):
        return self.defaultImage

    def getIcon(self):
        return self.program_icon