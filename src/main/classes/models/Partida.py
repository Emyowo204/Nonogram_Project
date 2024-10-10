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
        self.panel_resultado = PanelCuadrilla(self.cuadrilla_resultado, x, y + 330, 300, 300)

        self.size = self.cuadrilla_resultado.getSize()
        self.panelResultado.setColor(0,0,0)
        self.cuadrilla_jugador = Cuadrilla(self.size[0],self.size[1],None)
        self.panel_jugador = PanelCuadrilla(self.cuadrilla_jugador, x+40, y, 300, 300)


        self.panel_colnums = PanelNumeros(self.cuadrilla_resultado.getColumnNums(),'rows',x,y,30,300)

    def getSize(self):
        return self.size

    def handleClick(self,pos):
        self.panel_jugador.handleClick(pos)

    def loseLife(self):
        self.vidas -= 1

        print(f'tienes {self.vidas} vidas')

    def checkAssumtion(self,pos):
        col, row = self.panel_jugador.positionClick(pos)
        jugador_cell = self.cuadrilla_jugador.checkCell(col,row)
        resultado_cell = self.cuadrilla_resultado.checkCell(col,row)
        if col != -1 and row != -1:
            if  jugador_cell!=resultado_cell :
                if(jugador_cell!=-1):
                    self.loseLife()
                self.cuadrilla_jugador.setCell(col, row, -1)

    def draw(self,dest_surface):
        super().draw(dest_surface)
        self.panel_resultado.draw(dest_surface)
        self.panel_jugador.draw(dest_surface)
        self.panel_colnums.draw(dest_surface)
