import pygame

from src.main.classes.visuals.Panel import Panel

class PanelCuadrilla(Panel):
    def __init__(self,cuadrilla,x,y,size):
        super().__init__(x, y, size, size)
        self.cell_size = 0
        self.size = cuadrilla.getSize()
        self.board = cuadrilla.getBoard()
        self.fitWindow(size)
        self.zoom_x = 1
        self.draw_xoffset = 0
        self.draw_yoffset = 0

    def setNewCuadrilla(self, cuadrilla):
        self.size = cuadrilla.getSize()
        self.board = cuadrilla.getBoard()

    def positionClick(self,pos):
        row = int((pos[1] - self.y - self.draw_yoffset) // self.cell_size)
        col = int((pos[0] - self.x - self.draw_xoffset) // self.cell_size)
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
        return self.size

    def getCellSize(self):
        return self.cell_size

    def handleZoom(self, event, pos):

        self.surface = pygame.Surface((self.w,self.h))
        old_zoom_x = self.zoom_x

        if event.y > 0:
            if self.zoom_x < 4:
                self.zoom_x += 0.1

        elif event.y < 0:
            if self.zoom_x > 1:
                self.zoom_x -= 0.1

        if self.zoom_x < 1:
            self.zoom_x = 1
        if self.zoom_x > 4:
            self.zoom_x = 4
        if self.zoom_x == 1:
            self.draw_xoffset = 0
            self.draw_yoffset = 0
            self.calculate_cellSize(self.w)
        else:
            new_cell_size = self.cell_size * (self.zoom_x / old_zoom_x)

            self.draw_xoffset += (pos[0] - self.x) * (1 - (new_cell_size / self.cell_size))
            self.draw_yoffset += (pos[1] - self.y) * (1 - (new_cell_size / self.cell_size))

            self.cell_size = new_cell_size

    def defaultZoom(self):
        self.zoom_x = 1
        self.draw_xoffset = 0
        self.draw_yoffset = 0

    def calculate_cellSize(self,size):
        if self.size[0] > self.size[1]:
            self.cell_size = size / self.size[0]
        else:
            self.cell_size = size / self.size[1]

    def fitWindow(self,size):
        self.w = size
        self.h = size
        self.surface = pygame.Surface((self.w,self.h))
        self.surface.fill((self.red, self.green, self.blue))
        self.calculate_cellSize(size)

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
                pygame.draw.rect(self.surface, color, (col * self.cell_size + self.draw_xoffset, row * self.cell_size + self.draw_yoffset, self.cell_size - 2, self.cell_size - 2))
        super().draw(dest_surface)

    def getXOffset(self):
        return self.draw_xoffset

    def getYOffset(self):
        return self.draw_yoffset

    def getZoom(self):
        return self.zoom_x