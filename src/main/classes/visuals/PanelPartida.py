import pygame

from src.main.classes.visuals.ImageLoader import ImageLoader
from src.main.classes.visuals.PanelNonograma import PanelNonograma
from src.main.classes.visuals.Panel import Panel
from src.main.classes.visuals.BotonRect import BotonRect


class PanelPartida(Panel):

    def __init__(self, x, y, width, height, juego):
        super().__init__(x,y,width,height)
        self.vidas = 5
        self.panel_nonograma = PanelNonograma(self.x, self.y, self.w, self.h)
        self.setColor(200,200,200)
        self.font = pygame.font.Font(None, 40)
        self.stringInfo = 'Vidas: 5'
        self.btnOpciones = BotonRect(width-70, height-70, 60, 60, juego.mostrarPanelOpciones, None)
        self.btnOpciones.setImage(ImageLoader().getOpnNormal(), ImageLoader().getOpnShaded())
        self.botonVolver = BotonRect(10, height-70, 60, 60, juego.mostrarPanelNiveles,None)
        self.botonVolver.setImage(ImageLoader().getVolNormal(), ImageLoader().getVolShaded())
        self.juego = juego

    def setNonograma(self, path):
        self.panel_nonograma.setNonograma(path)
        self.vidas = 5
        self.stringInfo = 'Vidas: 5'

    def setVolverBoton(self, game_difficulty):
        self.botonVolver.setAction(self.juego.mostrarPanelNiveles, game_difficulty)

    def handleClick(self,pos):
        self.panel_nonograma.handleClick(pos)
        if self.panel_nonograma.checkAssumtion(pos) == 1:
            self.loseLife()

    def handleZoom(self,event, pos):
        self.panel_nonograma.handleZoom(event, pos)

    def defaultZoom(self):
        self.panel_nonograma.defaultZoom()

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
        self.btnOpciones.evento(event)

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
        self.btnOpciones.setValues(self.w-70*multi, self.h-70*multi, 60*multi, 60*multi)
        self.botonVolver.setValues(10*multi, self.h-70*multi, 60*multi, 60*multi)

    def draw(self,dest_surface):
        super().draw(dest_surface)
        self.panel_nonograma.draw(self.surface)
        self.botonVolver.draw(self.surface)
        self.btnOpciones.draw(self.juego.getWindow())
        text_surface = self.font.render(self.stringInfo, False, (0, 0, 0))
        self.surface.blit(text_surface, (10, 10))
