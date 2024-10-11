import pygame

from src.main.classes.visuals.BotonRectangular import BotonRectangular
from src.main.classes.visuals.ImageLoader import ImageLoader
from src.main.classes.visuals.Panel import Panel

class PanelOpciones(Panel):
    def __init__(self, x, y, width, height, juego):
        super().__init__(x, y, width, height)
        self.juego = juego
        self.slider= pygame.Rect(x+50, y+50, 200, 20)
        self.slideando = False
        self.normalImage = pygame.image.load('../images/botonNormal.png')
        self.shadedImage = pygame.image.load('../images/botonShaded.png')
        self.pressedImage = pygame.image.load('../images/botonPressed.png')
        self.botonVolver = BotonRectangular(500, 300, 40, 40, self.normalImage, self.shadedImage, self.pressedImage, self.juego.mostrarPanelCuadrilla)

    def evento(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.slider.collidepoint(event.pos):
            self.slideando = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.slideando = False
        elif event.type == pygame.MOUSEMOTION and self.slideando:
            self.slider.x = max(self.x+50, min(event.pos[0], self.x+250))
        ##        nuevoVolumen = (self.slider.x - (self.x +50)) / 200
        ##        self.juego.getMusica.setVolumen(nuevoVolumen)

        self.botonVolver.evento(event)

    def draw(self, dest_surface):
        dest_surface.fill((0, 0, 0,)) # panel en negro por mientras
        self.botonVolver.draw(self.juego.getWindow())
        pygame.draw.rect(dest_surface, (100, 100, 100), (self.x + 30, self.y + 45, 250, 30))  # fondo slider
        pygame.draw.rect(dest_surface, (255, 0, 0), self.slider)  # el rectangulito del slide

        # añadir texto o indicador de volumen actual
