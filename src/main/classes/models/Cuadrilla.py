import os
class Cuadrilla:

    def __init__(self, rows=None, columns=None, name = None):
        if name:
            self.col_nums = []
            self.row_nums = []
            self.board = []
            self.__loadCuadrilla(name)
            self.discoverNums()
        else:
            self.col_nums = []
            self.row_nums = []
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
        current_dir = os.path.dirname(os.path.abspath(__file__))
        fulldirectory = os.path.join(current_dir, '..','..', 'puzzles', name)
        archivo = open(fulldirectory,'r')
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
        m_size = cuadrilla.getSize()
        if self.c != m_size[0] or self.r != m_size[1]:
            print("Size missmatch")
        else:
            output = []
            for c in range(self.c):
                output.append([])
                for r in range(self.r):
                    output[c].append(1 if(self.board[c][r]!=matrix[c][r]) else 0)
            return output

    def discoverNums(self):

        last_in_column = [0] * self.c
        last_in_row = [0] * self.r

        for i in range(self.c):
            self.col_nums.append([])
        for j in range(self.r):
            self.row_nums.append([])

        for i in range(self.c):
            for j in range(self.r):
                current_in_column = self.board[i][j]
                if current_in_column == last_in_column[i] and last_in_column[i] > 0:
                    self.col_nums[i][-1]+=1
                elif current_in_column > 0:
                    self.col_nums[i].append(1)
                last_in_column[i] = current_in_column

                current_in_row = self.board[i][j]
                if current_in_row == last_in_row[j] and last_in_row[j] > 0:
                    self.row_nums[j][-1] += 1
                elif current_in_row > 0:
                    self.row_nums[j].append(1)
                last_in_row[j] = current_in_row

    def getColumnNums(self):
        return self.col_nums

    def getRowNums(self):
        return self.row_nums

    def checkCell(self,column,row):
        return self.board[column][row]

    def print(self):
        for i in range(self.c):
            for j in range(self.r):
                print(self.board[i][j], end=" ")
            print()

