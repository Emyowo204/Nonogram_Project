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
        self.botonJugar = BotonRect(width*1/4, height*2/8, width*1/2, height*1/8, self.normalImage, self.shadedImage, self.juego.mostrarPanelCuadrilla)
        self.botonOpciones = BotonRect(width*1/4, height*4/8, width*1/2, height*1/8, self.normalImage, self.shadedImage, self.juego.mostrarPanelOpciones)

    def evento(self, event):
        self.botonJugar.evento(event)
        self.botonOpciones.evento(event)

    def fitWindow(self, w, h):
        self.w = w
        self.h = h
        self.surface = pygame.Surface((self.w,self.h))
        self.surface.fill((self.red,self.green,self.blue))
        self.botonJugar.setCoord(self.w*1/4, self.h*2/8)
        self.botonJugar.setSize(self.w*1/2, self.h*1/8)
        self.botonOpciones.setCoord(self.w*1/4, self.h*4/8)
        self.botonOpciones.setSize(self.w*1/2, self.h*1/8)


    def draw(self, dest_surface):
        dest_surface.blit(self.fondoImage, (0, 0)) # panel en negro por mientras
        self.botonJugar.draw(self.juego.getWindow())
        self.botonOpciones.draw(self.juego.getWindow())

