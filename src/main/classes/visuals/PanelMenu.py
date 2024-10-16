import pygame

from src.main.classes.visuals.Panel import Panel
from src.main.classes.visuals.BotonRect import BotonRect

class PanelMenu(Panel):
    def __init__(self, x, y, width, height, juego):
        super().__init__(x, y, width, height)
        self.juego = juego
        self.fondoImageOG = pygame.image.load('../images/fondoMenuTest.png')
        self.fondoImage = pygame.transform.scale(self.fondoImageOG, (width, height))
        normalImage = pygame.image.load('../images/botonJugar.png')
        shadedImage = pygame.image.load('../images/botonJugarShaded.png')
        self.botonJugar = BotonRect(width*1/4, height*2/8, 360, 90, normalImage, shadedImage, self.juego.mostrarPanelCuadrilla)
        normalImage = pygame.image.load('../images/botonOpciones.png')
        shadedImage = pygame.image.load('../images/botonOpcionesShaded.png')
        self.botonOpciones = BotonRect(width*1/4, height*4/8, 360, 90, normalImage, shadedImage, self.juego.mostrarPanelOpciones)

    def evento(self, event):
        self.botonJugar.evento(event)
        self.botonOpciones.evento(event)

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

        self.botonJugar.setSize(360*multi, 90*multi)
        self.botonJugar.setCoord((self.w-self.botonJugar.getSize()[0])/2, (self.h-self.botonJugar.getSize()[1])*2/7)
        self.botonOpciones.setSize(360*multi, 90*multi)
        self.botonOpciones.setCoord((self.w-self.botonOpciones.getSize()[0])/2, (self.h-self.botonOpciones.getSize()[1])*4/7)

    def draw(self, dest_surface):
        dest_surface.blit(self.fondoImage, (0, 0)) # panel en negro por mientras
        self.botonJugar.draw(self.juego.getWindow())
        self.botonOpciones.draw(self.juego.getWindow())