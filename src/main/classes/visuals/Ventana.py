import pygame

from src.main.classes.visuals.ImageLoader import ImageLoader


class Ventana:
    def __init__(self,height,width):
        pygame.init()
        self.program_icon = ImageLoader().getIcon()
        pygame.display.set_icon(self.program_icon)
        self.window_size = (height,width)
        self.window = pygame.display.set_mode(self.window_size, pygame.RESIZABLE)

    def getWindow(self):
        return self.window

    def resizeWindow(self,height,width):
        self.window_size=(height,width)
        self.window = pygame.display.set_mode(self.window_size, pygame.RESIZABLE)
