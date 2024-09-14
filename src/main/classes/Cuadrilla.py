class Cuadrilla:

    def __init__(self, rows=None, columns=None, name = None):
        if name:
            self.board = []
            self.__loadCuadrilla(name)
        else:
            self.r = rows
            self.c = columns
            self.board = []
            self._cleanBoard()


    def _cleanBoard(self):
        for i in range(self.c):
            self.board.append([])
            for j in range (self.r):
                self.board[i].append(0)

    def getBoard(self):
        return self.board

    def setCell(self, r, c, value):
        self.board[r][c]=value

    def __loadCuadrilla(self,name):
        archivo = open(f'../puzzles/{name}','r')
        contenido = archivo.read()
        textos = contenido.split()
        self.c = int (textos.pop(0))
        self.r = int (textos.pop(0))
        self._cleanBoard()
        for i in range(self.c):
            for j in range(self.r):
                index = i*self.r+j
                self.board[i][j] = int(textos[index])



    def print(self):
        for i in range(self.c):
            for j in range(self.r):
                print(self.board[i][j], end=" ")
            print()


c = Cuadrilla(None,None,'test.txt')
c.print()

