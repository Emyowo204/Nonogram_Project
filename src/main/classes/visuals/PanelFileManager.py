import pygame
from src.main.classes.models.FileManager import FileManager
from src.main.classes.models.Image2Nonogram import Image2Nonogram
from src.main.classes.visuals.BotonRect import BotonRect
from src.main.classes.visuals.Panel import Panel


class PanelFileManager(Panel):
    def __init__(self,x,y,width,height):
        super().__init__(x,y,width,height)
        self.filemanager = FileManager()
        self.font = pygame.font.Font(None, 20)
        self.surface.fill((50,50,50))


    def updateButtons(self):
        self.container = []
        currentdir = self.filemanager.getCurrentDir()
        y=0
        if currentdir != "/":
            surface = pygame.Surface((400, 40))
            surface.fill((255, 255, 255))
            text_surface = self.font.render("..", False, (0, 0, 0))
            surface.blit(text_surface, (0, 0))
            button = BotonRect(0,y*40,400,40,self.filemanager.enterPath,"..")
            button.setImage(text_surface,text_surface)
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
            button = BotonRect(0, y*40, 400, 40, self.filemanager.enterPath, folder)
            button.setImage(surface, surface)
            self.add(button)
            y += 1

        for file in files:
            surface = pygame.Surface((400, 40))
            surface.fill((255, 255, 255))
            text_surface = self.font.render(file, False, (0, 0, 0))
            surface.blit(text_surface, (0, 0))
            button = BotonRect(0, y*40, 400, 40, Image2Nonogram.convertImg2Bin, (file,30,30))
            button.setImage(text_surface, text_surface)
            self.add(button)
            y += 1

    def draw(self, dest_surface):
        super().draw(dest_surface)
        dest_surface.blit(self.surface,(0,0))







