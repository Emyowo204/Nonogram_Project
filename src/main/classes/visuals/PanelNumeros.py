import pygame
from src.main.classes.visuals.Panel import Panel


class PanelNumeros(Panel):
    def __init__(self, numbers,mode, x, y, width, height):
        super().__init__(x, y, width, height)
        self.zoom = 1
        self.offset = 0
        self.numbers = numbers
        self.font = pygame.font.Font(None,18)
        self.mode = mode
        self.spacing = [0,0]
        self.halfCell = 0
        self.max_lenght = len(max(numbers, key=len))

    def setNewNumbers(self, numbers, mode):
        self.numbers = numbers
        self.mode = mode
        self.max_lenght = len(max(numbers, key=len))

    def drawNumbers(self,mode):
        for i in range(len(self.numbers)):
            for j in range(len(self.numbers[i])):
                text_surface = self.font.render(str(self.numbers[i][len(self.numbers[i])-1-j]), False, (255, 255, 255))  # White color
                if self.mode== 'columns':
                    self.surface.blit(text_surface, (self.halfCell+i * self.spacing[0] * self.zoom + self.offset, (self.max_lenght-1-j)/10 * self.spacing[1]))
                elif mode== 'rows':
                    self.surface.blit(text_surface, ((self.max_lenght-1-j)/10 * self.spacing[1] , self.halfCell+i * self.spacing[0] * self.zoom + self.offset) )

    def fitPanel(self,numCells):
        self.surface = pygame.Surface((self.w,self.h))
        if self.mode == 'columns':
            self.halfCell = (self.w*3/10) / numCells
            self.spacing[0] = self.w / numCells
            self.spacing[1] = self.h*10 / self.max_lenght
        elif self.mode == 'rows':
            self.halfCell = (self.h*3/10) / numCells
            self.spacing[0] = self.h / numCells
            self.spacing[1] = self.w*10 / self.max_lenght
        self.font = pygame.font.Font(None, int(self.halfCell)*3)

    def handleZoom(self, zoom, y_offset):
        self.surface = pygame.Surface((self.w,self.h))
        self.offset = y_offset
        self.zoom = zoom

    def defaultZoom(self):
        self.zoom = 1
        self.offset = 0

    def draw(self, dest_surface):
        self.drawNumbers(self.mode)
        dest_surface.blit(self.surface,(self.x,self.y))

