import pygame
import os

class Musica:
    """
    Clase que representa la música del juego.
    Modificable y única en el juego.

    Variables:
        archivo (string): Ubicación del archivo de música que se inicializará.
        volumen (float): Valor del volumen de la música.

    Métodos:
        __init__(archivo, volumen): Inicializa la música.
        play(): Reproduce la música.
        setVolumen(): Designa el valor del volumen.
        getVolumen(): Retorna el valor del volumen.
        cambiarMusica(): Cambia el volumen de la musica con el volumen entregado.
    """
    def __init__(self, archivo, volumen = 0.5):
        """
        Inicializa la música del Panel.
        :param archivo: Ubicacion del archivo de música para ser designada.
        :param volumen: Valor del volumen de la música para ser designado.
        """
        self.archivo = archivo
        self.volumen = volumen
        self.play()

    def play(self):
        """
        Reproduce la canción de la ubicación que esté actualmente almacenada en archivo al volumen
        almacenado en volumen.
        """
        if self.archivo == None:
            pygame.mixer.music.stop()
            return
        fulldirectory = os.path.join(os.path.dirname(__file__), self.archivo)
        pygame.mixer.music.load(fulldirectory)
        pygame.mixer.music.set_volume(self.volumen)
        pygame.mixer.music.play(-1)  # -1 = loop

    def setVolumen(self, nuevoVolumen):
        """
        Designa el valor que se entregue a la variable volumen.
        :param nuevoVolumen: Nuevo volumen que se quiere designar.
        """
        self.volumen = nuevoVolumen
        pygame.mixer.music.set_volume(self.volumen)

    def getVolumen(self):
        """
        Metodo getter, obtiene el volumen actual.
        :return: El valor actual del volumen.
        """
        return self.volumen

    def cambiarMusica(self, nuevoArchivo):
        """
        Cambia la ubicación en la variable archivo a otra para poder cambiar la música.
        :param nuevoArchivo: Ubicación de la nueva canción a reproducir.
        """
        pygame.mixer.music.stop()
        self.archivo = nuevoArchivo
        self.play()