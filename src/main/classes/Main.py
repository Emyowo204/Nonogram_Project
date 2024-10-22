from src.main.classes.models.Image2Nonogram import Image2Nonogram
from src.main.classes.visuals import Juego


def main():
    Juego.Juego().start()


if __name__ == '__main__':
    Image2Nonogram.convertImg2Bin("../../images_to_convert/benitowb.png", 30, 30)
    main()
