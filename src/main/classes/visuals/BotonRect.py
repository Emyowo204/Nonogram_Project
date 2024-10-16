import pygame

from src.main.classes.visuals.ImageLoader import ImageLoader

class BotonRect:
    def __init__(self, x, y, width, height, normalImage, shadedImage, action):
        self.coord = [x, y]
        self.size = [width, height]
        self.rect = pygame.Rect(x, y, width, height)
        self.normalImageSize = normalImage
        self.shadedImageSize = shadedImage
        self.normalImage = pygame.transform.scale(normalImage, (width, height))
        self.shadedImage = pygame.transform.scale(shadedImage, (width, height))
        self.currentImage = self.normalImage
        self.action = action
        self.pressed = False

    def evento(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            self.pressed = True
            if self.action:
                self.action()
        elif event.type == pygame.MOUSEBUTTONUP and self.rect.collidepoint(event.pos):
            self.currentImage = self.shadedImage
            self.pressed = False
        elif not self.rect.collidepoint(pygame.mouse.get_pos()):
            self.currentImage = self.normalImage

    def setSize(self,width, height):
        self.rect = pygame.Rect(self.coord[0], self.coord[1],width, height)
        self.normalImage = pygame.transform.scale(self.normalImageSize, (width, height))
        self.shadedImage = pygame.transform.scale(self.shadedImageSize, (width, height))
        self.size = [width, height]

    def setCoord(self,x,y):
        self.rect = pygame.Rect(x, y, self.size[0], self.size[1])
        self.coord = [x, y]

    def draw(self, screen):
        mouse = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse):
            self.currentImage = self.shadedImage
        else:
            self.currentImage = self.normalImage
        screen.blit(self.currentImage, (self.rect.x, self.rect.y))