from src.main.classes.models.Cuadrilla import Cuadrilla
from src.main.classes.models.BoardEnum import BoardEnum

class Partida:


    def __init__(self,size,game_difficulty, game_index):
        self.cuadrilla_jugador = Cuadrilla(size,size,None)
        self.cuadrilla_resultado = Cuadrilla(None,None,BoardEnum[game_difficulty][game_index])

