import pygame

class Panel:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.w = width
        self.h = height
        self.surface = pygame.Surface((width,height))
        self.surface.fill((255,0,0)) #Rojo
        self.container = []

    def add(self,component):
        self.container.append(component)

    def draw(self, destSurface): #desSurface es una superficie a la cual se va a dibujar, ejemplo de uso dibujar a pantalla(surface)
        for component in self.container:
            self.surface.blit(component,component.getDest())
        destSurface.blit(self.surface,(self.x,self.y))