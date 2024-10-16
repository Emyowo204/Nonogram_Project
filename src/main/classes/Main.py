from src.main.classes.models.Image2Nonogram import Image2Nonogram
from src.main.classes.visuals import Juego


def main(mode,index):
    Juego.Juego().start(mode,index)


if __name__ == '__main__':
    Image2Nonogram.convertImg("../../images_to_convert/benitowb.png",30,30)
    #temporal main("IMAGE", 0) juega con una imagen de un gato ("TEST, X") con X = 0,1,2,3 juega con test de cuadrillas
    main("IMAGE",0)
