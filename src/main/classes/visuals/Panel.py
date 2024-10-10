import pygame

from src.main.classes.visuals.Componente import Componente

class Panel(Componente):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.red = 0
        self.green = 0
        self.blue = 0
        self.surface = pygame.Surface((width,height))
        self.surface.fill((self.red,self.green,self.blue))
        self.container = []

    def setPos(self,x,y):
        self.x = x
        self.y = y

    def add(self, component):
        self.container.append(component)

    def setColor(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue
        self.surface.fill((self.red, self.green, self.blue))

    def draw(self, dest_surface): #desSurface es una superficie a la cual se va a dibujar, ejemplo de uso dibujar a pantalla(surface)
        for component in self.container:
            component.draw(self.surface)
        dest_surface.blit(self.surface, (self.x, self.y))
        if (self.image != None):
            super().draw(dest_surface)