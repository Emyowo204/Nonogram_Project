import pygame

from src.main.classes.visuals.Panel import Panel

class PanelCuadrilla(Panel):
    def __init__(self,cuadrilla,x,y,size):
        super().__init__(x, y, size, size)
        self.cell_size = 0
        self.size = cuadrilla.getSize()
        self.board = cuadrilla.getBoard()
        self.fitWindow(size)


    def positionClick(self,pos):
        row = int((pos[1] - self.y) // self.cell_size)
        col = int((pos[0] - self.x) // self.cell_size)
        if 0 <= col < self.size[0] and 0 <= row < self.size[1]:
            return col,row
        else:
            return -1,-1

    def handleClick(self, pos):
        col,row = self.positionClick(pos)
        if col != -1 and row != -1:
            if 0 <= col < len(self.board) and 0 <= row < len(self.board[col]):
                if self.board[col][row] != -1 and self.board[col][row] != 1:
                    self.board[col][row] = not self.board[col][row]

    def getSize(self):
        return self.board.getSize()

    def getCellSize(self):
        return self.cell_size

    def fitWindow(self,size):
        self.w = size
        self.h = size
        self.surface = pygame.Surface((self.w,self.h))
        self.surface.fill((self.red, self.green, self.blue))
        if self.size[0] > self.size[1]:
            self.cell_size = size / self.size[0]
        else:
            self.cell_size = size / self.size[1]

    def draw(self, dest_surface):

        for col in range(self.size[0]):
            for row in range(self.size[1]):
                cell =self.board[col][row]
                color = (128, 128, 128)
                if cell == 0:
                    color = (30, 30, 30)
                elif cell == 1:
                    color = (255, 255, 255)
                elif cell == -1:
                    color = (255, 0, 0)
                pygame.draw.rect(self.surface, color, (col * self.cell_size , row * self.cell_size, self.cell_size - 2, self.cell_size - 2))
        super().draw(dest_surface)