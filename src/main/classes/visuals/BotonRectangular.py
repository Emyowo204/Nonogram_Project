import pygame

from src.main.classes.visuals.ImageLoader import ImageLoader

class BotonRectangular:
    def __init__(self, x, y, width, height, normalImage, shadedImage, pressedImage, action):
        self.rect = pygame.Rect(x, y, width, height)
        self.normalImage = pygame.transform.scale(normalImage, (width, height))
        self.shadedImage = pygame.transform.scale(shadedImage, (width, height))
        self.pressedImage = pygame.transform.scale(pressedImage, (width, height))
        self.currentImage = self.normalImage
        self.action = action

    def draw(self, screen):
        screen.blit(self.currentImage, (self.rect.x, self.rect.y))

    def evento(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            self.currentImage = self.pressedImage
            if self.action:
                self.action()
        elif event.type == pygame.MOUSEBUTTONUP and self.rect.collidepoint(event.pos):
            self.currentImage = self.shadedImage
        elif not self.rect.collidepoint(pygame.mouse.get_pos()):
            self.currentImage = self.normalImage

