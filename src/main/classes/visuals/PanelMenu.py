import pygame

from src.main.classes.visuals.Panel import Panel
from src.main.classes.visuals.BotonRect import BotonRect

class PanelMenu(Panel):
    def __init__(self, x, y, width, height, juego):
        super().__init__(x, y, width, height)
        self.juego = juego
        self.normalImage = pygame.image.load('../images/botonNormal.png')
        self.shadedImage = pygame.image.load('../images/botonShaded.png')
        self.botonJugar = (BotonRect(300, 300, 40, 40, self.normalImage, self.shadedImage, self.juego.mostrarPanelCuadrilla()))
        self.botonOpciones = BotonRect(500, 300, 40, 40, self.normalImage, self.shadedImage, self.juego.mostrarPanelOpciones())


    def draw(self, dest_surface):
        dest_surface.fill((0, 0, 0)) # panel en negro por mientras

