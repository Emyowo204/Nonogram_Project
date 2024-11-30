import cv2
import os

import numpy as np



class Image2Nonogram:
    """
        Clase para convertir una imagen en una matriz binaria, útil para
        crear un nonogram a partir de imágenes.

        Métodos:
            convertImg2Bin(img_path, width, height):
                Convierte una imagen en una matriz binaria y guarda el resultado en un archivo de texto.
    """
    @staticmethod
    def convertImg2Bin(img_path, width, height):

        """
            Convierte una imagen en una matriz binaria y la guarda en un archivo de texto.

            Parámetros:
                img_path (str): Ruta relativa a la imagen que se va a convertir.
                width (int): Ancho deseado de la imagen redimensionada.
                height (int): Alto deseado de la imagen redimensionada.

            Archivo de salida:
                Se guarda un archivo llamado 'image.txt' en el directorio '../../puzzles',
                que contiene el ancho y la altura de la matriz binaria seguida por los datos
                de la matriz en formato binario (0s y 1s).

            Ejemplo de uso:
                Image2Nonogram.convertImg2Bin('path/to/image.png', 10, 10)

            Excepciones:
                - Lanza un error si la imagen no se encuentra en la ruta especificada.
                - Lanza un error si hay problemas al abrir o escribir el archivo de salida.
            """

        fulldirectory = os.path.join(os.path.dirname(__file__), img_path)
        img = cv2.imread(fulldirectory, cv2.IMREAD_GRAYSCALE)
        img = cv2.resize(img, (width, height))

        img_binary_matrix = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2) // 255
        dir = os.path.join(os.path.dirname(__file__), '../../puzzles/Custom')
        file_path = os.path.join(dir, os.path.splitext(os.path.basename(img_path))[0] +".txt")
        file = open(file_path,'w')
        file.write(f"{width} {height}\n")
        for r in img_binary_matrix:
            file.write(" ".join(map(str,r))+"\n")

    @staticmethod
    def convertImg2Color(img_path, width, height):

        fulldirectory = os.path.join(os.path.dirname(__file__), img_path)
        img = cv2.imread(fulldirectory, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (width, height))
        pixels = img.reshape((-1,3))
        pixels = np.float32(pixels)

        k=4
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
        _, labels, centers = cv2.kmeans(pixels, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

        centers = np.uint8(centers)
        unique_colors = np.array(centers.tolist())
        segmented_image = centers[labels.flatten()].reshape(img.shape)

        dir = os.path.join(os.path.dirname(__file__), '../../puzzles/Colored')
        file_path = os.path.join(dir, os.path.splitext(os.path.basename(img_path))[0] + ".txt")

        file = open(file_path, 'w')
        file.write(f"{width} {height}\n")

        for r in unique_colors:
            file.write(f"{r} ")
        file.write("\n")
        for r in segmented_image:
            for pixel in r:
                index = np.where((unique_colors == pixel).all(axis=1))[0][0]+1
                file.write(f"{index} ")
            file.write("\n")

        pass