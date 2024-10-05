import pygame

from src.main.classes.visuals.Panel import Panel

class PanelCuadrilla(Panel):
    def __init__(self,cuadrilla,x,y,width,height):
        self.size = cuadrilla.getSize()
        self.board = cuadrilla.getBoard()
        self.cell_size = 30
        super().__init__(x,y,width,height)

    def handleClick(self, pos):
        row = (pos[1]-self.y) // self.cell_size
        col = (pos[0]-self.x) // self.cell_size
        if 0 <= row < len(self.board) and 0 <= col < len(self.board[row]):
            if(self.board[col][row] != -1 and self.board[col][row] != 1):
                self.board[col][row] = not self.board[col][row]

    def draw(self, dest_surface):

        for row in range(self.size[0]):
            for col in range(self.size[1]):
                color = (128,128,128)
                if self.board[col][row] == 0:
                    color = (0, 0, 0)
                elif self.board[col][row] == 1:
                    color = (255, 255, 255)
                elif self.board[col][row] == -1:
                    color =(255,0,0)
                pygame.draw.rect(dest_surface, color, (col * self.cell_size + self.x, row * self.cell_size + self.y, self.cell_size - 2, self.cell_size - 2))


