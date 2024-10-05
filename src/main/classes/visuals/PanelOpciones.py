import pygame

from src.main.classes.visuals.Panel import Panel

class PanelOpciones(Panel):
    def __init__(self, musica, x, y, width, height):
        super().__init__(x, y, width, height)
        self.musica = musica
        self.volumenActual = self.musica.getVolumen()
        self.slider= pygame.Rect(x+50, y+50, 200, 20)
        self.slideando = False

    def evento(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.slider.collidepoint(event.pos):
                self.slideando = True

        elif event.type == pygame.MOUSEBUTTONUP:
            self.slideando = False

        elif event.type == pygame.MOUSEMOTION:
            if self.slideando:
                self.slider.x = max(self.x+50, min(event.pos[0], self.x+250))
                nuevoVolumen = (self.slider.x - (self.x +50)) / 200
                self.musica.setVolumen(nuevoVolumen)

    def draw(self, destSurface):
        destSurface.fill((0,0,0,)) # panel en negro por mientras

        pygame.draw.rect(destSurface, (100, 100, 100), (self.x + 50, self.y + 50, 200, 20))  # fondo slider
        pygame.draw.rect(destSurface, (255, 0, 0), self.slider)  # el rectangulito del slide

        # añadir texto o indicador de volumen actual