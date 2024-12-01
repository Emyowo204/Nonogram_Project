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
        if name:
            if self.__loadCuadrilla(name):
                pass
                #self.__discover_nums()
            else:
                self.__c = 3
                self.__r = 3
                self.__colors = [[0,0,0], [200,200,200], [0,0,0]]
                self.__board = [[1, 0, 1], [0, 1, 0], [1, 0, 1]]
                #self.__discover_nums()
        else:
            self.__c = columns
            self.__r = rows
            self._cleanBoard()


    def _cleanBoard(self):
        """
            Limpia el tablero, lo inicializa a cero y reinicia la lista de colores.
        """
        """Limpia el tablero y lo inicializa a cero."""
        for i in range(self.__c):
            self.__board.append([])
            for j in range(self.__r):
                self.__board[i].append(0)
        self.__colors = []

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
        fulldirectory = os.path.join(current_dir, '..','..', 'puzzles', name)
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
            color_line = archivo.readline().strip()
        return True

    def setCell(self, c, r, value):
        """
            Establece el valor de una celda específica en el tablero.
            Args:
                c (int): Índice de la columna de la celda.
                r (int): Índice de la fila de la celda.
                value (int): Valor a establecer en la celda.
        """
        self.__board[c][r]=value

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
