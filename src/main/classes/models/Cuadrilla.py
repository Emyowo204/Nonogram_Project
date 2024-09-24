class Cuadrilla:

    def __init__(self, rows=None, columns=None, name = None):
        if name:
            self.board = []
            self.__loadCuadrilla(name)
        else:
            self.c = columns
            self.r = rows
            self.board = []
            self._cleanBoard()


    def _cleanBoard(self):
        for i in range(self.c):
            self.board.append([])
            for j in range (self.r):
                self.board[i].append(0)

    def getBoard(self):
        return self.board

    def getSize(self):
        return [self.c,self.r]

    def setCell(self, c, r, value):
        self.board[c][r]=value

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

    def checkDifference(self,cuadrilla):
        matrix = cuadrilla.getBoard()
        mSize = cuadrilla.getSize()
        if self.c != mSize[0] or self.r != mSize[1]:
            print("Size missmatch")
        else:
            output = []
            for c in range(self.c):
                output.append([])
                for r in range(self.r):
                    output[c].append(1 if(self.board[c][r]!=matrix[c][r]) else 0)
            return output



    def print(self):
        for i in range(self.c):
            for j in range(self.r):
                print(self.board[i][j], end=" ")
            print()

