import pygame

from src.main.classes.visuals.ImageLoader import ImageLoader
from src.main.classes.visuals.PanelNonograma import PanelNonograma
from src.main.classes.visuals.Panel import Panel
from src.main.classes.visuals.BotonRect import BotonRect
from src.main.classes.visuals.PanelNonogramaColored import PanelNonogramaColored


class PanelPartida(Panel):

    def __init__(self, x, y, width, height, juego):
        super().__init__(x,y,width,height)
        self.vidas = 5
        self.isSolved = 0
        self.type_nonograma = [PanelNonograma(self.x, self.y, self.w, self.h), PanelNonogramaColored(self.x, self.y, self.w, self.h)]
        self.panel_nonograma = self.type_nonograma[0]
        self.setColor(200,200,200)
        self.font = pygame.font.Font(None, 40)
        self.stringInfo = 'Vidas: 5'
        self.btnOpciones = BotonRect(width-70, height-70, 60, 60, juego.mostrarPanelOpciones, None)
        self.btnOpciones.setImage(ImageLoader().getOpnNormal(), ImageLoader().getOpnShaded())
        self.botonVolver = BotonRect(10, height-70, 60, 60, self.volverPanelNiveles,None)
        self.botonVolver.setImage(ImageLoader().getVolNormal(), ImageLoader().getVolShaded())
        self.botonReset = BotonRect(width-70, 10, 60, 60, self.resetNonograma,None)
        self.botonReset.setImage(ImageLoader().getVolNormal(), ImageLoader().getVolShaded())
        self.juego = juego
        self.game_difficulty = 0
        self.game_mode = 0

    def setNonograma(self, path, mode):
        self.panel_nonograma = self.type_nonograma[mode%2]
        self.panel_nonograma.setNonograma(path, mode)
        self.isSolved = 0
        self.vidas = 5-self.panel_nonograma.getInfoCuadrilla(0)[1]
        self.game_mode = mode
        if mode < 2:
            self.stringInfo = ''
        else:
            self.stringInfo = f'Vidas: {self.vidas}'
            if self.vidas <= 0:
                self.isSolved = -1
                self.stringInfo = f'Vidas: 0 - PERDISTE'
        self.checkSolve()

    def saveNonograma(self):
        self.panel_nonograma.saveNonograma()

    def volverPanelNiveles(self):
        self.saveNonograma()
        self.juego.mostrarPanelNiveles(self.game_difficulty)

    def resetNonograma(self):
        self.panel_nonograma.resetNonograma()
        self.isSolved = 0
        self.vidas = 5
        if self.game_mode >= 2:
            self.stringInfo = 'Vidas: 5'
        else:
            self.stringInfo = ''
        self.surface.fill((self.red, self.green, self.blue))

    def setVolverBoton(self, game_difficulty):
        self.game_difficulty = game_difficulty

    def handleClick(self,pos):
        if self.isSolved == 0:
            self.panel_nonograma.handleClick(pos)
            if self.panel_nonograma.checkAssumtion(pos) == 1 and self.game_mode >= 2:
                self.loseLife()
                if self.vidas == 0:
                    self.isSolved = -1
            self.checkSolve()

    def checkSolve(self):
        if self.panel_nonograma.getInfoCuadrilla(0)[0] == self.panel_nonograma.getInfoCuadrilla(1)[0]:
            if self.game_mode < 2 and self.panel_nonograma.getInfoCuadrilla(0)[1] == 0:
                self.isSolved = 1
                self.stringInfo = 'GANASTE!'
                self.surface.fill((self.red, self.green, self.blue))
            elif self.game_mode >= 2:
                self.isSolved = 1
                self.stringInfo = f'Vidas: {self.vidas} - GANASTE!'
                self.surface.fill((self.red, self.green, self.blue))

    def handleZoom(self,event, pos):
        self.panel_nonograma.handleZoom(event, pos)

    def defaultZoom(self):
        self.panel_nonograma.defaultZoom()

    def loseLife(self):
        self.vidas -= 1
        if self.vidas <= 0 :
            self.vidas = 0
            self.stringInfo = 'Vidas: 0 - PERDISTE'
        else :
            self.stringInfo = f'Vidas: {self.vidas}'
        self.surface.fill((self.red, self.green, self.blue))

    def evento(self, event):
        self.botonVolver.evento(event)
        self.btnOpciones.evento(event)
        self.botonReset.evento(event)

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
        self.botonReset.setValues(self.w-70*multi, 10*multi, 60*multi, 60*multi)

    def draw(self,dest_surface):
        super().draw(dest_surface)
        self.panel_nonograma.draw(self.surface)
        self.botonVolver.draw(self.surface)
        self.btnOpciones.draw(self.juego.getWindow())
        self.botonReset.draw(self.surface)
        text_surface = self.font.render(self.stringInfo, False, (0, 0, 0))
        self.surface.blit(text_surface, (10, 10))
