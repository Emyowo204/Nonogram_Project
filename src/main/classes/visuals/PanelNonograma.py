import pygame

from src.main.classes.models.Cuadrilla import Cuadrilla
from src.main.classes.visuals.Panel import Panel
from src.main.classes.visuals.PanelCuadrilla import PanelCuadrilla
from src.main.classes.visuals.PanelNumeros import PanelNumeros


class PanelNonograma(Panel):

    def __init__(self, x, y, width, height):
        super().__init__(x,y,width,height)
        self.setColor(0,0,0)
        self.path = ['Easy/Easy_Nivel1.txt','Easy/M0_Hard_Nivel1.txt']
        self.mode = 0
        self.cuadrilla_resultado = Cuadrilla(None, None, 'puzzles/'+str(self.path[0]))
        self.panel_resultado = PanelCuadrilla(self.cuadrilla_resultado, 0, 330, 300)
        self.board_size = self.cuadrilla_resultado.getSize()
        self.panel_resultado.setColor(0,0,0)
        self.cuadrilla_jugador = Cuadrilla(self.board_size[0], self.board_size[1], None)
        self.panel_jugador = PanelCuadrilla(self.cuadrilla_jugador, 0, 0, 300)
        self.panel_colnums = PanelNumeros(self.cuadrilla_resultado.getColumnNums(),'columns',0,0,700,300)
        self.panel_rownums = PanelNumeros(self.cuadrilla_resultado.getRowNums(), 'rows', 0, 0, 30, 700)

    def setNonograma(self, path, mode):
        self.path[0] = path
        self.path[1] = path.split('/')
        self.path[1] = self.path[1][0]+'/M'+str(mode)+'_'+self.path[1][1]
        self.mode = mode
        self.cuadrilla_resultado = Cuadrilla(None, None, 'puzzles/'+path)
        self.board_size = self.cuadrilla_resultado.getSize()
        self.cuadrilla_jugador = Cuadrilla(self.board_size[0], self.board_size[1], 'saves/' + self.path[1])
        self.panel_jugador.setNewCuadrilla(self.cuadrilla_jugador)
        if mode >= 2:
            self.panel_jugador.setCheckResult(True)
        else:
            self.panel_jugador.setCheckResult(False)
        self.panel_resultado.setNewCuadrilla(self.cuadrilla_resultado)
        self.panel_colnums.setNewNumbers(self.cuadrilla_resultado.getColumnNums(), 'columns')
        self.panel_rownums.setNewNumbers(self.cuadrilla_resultado.getRowNums(), 'rows')

    def saveNonograma(self):
        self.cuadrilla_jugador.saveCuadrilla(str(self.path[1]))

    def resetNonograma(self):
        self.cuadrilla_jugador.resetSave(str(self.path[1]))
        self.cuadrilla_jugador.emptyBoard()

    def getInfoCuadrilla(self, choice):
        if choice == 0:
            return self.cuadrilla_jugador.getInfo()
        else:
            return self.cuadrilla_resultado.getInfo()

    def getSize(self):
        return self.board_size

    def getBoardPosition(self,pos):
        return pos[0] - self.x, pos[1] - self.y

    def handleClick(self,pos):
        self.panel_jugador.handleClick(self.getBoardPosition(pos))

    def handleZoom(self, event, pos):
        size = self.panel_resultado.getSize()
        if size[0] > 5 or  size[1] > 5:
            self.panel_jugador.handleZoom(event, (pos[0]-self.x,pos[1]-self.y))
            x_offset = self.panel_jugador.getXOffset()
            y_offset = self.panel_jugador.getYOffset()
            zoom = self.panel_jugador.getZoom()
            self.panel_rownums.handleZoom(zoom, y_offset)
            self.panel_colnums.handleZoom(zoom, x_offset)

    def defaultZoom(self):
        self.panel_jugador.defaultZoom()
        self.panel_rownums.handleZoom(1, 0)
        self.panel_colnums.handleZoom(1, 0)

    def checkAssumtion(self,pos):
        result = 0
        col, row = self.panel_jugador.positionClick(self.getBoardPosition(pos))
        jugador_cell = self.cuadrilla_jugador.checkCell(col,row)
        resultado_cell = self.cuadrilla_resultado.checkCell(col,row)
        if col != -1 and row != -1:
            if jugador_cell == 'clk':
                if resultado_cell==0:
                    result = 1
                    self.cuadrilla_jugador.setCell(col, row, -1)
                    self.cuadrilla_jugador.setInfo(1, self.cuadrilla_jugador.getInfo()[1]+1)
                else:
                    self.cuadrilla_jugador.setCell(col, row, 1)
                    self.cuadrilla_jugador.setInfo(0, self.cuadrilla_jugador.getInfo()[0]+1)
            elif self.mode < 2:
                self.cuadrilla_jugador.setCell(col, row, 0)
                if jugador_cell==-1:
                    self.cuadrilla_jugador.setInfo(1, self.cuadrilla_jugador.getInfo()[1]-1)
                else:
                    self.cuadrilla_jugador.setInfo(0, self.cuadrilla_jugador.getInfo()[0]-1)
        return result

    def fitWindow(self, w, h):
        if w < h:
            self.w = w * 8/10
            self.h = w * 8/10
        else:
            self.h = h * 8/10
            self.w = h * 8/10

        self.x = (w - self.w) / 2
        self.y = (h - self.h) / 2

        self.surface = pygame.Surface((self.w,self.h))
        self.surface.fill((self.red,self.green,self.blue))

        self.panel_colnums.setSize(self.w*6/8, self.h*2/8)
        self.panel_colnums.fitPanel(self.board_size[0])
        self.panel_colnums.setPos(self.w*2/8, 0)
        self.panel_rownums.setSize(self.w*2/8, self.h*6/8)
        self.panel_rownums.fitPanel(self.board_size[1])
        self.panel_rownums.setPos(0, self.h*2/8)

        self.panel_jugador.fitWindow(self.w*6/8)
        self.panel_jugador.setPos(self.w*2/8, self.h*2/8)
        self.panel_resultado.fitWindow(self.w*2/8)
        self.panel_resultado.setPos(0, 0)
        self.panel_jugador.defaultZoom()
        self.panel_colnums.defaultZoom()
        self.panel_rownums.defaultZoom()

    def draw(self,dest_surface):
        super().draw(dest_surface)
        self.panel_jugador.draw(self.surface)
        #self.panel_resultado.draw(self.surface)
        self.panel_colnums.draw(self.surface)
        self.panel_rownums.draw(self.surface)

