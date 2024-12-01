import os

from src.main.classes.models.Image2Nonogram import Image2Nonogram
from src.main.classes.models import Juego
from src.main.classes.models.FileManager import FileManager


def main():
    Juego.Juego().start()


if __name__ == '__main__':
    #Image2Nonogram.convertImg2Color("../../images_to_convert/benito.jpg", 30, 30)
    main()

