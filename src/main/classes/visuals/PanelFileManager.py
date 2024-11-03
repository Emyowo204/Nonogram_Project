import os

import pygame
from pygame.tests.test_utils.png import Image

from src.main.classes.models.FileManager import FileManager
from src.main.classes.models.Image2Nonogram import Image2Nonogram
from src.main.classes.visuals.BotonRect import BotonRect
from src.main.classes.visuals.ImageLoader import ImageLoader
from src.main.classes.visuals.Panel import Panel


class PanelFileManager(Panel):
    def __init__(self,x,y,width,height,juego):
        super().__init__(x,y,width,height)
        self.juego = juego
        self.filemanager = FileManager()
        self.font = pygame.font.Font(None, 20)
        self.surface.fill((50,50,50))


    def updateButtons(self):
        self.surface.fill((50,50,50))
        self.container = []
        currentdir = self.filemanager.getCurrentDir()
        y=0
        if currentdir != "/":
            surface = pygame.Surface((400, 40))
            surface.fill((255, 255, 255))
            text_surface = self.font.render("..", False, (0, 0, 0))
            surface.blit(text_surface, (0, 0))
            button = BotonRect(0,y*40,400,40,self.changeDir,"..")
            button.setImage(surface,ImageLoader().getDefaultImage())
            self.add(button)
            y += 1

        self.filemanager.updateFoldersAndImages()
        folders = self.filemanager.getFolders()
        files = self.filemanager.getImages()

        for folder in folders:
            surface = pygame.Surface((400,40))
            surface.fill((255,255,255))
            text_surface = self.font.render(folder, False, (0, 0, 0))
            surface.blit(text_surface,(0,0))
            button = BotonRect(0, y*40, 400, 40, self.changeDir, folder)
            button.setImage(surface, ImageLoader().getDefaultImage())
            self.add(button)
            y += 1

        for file in files:
            surface = pygame.Surface((400, 40))
            surface.fill((255, 255, 255))
            text_surface = self.font.render(file, False, (0, 0, 0))
            surface.blit(text_surface, (0, 0))
            button = BotonRect(0, y*40, 400, 40, Image2Nonogram.convertImg2Bin, (file,30,30))
            button.setImage(text_surface, ImageLoader().getDefaultImage())
            self.add(button)
            y += 1

    def evento(self, event):
        for button in self.container:
            button.evento(event)

    def changeDir(self, path):
        new_path = os.path.join(self.filemanager.getCurrentDir(),path)
        self.filemanager.enterPath(new_path)
        self.updateButtons()
        print(path)


    def draw(self, dest_surface):
        super().draw(dest_surface)
        dest_surface.blit(self.surface,(0,0))







