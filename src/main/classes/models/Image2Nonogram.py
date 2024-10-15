import cv2
import os
class Image2Nonogram:
    @staticmethod
    def convertImg(img_path,width,height):
        fulldirectory = os.path.join(os.path.dirname(__file__), img_path)
        img = cv2.imread(fulldirectory, cv2.IMREAD_GRAYSCALE)
        img = cv2.resize(img, (width, height))

        img_binary_matrix = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2) // 255
        dir = os.path.join(os.path.dirname(__file__), '../../puzzles')
        file_path = os.path.join(dir, "image.txt")
        file = open(file_path,'w')
        file.write(f"{width} {height}\n")
        for r in img_binary_matrix:
            file.write(" ".join(map(str,r))+"\n")