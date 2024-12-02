import pygame
import os

class Sonido:
    """
    Clase que representa sonidos del juego.

    Variables:
        archivo (string): Ubicación del archivo de sonido que se inicializará.
        volumen (float): Valor del volumen del sonido.

    Métodos:
        __init__(archivo, volumen): Inicializa el sonido.
        play(): Reproduce el sonido.
        setVolumen(): Designa el valor del volumen.
        getVolumen(): Retorna el valor del volumen.
    """
    def __init__(self, archivo, volumen = 0.5):
        """
        Inicializa la música del Panel.
        :param archivo: Ubicacion del archivo de música para ser designada.
        :param volumen: Valor del volumen de la música para ser designado.
        """
        fulldirectory = os.path.join(os.path.dirname(__file__), archivo)
        self.sonido = pygame.mixer.Sound(fulldirectory)
        self.volumen = volumen

    def play(self, archivo):
        """
        Reproduce la canción de la ubicación que esté actualmente almacenada en archivo al volumen
        almacenado en volumen.
        """
        fulldirectory = os.path.join(os.path.dirname(__file__), archivo)
        self.sonido = pygame.mixer.Sound(fulldirectory)
        self.sonido.set_volume(self.volumen)
        self.sonido.play()

    def setVolumen(self, nuevoVolumen):
        """
        Designa el valor que se entregue a la variable volumen.
        :param nuevoVolumen: Nuevo volumen que se quiere designar.
        """
        self.volumen = nuevoVolumen
        self.sonido.set_volume(self.volumen)

    def getVolumen(self):
        """
        Metodo getter, obtiene el volumen actual.
        :return: El valor actual del volumen.
        """
        return self.volumen
