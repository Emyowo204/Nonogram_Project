import pygame
import os

class Musica:
    def __init__(self, archivo, volumen = 0.5):
        self.archivo = archivo
        self.volumen = volumen
        self.play()

    def play(self):
        fulldirectory = os.path.join(os.path.dirname(__file__), self.archivo)
        pygame.mixer.music.load(fulldirectory)
        pygame.mixer.music.set_volume(self.volumen)
        pygame.mixer.music.play(-1)  # -1 = loop

    def stop(self):
        pygame.mixer.music.stop()

    def setVolumen(self, nuevoVolumen):
        self.volumen = nuevoVolumen
        pygame.mixer.music.set_volume(self.volumen)

    def getVolumen(self):
        return self.volumen

    def cambiarMusica(self, nuevoArchivo):
        self.stop()
        self.archivo = None
        self.archivo = nuevoArchivo
        self.play()