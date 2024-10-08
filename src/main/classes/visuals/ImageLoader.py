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
            self.image = pygame.image.load('../images/default.png')
            self.program_icon = pygame.image.load('../images/icon_temp.png')
            ImageLoader._inicializado = True

    def getImage(self):
        return self.image

    def getIcon(self):
        return self.program_icon