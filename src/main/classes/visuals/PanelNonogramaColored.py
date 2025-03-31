import pygame

from main.classes.models.CuadrillaColored import CuadrillaColored
from main.classes.visuals.Panel import Panel
from main.classes.visuals.PanelCuadrillaColored import PanelCuadrillaColored
from main.classes.visuals.PanelNumeros import PanelNumeros


class PanelNonogramaColored(Panel):

    def __init__(self, x, y, width, height):
        super().__init__(x,y,width,height)
        self.setColor(0, 0, 0)
        self.path = ['Easy/Easy_Nivel1.txt','Easy/M1_Easy_Nivel1.txt']
        self.mode = 0
        self.cuadrilla_resultado = CuadrillaColored(None, None, 'main/puzzles1/' + str(self.path[0]))
        self.panel_resultado = PanelCuadrillaColored(self.cuadrilla_resultado, 0, 330, 300)
        self.board_size = self.cuadrilla_resultado.getSize()
        self.panel_resultado.setColor(0, 0, 0)
        self.cuadrilla_jugador = CuadrillaColored(self.board_size[0], self.board_size[1], None)
        self.cuadrilla_jugador.setColors(self.cuadrilla_resultado.getColors())
        self.panel_jugador = PanelCuadrillaColored(self.cuadrilla_jugador, 0, 0, 300)
        self.panel_colnums = PanelNumeros(self.cuadrilla_resultado.getColumnNums(), self.cuadrilla_resultado.getColumnColors(), 'columns', 0, 0, 700, 300)
        self.panel_rownums = PanelNumeros(self.cuadrilla_resultado.getRowNums(), self.cuadrilla_resultado.getRowColors(), 'rows', 0, 0, 30, 700)
        self.colorRect = pygame.Rect(5, 5, 20, 20)
        self.selectedColor = [[0,0,0], 0]
        self.font = pygame.font.Font(None, 18)
        self.text_surface = self.font.render(str(1), False, (0, 10, 0))
        self.marking = [False, True]

    def setNonograma(self, path, mode, custom):
        self.path[0] = path
        self.path[1] = path.split('/')
        self.path[1] = self.path[1][0]+'/M'+str(mode)+'_'+self.path[1][1]
        self.mode = mode
        if custom:
            self.cuadrilla_resultado = CuadrillaColored(None, None, 'main/puzzles_custom/'+self.path[0])
            self.board_size = self.cuadrilla_resultado.getSize()
        else:
            self.cuadrilla_resultado = CuadrillaColored(None, None, 'main/puzzles'+str(mode)+'/'+self.path[0])
            self.board_size = self.cuadrilla_resultado.getSize()
        self.cuadrilla_jugador = CuadrillaColored(self.board_size[0], self.board_size[1], 'main/saves_color/' + self.path[1])
        self.cuadrilla_jugador.setColors(self.cuadrilla_resultado.getColors())
        self.panel_jugador.setNewCuadrilla(self.cuadrilla_jugador)
        if mode >= 2:
            self.panel_jugador.setCheckResult(True)
        else:
            self.panel_jugador.setCheckResult(False)
        self.panel_resultado.setNewCuadrilla(self.cuadrilla_resultado)
        self.panel_colnums.setNewNumbers(self.cuadrilla_resultado.getColumnNums(), self.cuadrilla_resultado.getColumnColors(), 'columns')
        self.panel_rownums.setNewNumbers(self.cuadrilla_resultado.getRowNums(), self.cuadrilla_resultado.getRowColors(), 'rows')
        self.selectedColor = [self.cuadrilla_resultado.getColor(0), 1]

    def handleKey(self, event):
        self.panel_jugador.handleKey(event)
        self.selectedColor[1] = self.panel_jugador.getSelectedColor()
        self.selectedColor[0] = self.cuadrilla_jugador.getColor(self.panel_jugador.getSelectedColor()-1)
        self.text_surface = self.font.render(str(self.selectedColor[1]), False, (0, 0, 0))

    def checkAssumtion(self,pos,crossing):
        result = 0
        col, row = self.panel_jugador.positionClick(self.getBoardPosition(pos))
        jugador_cell = self.cuadrilla_jugador.checkCell(col,row)
        resultado_cell = self.cuadrilla_resultado.checkCell(col,row)
        if col != -1 and row != -1:
            if jugador_cell == 'cross':
                if not crossing and pygame.mouse.get_pressed()[0]:
                    self.cuadrilla_jugador.setCell(col, row, 0)
                return
            elif jugador_cell == 'check':
                self.cuadrilla_jugador.setCell(col, row, resultado_cell)
                return
            elif jugador_cell >= 1:
                if not self.marking[0]:
                    self.marking = [True, True]
                    self.panel_jugador.setMarking(True)
                if resultado_cell!=jugador_cell:
                    result = 1
                    self.cuadrilla_jugador.setCell(col, row, -jugador_cell)
                    self.cuadrilla_jugador.setInfo(1, self.cuadrilla_jugador.getInfo()[1]+1)
                else:
                    self.cuadrilla_jugador.setCell(col, row, jugador_cell)
                    self.cuadrilla_jugador.setInfo(0, self.cuadrilla_jugador.getInfo()[0]+1)
            elif not self.marking[0]:
                    self.marking = [True, False]
                    self.panel_jugador.setMarking(False)
            if self.mode < 2 and not self.marking[1] and jugador_cell<0:
                if resultado_cell==-jugador_cell:
                    self.cuadrilla_jugador.setInfo(0, self.cuadrilla_jugador.getInfo()[0] - 1)
                else:
                    self.cuadrilla_jugador.setInfo(1, self.cuadrilla_jugador.getInfo()[1] - 1)
                self.cuadrilla_jugador.setCell(col, row, 0)
        return result


    def setIsPressed(self, pressed):
        self.marking[0] = pressed
        self.panel_jugador.setMarking(True)

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

    def showHint(self):
        """
        Muestra una pista en el tablero. Encuentra una celda incorrecta o vacía
        y la corrige basándose en el resultado esperado.
        """
        for fila in range(self.board_size[1]):
            for col in range(self.board_size[0]):
                valor_jugador = self.cuadrilla_jugador.checkCell(col, fila)
                valor_resultado = self.cuadrilla_resultado.checkCell(col, fila)
                if valor_jugador == 'cross':
                    if valor_resultado != 0:
                        self.cuadrilla_jugador.setCell(col, fila, valor_resultado)
                        self.cuadrilla_jugador.setInfo(0, self.cuadrilla_jugador.getInfo()[0] + 1)
                        return
                elif valor_resultado != 0 and valor_jugador == 0:
                    self.cuadrilla_jugador.setCell(col, fila, valor_resultado)
                    self.cuadrilla_jugador.setInfo(0, self.cuadrilla_jugador.getInfo()[0] + 1)
                    return

    def handleClick(self,pos,crossing):
        self.panel_jugador.handleClick(self.getBoardPosition(pos),crossing,self.mode)
        if self.selectedColor[0] == [0,0,0]:
            self.selectedColor[0] = self.cuadrilla_jugador.getColor(self.panel_jugador.getSelectedColor() - 1)

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
        self.colorRect = pygame.Rect(self.w*1/32, self.h*1/32, self.w*3/16, self.h*3/16)
        self.font = pygame.font.Font(None, int(self.w/8))
        self.text_surface = self.font.render(str(self.selectedColor[1]), False, (0, 0, 0))

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
        pygame.draw.rect(self.surface, self.selectedColor[0] ,self.colorRect)
        self.surface.blit(self.text_surface, (self.w*5/49, self.h*3/36))
