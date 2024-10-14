import pygame

from src.main.classes.visuals.Panel import Panel
from src.main.classes.visuals.BotonRect import BotonRect

class PanelMenu(Panel):
    def __init__(self, x, y, width, height, juego):
        super().__init__(x, y, width, height)
        self.juego = juego
        self.fondoImage = pygame.image.load('../images/pruebaPanelMenu.png')
        self.fondoImage = pygame.transform.scale(self.fondoImage, (width, height))
        self.normalImage = pygame.image.load('../images/botonNormal.png')
        self.shadedImage = pygame.image.load('../images/botonShaded.png')
        self.botonJugar = BotonRect(100, 100, 300, 50, self.normalImage, self.shadedImage, self.juego.mostrarPanelCuadrilla)
        self.botonOpciones = BotonRect(100, 300, 300, 50, self.normalImage, self.shadedImage, self.juego.mostrarPanelOpciones)

    def evento(self, event):
        self.botonJugar.evento(event)
        self.botonOpciones.evento(event)

    def draw(self, dest_surface):
        dest_surface.blit(self.fondoImage, (0, 0)) # panel en negro por mientras
        self.botonJugar.draw(self.juego.getWindow())
        self.botonOpciones.draw(self.juego.getWindow())

