import pygame

from src.main.classes.visuals.Panel import Panel

class PanelCuadrillaColored(Panel):
    def __init__(self,cuadrilla_colored,x,y,size):
        super().__init__(x, y, size, size)
        self.cell_size = 0
        self.size = cuadrilla_colored.getSize()
        self.board = cuadrilla_colored.getBoard()
        self.colors = cuadrilla_colored.getColors()
        self.selected_color = 1
        self.fitWindow(size)
        self.zoom_x = 1
        self.draw_xoffset = 0
        self.draw_yoffset = 0

    def setNewCuadrilla(self, cuadrilla_colored):
        self.size = cuadrilla_colored.getSize()
        self.board = cuadrilla_colored.getBoard()
        self.colors = cuadrilla_colored.getColors()

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
                current_value = self.board[col][row]
                if current_value != 0:
                    self.board[col][row] = self.selected_color

    def handleKey(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                self.selected_color = 0
            elif event.key == pygame.K_1:
                self.selected_color = 1
            elif event.key == pygame.K_2:
                self.selected_color = 1
            elif event.key == pygame.K_3:
                self.selected_color = 3

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

            self.draw_xoffset += (pos[0] - self.x - self.draw_xoffset) * (1 - (new_cell_size / self.cell_size))
            self.draw_yoffset += (pos[1] - self.y - self.draw_yoffset) * (1 - (new_cell_size / self.cell_size))

            if self.draw_xoffset > 0 and self.w > (self.size[0] * new_cell_size)/self.w * new_cell_size - self.draw_xoffset:
                self.draw_xoffset = 0
            elif self.draw_xoffset < 0 and self.draw_xoffset + (self.size[0] * new_cell_size) < self.w:
                self.draw_xoffset = -(self.size[0] * new_cell_size - self.w)

            if self.draw_yoffset > 0 and self.h > (self.size[1] * new_cell_size)/self.h * new_cell_size - self.draw_yoffset:
                self.draw_yoffset = 0
            elif self.draw_yoffset < 0 and self.draw_yoffset + (self.size[1] * new_cell_size) < self.h:
                self.draw_yoffset = -(self.size[1] * new_cell_size - self.h)

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
                cell = self.board[col][row]
                color = self.colors[cell]
                pygame.draw.rect(self.surface, color, (col * self.cell_size + self.draw_xoffset, row * self.cell_size + self.draw_yoffset, self.cell_size - 2, self.cell_size - 2))
        super().draw(dest_surface)

    def getXOffset(self):
        return self.draw_xoffset

    def getYOffset(self):
        return self.draw_yoffset

    def getZoom(self):
        return self.zoom_x

