import pygame
from src.main.classes.visuals.Panel import Panel


class PanelNumeros(Panel):
    def __init__(self, numbers,mode, x, y, width, height):
        super().__init__(x, y, width, height)
        self.numbers = numbers
        self.font = pygame.font.Font(None,18)
        self.mode = mode

    def drawNumbers(self,mode):
        spacing = 50
        for i in range(len(self.numbers)):
            for j in range(len(self.numbers[i])):
                text_surface = self.font.render(str(self.numbers[i][j]), False, (255, 255, 255))  # White color
                if self.mode== 'columns':
                    self.surface.blit(text_surface, (i*2/3 * spacing, j/10 * spacing))
                elif mode== 'rows':
                    self.surface.blit(text_surface, (j/10 * spacing, i*2/3 * spacing))


    def draw(self, dest_surface):
        self.drawNumbers(self.mode)
        dest_surface.blit(self.surface,(self.x,self.y))

