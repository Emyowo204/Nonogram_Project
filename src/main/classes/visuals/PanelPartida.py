import pygame

from src.main.classes.visuals.PanelNonograma import PanelNonograma
from src.main.classes.visuals.Panel import Panel
from src.main.classes.visuals.BotonRect import BotonRect


class PanelPartida(Panel):

    def __init__(self, x, y, width, height, game_difficulty, game_index, juego):
        super().__init__(x,y,width,height)
        self.vidas = 5
        self.errores = 0
        self.panel_nonograma = PanelNonograma(x, y, width, height, game_difficulty, game_index)
        self.setColor(200,200,200)
        self.font = pygame.font.Font(None, 40)
        self.stringInfo = 'Vidas: 5'
        self.botonVolver = BotonRect(width * 12 / 16, height * 15 / 16, 170, 35,juego.mostrarPanelMenu)
        self.botonVolver.setImage(pygame.image.load('../images/botonNormal.png'),pygame.image.load('../images/botonShaded.png'))

    def handleClick(self,pos):
        self.panel_nonograma.handleClick(pos)
        if self.panel_nonograma.checkAssumtion(pos) == 1:
            self.loseLife()

    def loseLife(self):
        self.vidas -= 1
        if self.vidas <= 0 :
            self.vidas = 0
            self.stringInfo = 'Vidas: 0 - Game Over'
        else :
            self.stringInfo = f'Vidas: {self.vidas}'
        self.surface.fill((self.red, self.green, self.blue))

    def evento(self, event):
        self.botonVolver.evento(event)

    def fitWindow(self, w, h):
        self.w = w
        self.h = h
        self.surface = pygame.Surface((self.w,self.h))
        self.surface.fill((self.red,self.green,self.blue))
        self.panel_nonograma.fitWindow(w, h)
        self.font = pygame.font.Font(None, int(w/18))

        if w < h :
            multi = w / 720
        else :
            multi = h / 720
        self.botonVolver.setSize(170*multi, 35*multi)
        self.botonVolver.setCoord((self.w-180*multi), (self.h-45*multi))

    def draw(self,dest_surface):
        super().draw(dest_surface)
        self.panel_nonograma.draw(self.surface)
        self.botonVolver.draw(self.surface)
        text_surface = self.font.render(self.stringInfo, False, (0, 0, 0))
        self.surface.blit(text_surface, (10, 10))



