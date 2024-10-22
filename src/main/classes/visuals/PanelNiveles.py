import pygame

from src.main.classes.visuals.Panel import Panel
from src.main.classes.visuals.BotonRect import BotonRect

class PanelNiveles(Panel):

    def __init__(self, x, y, width, height, juego):
        super().__init__(x, y, width, height)
        self.juego = juego
        self.fondoImageOG = pygame.image.load('../images/fondoMenuTest.png')
        self.fondoImage = pygame.transform.scale(self.fondoImageOG, (width, height))
        self.btnNiveles = []
        j=0
        i=0
        for a in range(20) :
            self.btnNiveles.append(BotonRect(width*(2+2*i)/13, height*(2+2*j)/13, 55, 55, self.juego.mostrarPanelCuadrilla,a))
            i = i+1
            if i >= 5:
                j = j+1
                i = 0

        self.btnVolver = BotonRect(width * 12 / 16, height * 15 / 16, 170, 35, self.juego.mostrarPanelMenu,None)
        self.btnVolver.setImage(pygame.image.load('../images/botonNormal.png'), pygame.image.load('../images/botonShaded.png'))

    def evento(self, event):
        for i in range(20):
            self.btnNiveles[i].evento(event)
        self.btnVolver.evento(event)

    def fitWindow(self, w, h):
        if w < h :
            multi = w / 720
        else :
            multi = h / 720

        self.w = w
        self.h = h
        self.fondoImage = pygame.transform.scale(self.fondoImageOG, (self.w, self.h))
        self.surface = pygame.Surface((self.w,self.h))
        self.surface.fill((self.red,self.green,self.blue))
        j=0
        i=0
        for a in range(20):
            self.btnNiveles[a].setValues(w*(2+2*i)/13, h*(2+2*j)/13, 55 * multi, 55 * multi)
            i = i + 1
            if i >= 5:
                j = j + 1
                i = 0
        self.btnVolver.setValues((self.w-180*multi), (self.h-45*multi), 170*multi, 35*multi)

    def draw(self, dest_surface):
        dest_surface.blit(self.fondoImage, (0, 0))
        for i in range(20):
            self.btnNiveles[i].draw(self.juego.getWindow())
        self.btnVolver.draw(self.juego.getWindow())