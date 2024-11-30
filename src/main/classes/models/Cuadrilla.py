import os

class Cuadrilla:
    """
    Una clase que representa a una cuadrilla, que es una estructura de datos
    que puede ser utilizada para representar un tablero o matriz de valores.

    Variables:
        __col_nums (list): Lista que almacena los números seguidos de aparición de un valor en las columnas del tablero. \n
        __row_nums (list): Lista que almacena los números seguidos de aparición de un valor en las filas del tablero. \n
        __board (list): Lista bidimensional que representa el tablero. \n
        __c (int): Número de columnas en la cuadrilla. \n
        __r (int): Número de filas en la cuadrilla. \n


    Métodos:
        __init__(columns, rows, name): Inicializa la cuadrilla con las dimensiones dadas o carga una cuadrilla desde un archivo. \n
        __cleanBoard(): Limpia el tablero y lo inicializa a cero. \n
        getBoard(): Devuelve el tablero actual. \n
        getSize(): Devuelve un listado con el número de columnas y filas de la cuadrilla. \n
        setCell(c, r, value): Establece el valor de una celda específica en el tablero. \n
        __loadCuadrilla(name): Carga una cuadrilla desde un archivo dado su nombre de archivo. \n
        checkDifference(cuadrilla): Compara la cuadrilla actual con otra y devuelve una matriz indicando las diferencias. \n
        __discover_nums(): Descubre y almacena los números de filas y columnas basados en el contenido de la cuadrilla. \n
        getColumnNums(): Devuelve los números descubiertos de las columnas. \n
        getRowNums(): Devuelve los números descubiertos de las filas. \n
        checkCell(column, row): Devuelve el valor de una celda específica en la cuadrilla. \n
        print(): Imprime la representación textual del tablero en la consola.
    """
    def __init__(self, columns=None, rows=None, name = None):
        """
            Inicializa la cuadrilla. Si se proporciona un nombre, se carga la cuadrilla
            desde un archivo. De lo contrario, se inicializa un tablero vacío con las
            dimensiones especificadas.
            Args:
                columns (int): Número de columnas de la cuadrilla.
                rows (int): Número de filas de la cuadrilla.
                name (str): Nombre del archivo desde el que cargar la cuadrilla (opcional).
        """
        self.__col_nums = []
        self.__row_nums = []
        self.__board = []
        if name:
            if self.__loadCuadrilla(name) :
                self.__discover_nums()
            else:
                self.__c = 3
                self.__r = 3
                self.__board = [[1,0,1],[0,1,0],[1,0,1]]
                self.__discover_nums()
        else:
            self.__c = columns
            self.__r = rows
            self._cleanBoard()


    def _cleanBoard(self):
        """Limpia el tablero y lo inicializa a cero."""
        for i in range(self.__c):
            self.__board.append([])
            for j in range (self.__r):
                self.__board[i].append(0)

    def getBoard(self):
        """
            Devuelve el tablero actual.

            Returns:
                list: Representación bidimensional del tablero.
        """
        return self.__board

    def getSize(self):
        """
            Devuelve el tamaño de la cuadrilla.

            Returns:
                list: Lista con el número de columnas y filas [columnas, filas].
        """
        return [self.__c, self.__r]

    def setCell(self, c, r, value):
        """
            Establece el valor de una celda específica en el tablero.
            Args:
                c (int): Índice de la columna de la celda.
                r (int): Índice de la fila de la celda.
                value (int): Valor a establecer en la celda.
        """
        self.__board[c][r]=value

    def __loadCuadrilla(self,name):
        """
            Carga una cuadrilla desde un archivo dado su nombre. Se espera que el
            archivo contenga las dimensiones de la cuadrilla seguidas de los valores.
            Args:
                name (str): Nombre del archivo desde el que cargar la cuadrilla.
        """
        current_dir = os.path.dirname(os.path.abspath(__file__))
        fulldirectory = os.path.join(current_dir, '..','..', 'puzzles', name)
        try:
            archivo = open(fulldirectory,'r')
        except OSError:
            return False
        contenido = archivo.read()
        textos = contenido.split()
        self.__c = int (textos.pop(0))
        self.__r = int (textos.pop(0))
        self._cleanBoard()
        for i in range(self.__r):
            for j in range(self.__c):
                self.__board[j][i] = int(textos.pop(0))
        return True

    def checkDifference(self,cuadrilla):
        """
            Compara la cuadrilla actual con otra cuadrilla y devuelve una matriz
            indicando las diferencias entre ambas.
            Args:
                cuadrilla (Cuadrilla): La cuadrilla con la que comparar.

            Returns:
                list: Matriz indicando las diferencias de elementos (1 si son diferentes, 0 si son iguales).
            """
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
        """Descubre y almacena los números de filas y columnas basados en el contenido de la cuadrilla."""
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
        """
            Devuelve los números descubiertos de las columnas.

            Returns:
                list: Lista de números de columnas.
            """
        return self.__col_nums

    def getRowNums(self):
        return self.__row_nums

    def checkCell(self,column,row):
        """
            Devuelve el valor de una celda específica en la cuadrilla.

            Args:
                column (int): Índice de la columna de la celda.
                row (int): Índice de la fila de la celda.

            Returns:
                int: Valor de la celda especificada.
            """
        return self.__board[column][row]

    def print(self):
        """Imprime la representación textual del tablero en la consola."""
        for i in range(self.__r):
            for j in range(self.__c):
                print(self.__board[j][i], end=" ")
            print()

