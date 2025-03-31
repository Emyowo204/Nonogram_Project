import pygame

from main.classes.visuals.ImageLoader import ImageLoader
from main.classes.visuals.Panel import Panel
from main.classes.visuals.BotonRect import BotonRect

class PanelNiveles(Panel):

    def __init__(self, x, y, width, height, juego):
        super().__init__(x, y, width, height)
        self.juego = juego
        self.fondoImageOG = pygame.image.load('main/images/fondoMenuTest.png')
        self.fondoImage = pygame.transform.scale(self.fondoImageOG, (width, height))
        self.btnNiveles = []
        self.cantidad_nivel = 0
        self.btnLoadImg = BotonRect(self.w/2-80, self.h-120, 160, 80, self.juego.mostrarPanelFileManager, None)
        self.btnLoadImg.setImage(pygame.image.load('main/images/btnImg2NonoNormal.png'), pygame.image.load('main/images/btnImg2NonoShaded.png'))
        self.btnOpciones = BotonRect(width-120, height-120, 80, 80, self.juego.mostrarPanelOpciones,None)
        self.btnOpciones.setImage(ImageLoader().getOpnNormal(), ImageLoader().getOpnShaded())
        self.btnVolver = BotonRect(40, height-120, 80, 80, self.juego.mostrarPanelMenu,None)
        self.btnVolver.setImage(ImageLoader().getVolNormal(), ImageLoader().getVolShaded())
        self.font = pygame.font.Font(None, 40)

    def setLoadEnable(self, enabled):
        self.btnLoadImg.setEnable(enabled)

    def setLevelButtons(self, quantity):
        self.cantidad_nivel = quantity
        j = 0
        i = 0
        for a in range(quantity):
            lvlSurNormal = pygame.image.load('main/images/botonNivelesNormal.png')
            lvlSurShaded = pygame.image.load('main/images/botonNivelesShaded.png')
            text_surface = self.font.render(str(a+1), False, (0, 0, 0))
            lvlSurNormal.blit(text_surface, (20,20))
            lvlSurShaded.blit(text_surface, (20, 20))
            self.btnNiveles.append(BotonRect(self.w * (1.5 + 2 * i) / 12, self.h * (1.5 + 2 * j) / 12, 60, 60, self.juego.mostrarPanelCuadrilla, a + 1))
            self.btnNiveles[a].setImage(lvlSurNormal, lvlSurShaded)
            i = i + 1
            if i >= 5:
                j = j + 1
                i = 0

    def evento(self, event):
        for i in range(self.cantidad_nivel):
            self.btnNiveles[i].evento(event)
        self.btnLoadImg.evento(event)
        self.btnVolver.evento(event)
        self.btnOpciones.evento(event)

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
        for a in range(self.cantidad_nivel):
            self.btnNiveles[a].setValues(w*(1.5+2*i)/12, h*(1.5+2*j)/12, 60 * multi, 60 * multi)
            i = i + 1
            if i >= 5:
                j = j + 1
                i = 0
        self.btnLoadImg.setValues(self.w/2-80*multi, self.h-120*multi, 160*multi, 80*multi)
        self.btnOpciones.setValues(self.w-120*multi, self.h-120*multi, 80*multi, 80*multi)
        self.btnVolver.setValues(40*multi, self.h-120*multi, 80*multi, 80*multi)

    def draw(self, dest_surface):
        super().draw(dest_surface)
        dest_surface.blit(self.fondoImage, (0, 0))
        for i in range(self.cantidad_nivel):
            self.btnNiveles[i].draw(self.juego.getWindow())
        if self.btnLoadImg.isEnabled():
            self.btnLoadImg.draw(self.juego.getWindow())
        self.btnVolver.draw(self.juego.getWindow())
        self.btnOpciones.draw(self.juego.getWindow())

