from src.main.classes.models.Cuadrilla import Cuadrilla
from src.main.classes.models.BoardEnum import BoardEnum
from src.main.classes.visuals.Panel import Panel
from src.main.classes.visuals.PanelCuadrilla import PanelCuadrilla


class Partida(Panel):


    def __init__(self, x, y, width, height, game_difficulty, game_index):
        super().__init__(x,y,width,height)
        self.vidas = 5
        self.errores = 0
        self.cuadrilla_resultado = Cuadrilla(None, None, BoardEnum[game_difficulty].value[game_index])
        self.panelResultado = PanelCuadrilla(self.cuadrilla_resultado, x, y+330, 300, 300)
        self.size = self.cuadrilla_resultado.getSize()
        self.cuadrilla_jugador = Cuadrilla(self.size[0],self.size[1],None)
        self.panelJugador = PanelCuadrilla(self.cuadrilla_jugador, x, y, 300, 300)


    def handleClick(self,pos):
        self.panelJugador.handleClick(pos)

    def loseLife(self):
        self.vidas = 5 - self.errores
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
        self.panelResultado.draw(dest_surface)
        self.panelJugador.draw(dest_surface)

