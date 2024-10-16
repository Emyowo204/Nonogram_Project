import os
class Cuadrilla:

    def __init__(self, columns=None, rows=None, name = None):
        self.__col_nums = []
        self.__row_nums = []
        self.__board = []
        if name:
            self.__loadCuadrilla(name)
            self.__discover_nums()
        else:
            self.__c = columns
            self.__r = rows
            self.__cleanBoard()


    def __cleanBoard(self):
        for i in range(self.__c):
            self.__board.append([])
            for j in range (self.__r):
                self.__board[i].append(0)

    def getBoard(self):
        return self.__board

    def getSize(self):
        return [self.__c, self.__r]

    def setCell(self, c, r, value):
        self.__board[c][r]=value

    def __loadCuadrilla(self,name):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        fulldirectory = os.path.join(current_dir, '..','..', 'puzzles', name)
        archivo = open(fulldirectory,'r')
        contenido = archivo.read()
        textos = contenido.split()
        self.__c = int (textos.pop(0))
        self.__r = int (textos.pop(0))
        self.__cleanBoard()
        for i in range(self.__r):
            for j in range(self.__c):
                self.__board[j][i] = int(textos.pop(0))

    def checkDifference(self,cuadrilla):
        matrix = cuadrilla.getBoard()
        m_size = cuadrilla.getSize()
        if self.__c != m_size[0] or self.__r != m_size[1]:
            print("Size missmatch")
        else:
            output = []
            for c in range(self.__c):
                output.append([])
                for r in range(self.__r):
                    output[c].append(1 if(self.__board[c][r] != matrix[c][r]) else 0)
            return output

    def __discover_nums(self):

        last_in_column = [0] * self.__c
        last_in_row = [0] * self.__r

        for i in range(self.__c):
            self.__col_nums.append([])
        for j in range(self.__r):
            self.__row_nums.append([])

        for i in range(self.__c):
            for j in range(self.__r):
                current_in_column = self.__board[i][j]
                if current_in_column == last_in_column[i] and last_in_column[i] > 0:
                    self.__col_nums[i][-1]+=1
                elif current_in_column > 0:
                    self.__col_nums[i].append(1)
                last_in_column[i] = current_in_column

                current_in_row = self.__board[i][j]
                if current_in_row == last_in_row[j] and last_in_row[j] > 0:
                    self.__row_nums[j][-1] += 1
                elif current_in_row > 0:
                    self.__row_nums[j].append(1)
                last_in_row[j] = current_in_row

    def getColumnNums(self):
        return self.__col_nums

    def getRowNums(self):
        return self.__row_nums

    def checkCell(self,column,row):
        return self.__board[column][row]

    def print(self):
        for i in range(self.__r):
            for j in range(self.__c):
                print(self.__board[j][i], end=" ")
            print()

