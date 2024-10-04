import pygame

from src.main.classes.visuals.Componente import Componente


class Panel(Componente):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.surface = pygame.Surface((width,height))
        self.surface.fill((255,0,0)) #Rojo
        self.container = []

    def setPos(self,x,y):
        self.x = x
        self.y = y

    def add(self, component):
        self.container.append(component)

    def draw(self, destSurface): #desSurface es una superficie a la cual se va a dibujar, ejemplo de uso dibujar a pantalla(surface)
        for component in self.container:
            component.draw(destSurface)
        super().draw(self.surface)
        destSurface.blit(self.surface,(self.x,self.y))