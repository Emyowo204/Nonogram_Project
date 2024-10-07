import pygame

from src.main.classes.models.Cuadrilla import Cuadrilla
from src.main.classes.models.BoardEnum import BoardEnum
from src.main.classes.visuals.Panel import Panel
from src.main.classes.visuals.PanelCuadrilla import PanelCuadrilla


class Partida(Panel):


    def __init__(self, x, y, width, height, game_difficulty, game_index):
        super().__init__(x,y,width,height)
        self.vidas = 5
        self.errores = 0
        self.setColor(0,100,0)
        self.cuadrilla_resultado = Cuadrilla(None, None, BoardEnum[game_difficulty].value[game_index])
        self.panelResultado = PanelCuadrilla(self.cuadrilla_resultado, 0, 330, 300, 300)
        self.size = self.cuadrilla_resultado.getSize()
        self.panelResultado.setColor(0,0,0)
        self.cuadrilla_jugador = Cuadrilla(self.size[0],self.size[1],None)
        self.panelJugador = PanelCuadrilla(self.cuadrilla_jugador, 0, 0, 300, 300)
        self.panelJugador.setColor(0,0,0)


    def handleClick(self,pos):
        self.panelJugador.handleClick((pos[0]-self.x,pos[1]-self.y))

    def loseLife(self):
        self.vidas = 5 - self.errores
        if self.vidas <= 0:
            self.vidas = 0
            print(f'PERDISTE')
        print(f'tienes {self.vidas} vidas')

    def checkResult(self):
        diferencia = self.cuadrilla_resultado.checkDifference(self.cuadrilla_jugador)
        self.errores = 0
        for col in range(self.size[0]):
            for row in range(self.size[1]):
                if diferencia[col][row] == 1 and self.cuadrilla_jugador.board[col][row] != 0:
                    self.errores +=1

                    self.cuadrilla_jugador.setCell(col,row,-1)
        if self.errores>0:
            self.loseLife()

    def draw(self,dest_surface):
        super().draw(dest_surface)
        self.panelResultado.draw(self.surface)
        self.panelJugador.draw(self.surface)
        dest_surface.blit(self.surface, (self.x, self.y))

