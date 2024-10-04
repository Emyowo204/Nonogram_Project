import pygame

from src.main.classes.visuals.Panel import Panel


class PanelCuadrilla(Panel):
    def __init__(self,cuadrilla,x,y,width,height):
        self.size = cuadrilla.getSize()
        self.board = cuadrilla.getBoard()
        self.cell_size = 30
        super().__init__(x,y,width,height)

    def draw(self, destSurface):

        for row in range(self.size[0]):
            for col in range(self.size[1]):
                color = (0, 0, 0) if self.board[col][row] == 0 else (255, 255, 255)
                pygame.draw.rect(destSurface, color,(col * self.cell_size + self.x, row * self.cell_size +self.y, self.cell_size - 2, self.cell_size - 2))


