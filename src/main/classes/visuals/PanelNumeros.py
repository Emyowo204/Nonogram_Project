import pygame
from src.main.classes.visuals.Panel import Panel


class PanelNumeros(Panel):
    def __init__(self, numbers,mode, x, y, width, height):
        super().__init__(x, y, width, height)
        self.numbers = numbers
        self.font = pygame.font.Font(None,18)
        self.mode = mode
        self.spacing = [0,0]
        self.halfCell = 0

    def drawNumbers(self,mode):
        for i in range(len(self.numbers)):
            for j in range(len(self.numbers[i])):
                text_surface = self.font.render(str(self.numbers[i][j]), False, (255, 255, 255))  # White color
                if self.mode== 'columns':
                    self.surface.blit(text_surface, (self.halfCell+i * self.spacing[0], j/10 * self.spacing[1]))
                elif mode== 'rows':
                    self.surface.blit(text_surface, (j/10 * self.spacing[1], self.halfCell+i * self.spacing[0]))

    def fitPanel(self,numCells):
        self.surface = pygame.Surface((self.w,self.h))
        if self.mode == 'columns':
            self.halfCell = (self.w*4/10) / numCells
            self.spacing[0] = self.w / numCells
            self.spacing[1] = self.w*5 / numCells
        elif self.mode == 'rows':
            self.halfCell = (self.h*3/10) / numCells
            self.spacing[0] = self.h / numCells
            self.spacing[1] = self.h*5 / numCells
        self.font = pygame.font.Font(None, 18)

    def draw(self, dest_surface):
        self.drawNumbers(self.mode)
        dest_surface.blit(self.surface,(self.x,self.y))

