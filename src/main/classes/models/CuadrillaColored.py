import os
from src.main.classes.models.Cuadrilla import Cuadrilla

class CuadrillaColored(Cuadrilla):
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
        super().__init__(columns, rows, name)
        self.__colors = []
        if name:
            self.__loadCuadrilla(name)

    def __cleanBoard(self):
        """
            Limpia el tablero, lo inicializa a cero y reinicia la lista de colores.
        """
        super()._Cuadrilla__cleanBoard()
        self.__colors = []

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

        self.__colors = []
        color_line = archivo.readline().strip()
        while color_line:
            colors = color_line.split(']')
            for color in colors:
                color = color.strip()
                if color.startswith('['):
                    rgb = list(map(int, color[1:].split()))
                    self.__colors.append(rgb)
            color_line = archivo.readline().strip()
        self.__cleanBoard()
        for i in range(self.__r):
            valores = list(map(int, archivo.readline().strip().split()))
            for j, value in enumerate(valores):
                self.setCell(j, i, value)
        return True

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

