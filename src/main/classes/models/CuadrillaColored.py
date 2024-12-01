import os
from src.main.classes.models.Cuadrilla import Cuadrilla

class CuadrillaColored:
    """
        Clase que extiende Cuadrilla para manejar nonogramas de colores.
        En lugar de trabajar con valores binarios (0s y 1s), esta clase trabaja
        con valores múltiples (0s, 1s, 2s, 3s) representando diferentes colores.

        Métodos:
            __init__: Inicializa la cuadrilla para colores.
            loadColors: Carga una cuadrilla de colores desde un archivo.
            getColors: Devuelve los colores utilizados en la cuadrilla.
            print: Imprime la cuadrilla con los colores codificados.
    """

    def __init__(self, columns=None, rows=None, name=None):
        """
            Inicializa una cuadrilla de colores.
            Args:
                columns (int): Número de columnas.
                rows (int): Número de filas.
                name (str): Nombre del archivo desde donde cargar la cuadrilla (opcional).
        """
        self.__col_nums = []
        self.__row_nums = []
        self.__colors = []
        self.__board = []
        self.__c = columns
        self.__r = rows
        self.__info = [0, 0]
        if name:
            if self.__loadCuadrilla(name) :
                self.__discover_nums()
            else:
                self._cleanBoard()
                self.__discover_nums()
        else:
            self._cleanBoard()


    def _cleanBoard(self):
        """
            Limpia el tablero, lo inicializa a cero y reinicia la lista de colores.
        """
        """Limpia el tablero y lo inicializa a cero."""
        self.__info = [0, 0]
        for i in range(self.__c):
            self.__board.append([])
            for j in range(self.__r):
                self.__board[i].append(0)
        self.__colors = []

    def emptyBoard(self):
        """Limpia el tablero y lo inicializa a cero."""
        self.__info = [0, 0]
        for i in range(self.__c):
            for j in range (self.__r):
                self.__board[i][j]=0

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
            archivo contenga las dimensiones de la cuadrilla seguidas de los valores
            rgb de los colores de los que está compuesto la cuadrilla, y finalmente
            los valores en la matriz.
            Args:
                name (str): Nombre del archivo desde el que cargar la cuadrilla.
        """
        current_dir = os.path.dirname(os.path.abspath(__file__))
        fulldirectory = os.path.join(current_dir, '..','..', name)
        try:
            archivo = open(fulldirectory,'r')
        except OSError:
            return False
        dimensions = archivo.readline().strip().split()
        self.__c = int(dimensions[0])
        self.__r = int(dimensions[1])
        self._cleanBoard()
        color_line = archivo.readline().strip()

        colors = color_line.split(']')
        for color in colors:
            color = color.strip()
            if color.startswith('['):
                rgb = list(map(int, color[1:].split()))
                self.__colors.append(rgb)

        color_line = archivo.readline().strip()
        while color_line:
            for i in range(self.__r):
                valores = list(map(int, archivo.readline().strip().split()))
                for j, value in enumerate(valores):
                    self.setCell(j, i, value)
                    if self.__board[j][i] == -1:
                        self.__info[1] += 1
                    elif self.__board[j][i] != 0:
                        self.__info[0] += 1
            color_line = archivo.readline().strip()
        archivo.close()
        return True

    def saveCuadrilla(self, name):
        """
            Carga una cuadrilla desde un archivo dado su nombre. Se espera que el
            archivo contenga las dimensiones de la cuadrilla seguidas de los valores.
        """
        current_dir = os.path.dirname(os.path.abspath(__file__))
        fulldirectory = os.path.join(current_dir, '..','..', 'saves_color', str(name))
        try:
            archivo = open(fulldirectory,'w')
        except OSError:
            return False
        archivo.write(f"{self.__c} {self.__r}\n")
        for colors in self.__colors:
            archivo.write(f"[")
            for color in colors:
                archivo.write(f"{color} ")
            archivo.write(f"]")
        archivo.write(f"\n")
        for i in range(self.__r):
            for j in range(self.__c):
                archivo.write(f"{self.__board[j][i]} ")
            archivo.write(f"\n")
        archivo.close()
        return True

    def resetSave(self, name):
        self.__info[1] = 0
        current_dir = os.path.dirname(os.path.abspath(__file__))
        fulldirectory = os.path.join(current_dir, '..','..', 'saves_color', str(name))
        try:
            archivo = open(fulldirectory,'w')
        except OSError:
            return False
        archivo.write(f"{self.__c} {self.__r}\n")
        for color in self.__colors:
            archivo.write(f"{color} \n")
        for i in range(self.__r):
            for j in range(self.__c):
                archivo.write(f"{0} ")
            archivo.write(f"\n")
        archivo.close()
        return True

    def checkDifference(self, cuadrilla):
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
                    output[c].append(1 if (self.__board[c][r] != matrix[c][r]) else 0)
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
                    self.__col_nums[i][-1] += 1
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

    def getInfo(self):
        return self.__info

    def setInfo(self, index, value):
        self.__info[index] = value

    def checkCell(self, column, row):
        """
            Devuelve el valor de una celda específica en la cuadrilla.

            Args:
                column (int): Índice de la columna de la celda.
                row (int): Índice de la fila de la celda.

            Returns:
                int: Valor de la celda especificada.
            """
        return self.__board[column][row]

    def getColor(self, index):
        """
            Devuelve el color asociado al índice dado.
            Args:
                index (int): Índice del color en la lista de colores.
            Returns:
                list: El color en formato [R,G,B], o None si el índice no es válido.
        """
        if 0 <= index < len(self.__colors):
            return self.__colors[index]
        return None

    def getColors(self):
        """
            Devuelve la lista completa de colores únicos.
            Returns:
                list: Lista de colores en formato [R,G,B].
        """
        return self.__colors

    def setColors(self, colors):
        self.__colors = colors

    def print(self):
        """Imprime la representación textual del tablero en la consola."""
        for i in range(self.__r):
            for j in range(self.__c):
                print(self.__board[j][i], end=" ")
            print()
