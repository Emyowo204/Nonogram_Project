import pygame

from src.main.classes.visuals.PanelNonograma import PanelNonograma
from src.main.classes.visuals.Panel import Panel


class PanelPartida(Panel):

    def __init__(self, x, y, width, height, game_difficulty, game_index):
        super().__init__(x,y,width,height)
        self.vidas = 5
        self.errores = 0
        self.panel_nonograma = PanelNonograma(x, y, width, height, game_difficulty, game_index)
        self.setColor(200,200,200)
        self.font = pygame.font.Font(None, 40)

    def handleClick(self,pos):
        self.panel_nonograma.handleClick(pos)
        if self.panel_nonograma.checkAssumtion(pos) == 1:
            self.loseLife()

    def loseLife(self):
        self.vidas -= 1
        if self.vidas <= 0 :
            self.vidas = 0
        self.surface.fill((self.red, self.green, self.blue))

    def fitWindow(self, w, h):
        self.w = w
        self.h = h
        self.surface = pygame.Surface((self.w,self.h))
        self.surface.fill((self.red,self.green,self.blue))
        self.panel_nonograma.fitWindow(w, h)
        self.font = pygame.font.Font(None, int(w/15))

    def draw(self,dest_surface):
        super().draw(dest_surface)
        self.panel_nonograma.draw(self.surface)
        text_surface = self.font.render(f'Vidas: {self.vidas}', False, (0, 0, 0))
        self.surface.blit(text_surface, (10, 10))



