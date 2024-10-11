import pygame
from src.main.classes.visuals.Panel import Panel


class PanelNumeros(Panel):
    def __init__(self, numbers,mode, x, y, width, height):
        super().__init__(x, y, width, height)
        self.numbers = numbers
        self.font = pygame.font.Font(None,18)
        self.mode = mode
        self.spacingSameGroup = 150
        self.spacingDiftGroup = 50
        self.halfCell = 0

    def drawNumbers(self,mode):
        for i in range(len(self.numbers)):
            for j in range(len(self.numbers[i])):
                text_surface = self.font.render(str(self.numbers[i][j]), False, (255, 255, 255))  # White color
                if self.mode== 'columns':
                    self.surface.blit(text_surface, (+self.halfCell+i*2/3 * self.spacingDiftGroup, j/10 * self.spacingSameGroup))
                elif mode== 'rows':
                    self.surface.blit(text_surface, (j/10 * self.spacingSameGroup, i*2/3 * self.spacingDiftGroup))

    def fitPanel(self,numCells,sizeCell):
        self.surface = pygame.Surface((self.w,self.h))
        self.spacingDiftGroup = (self.w*3/2)/numCells
        self.halfCell = sizeCell*4/10
        self.font = pygame.font.Font(None, 18)

    def draw(self, dest_surface):
        self.drawNumbers(self.mode)
        dest_surface.blit(self.surface,(self.x,self.y))

