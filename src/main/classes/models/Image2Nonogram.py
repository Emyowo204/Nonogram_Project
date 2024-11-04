import cv2
import os
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
        file_path = os.path.join(dir, os.path.splitext("Custom"+os.path.basename(img_path))[0] +".txt")
        file = open(file_path,'w')
        file.write(f"{width} {height}\n")
        for r in img_binary_matrix:
            file.write(" ".join(map(str,r))+"\n")