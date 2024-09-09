from orca.debug import println


class Cuadrilla:

    def __init__(self, rows, columns):
        global board
        global r
        global c
        r = rows
        c = columns
        board = []
        for i in range(c):
            board.append([])
            for j in range (r):
                board[i].append(0)

    def getBoard(self):
        return board

    def setCell(self, r, c, value):
        board[r][c]=value

    def print(self):
        for i in range(c):
            for j in range(r):
                print(board[i][j], end=" ")
            print()