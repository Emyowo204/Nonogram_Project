import pygame

from src.main.classes.models.Cuadrilla import Cuadrilla
from src.main.classes.models.BoardEnum import BoardEnum
from src.main.classes.visuals.Panel import Panel
from src.main.classes.visuals.PanelCuadrilla import PanelCuadrilla
from src.main.classes.visuals.PanelNumeros import PanelNumeros


class Partida(Panel):


    def __init__(self, x, y, width, height, game_difficulty, game_index):
        super().__init__(x,y,width,height)
        self.vidas = 5
        self.errores = 0
        self.setColor(0,100,0)
        self.cuadrilla_resultado = Cuadrilla(None, None, BoardEnum[game_difficulty].value[game_index])
        self.panel_resultado = PanelCuadrilla(self.cuadrilla_resultado, 0, 330, 300)

        self.board_size = self.cuadrilla_resultado.getSize()
        self.panel_resultado.setColor(0,0,0)
        self.cuadrilla_jugador = Cuadrilla(self.board_size[0], self.board_size[1], None)
        self.panel_jugador = PanelCuadrilla(self.cuadrilla_jugador, 0, 0, 300)
        self.panel_colnums = PanelNumeros(self.cuadrilla_resultado.getColumnNums(),'columns',0,0,300,300)
        self.panel_rownums = PanelNumeros(self.cuadrilla_resultado.getRowNums(), 'rows', 0, 0, 30, 300)

    def getSize(self):
        return self.board_size

    def getBoardPosition(self,pos):
        return pos[0] - self.x, pos[1] - self.y

    def handleClick(self,pos):
        self.panel_jugador.handleClick(self.getBoardPosition(pos))

    def loseLife(self):
        self.vidas -= 1

        print(f'tienes {self.vidas} vidas')

    def checkAssumtion(self,pos):
        col, row = self.panel_jugador.positionClick(self.getBoardPosition(pos))
        jugador_cell = self.cuadrilla_jugador.checkCell(col,row)
        resultado_cell = self.cuadrilla_resultado.checkCell(col,row)
        if col != -1 and row != -1:
            if  jugador_cell!=resultado_cell :
                if jugador_cell!=-1:
                    self.loseLife()
                self.cuadrilla_jugador.setCell(col, row, -1)

    def fitWindow(self, w, h):
        if w < h:
            self.w = w / 2
            self.h = w
        else:
            self.h = h
            self.w = h / 2

        self.x = (w - self.w) / 2
        self.y = (h - self.h) / 2

        self.surface = pygame.Surface((self.w,self.h))
        self.surface.fill((self.red,self.green,self.blue))

        self.panel_jugador.fitWindow(self.w)
        self.panel_resultado.setPos(0,self.h/2)
        self.panel_resultado.fitWindow(self.w)

    def draw(self,dest_surface):
        super().draw(dest_surface)
        self.panel_resultado.draw(self.surface)
        self.panel_jugador.draw(self.surface)
        self.panel_colnums.draw(self.surface)
        self.panel_rownums.draw(self.surface)
