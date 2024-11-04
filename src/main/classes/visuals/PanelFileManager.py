import os

import pygame
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
        self.setColor(50,50,50)
        self.btnVolver = BotonRect(width * 12 / 16, height * 15 / 16, 170, 35, juego.mostrarPanelMenu,None)
        self.btnVolver.setImage(ImageLoader().getVolNormal(), ImageLoader().getVolShaded())
        self.firstButton = 1
        self.scaleButton = 720/18
        self.btnMoveUp = BotonRect(400,0, 40, 40, self.moveButtons,4)
        self.btnMoveUp.setImage(pygame.image.load('../images/btnUpNormal.png'), pygame.image.load('../images/btnUpShaded.png'))
        self.btnMoveDown = BotonRect(400, 680, 40, 40, self.moveButtons, -4)
        self.btnMoveDown.setImage(pygame.image.load('../images/btnDownNormal.png'), pygame.image.load('../images/btnDownShaded.png'))
        self.buttonsDir = []
        self.buttonBack = None
        self.backRect = pygame.Rect(0, 0, 400, 720)

    def updateButtons(self):
        self.surface.fill((50,50,50))
        self.buttonsDir = []
        currentdir = self.filemanager.getCurrentDir()
        y=self.firstButton
        surfNormal = pygame.Surface((self.scaleButton*10, self.scaleButton))
        surfShaded = pygame.Surface((self.scaleButton*10, self.scaleButton))
        self.font = pygame.font.Font(None, int(self.scaleButton/2))
        self.backRect.update(0, 0, self.scaleButton*10, self.w)

        if currentdir != "/":
            self.buttonBack = BotonRect(0, 0, self.scaleButton * 10, self.scaleButton, self.changeDir, "..")
            self.buttonBack.setImage(self.setSurface(surfNormal,"<< Back",225), self.setSurface(surfShaded,"<< Back",180))

        self.filemanager.updateDir()
        folders = self.filemanager.getFolders()
        files = self.filemanager.getImages()

        for folder in folders:
            button = BotonRect(0, y*self.scaleButton, self.scaleButton*10, self.scaleButton, self.changeDir, folder)
            button.setImage(self.setSurface(surfNormal,folder,255), self.setSurface(surfShaded,folder,200))
            self.buttonsDir.append(button)
            y += 1

        for file in files:
            button = BotonRect(0, y*self.scaleButton, self.scaleButton*10, self.scaleButton, Image2Nonogram.convertImg2Bin, os.path.join(self.filemanager.getCurrentDir(),file),30,30)
            button.setImage(self.setSurface(surfNormal,file,255), self.setSurface(surfShaded,file,200))
            self.buttonsDir.append(button)
            y += 1

    def setSurface(self, surface, text, color):
        surface.fill((color, color, color))
        text_surface = self.font.render(text, False, (0, 0, 0))
        surface.blit(text_surface, (int(self.scaleButton/5), int(self.scaleButton*1/4)))
        return surface

    def evento(self, event):
        for button in self.buttonsDir:
            button.evento(event)
        self.buttonBack.evento(event)
        self.btnVolver.evento(event)
        self.btnMoveUp.evento(event)
        self.btnMoveDown.evento(event)

    def changeDir(self, path):
        new_path = os.path.join(self.filemanager.getCurrentDir(),path)
        self.filemanager.changeDir(new_path)
        self.firstButton = 1
        self.updateButtons()

    def moveButtons(self,start):
        self.surface = pygame.Surface((self.w,self.h))
        self.surface.fill((self.red,self.green,self.blue))
        if self.firstButton+start>1 or len(self.buttonsDir)<18:
            self.firstButton = 1
        elif self.firstButton+start<-len(self.buttonsDir)+18:
            self.firstButton = -len(self.buttonsDir)+18
        else:
            self.firstButton+=start
        y = self.firstButton
        for button in self.buttonsDir:
            button.setCoord(0,y*self.scaleButton)
            y+=1
            if y*self.scaleButton <= self.scaleButton:
                button.setEnable(False)
            else:
                button.setEnable(True)

    def fitWindow(self, w, h):
        if w < h :
            multi = w / 720
        else :
            multi = h / 720
        self.w = w
        self.h = h
        self.surface = pygame.Surface((self.w,self.h))
        self.surface.fill((self.red,self.green,self.blue))
        self.scaleButton = int(h / 18)
        self.btnVolver.setValues((self.w-180*multi), (self.h-45*multi), 170*multi, 35*multi)
        self.btnMoveUp.setValues(self.scaleButton*10, 0, 40*multi, 40*multi)
        self.btnMoveDown.setValues(self.scaleButton*10, self.h-40*multi, 40*multi, 40*multi)
        self.updateButtons()

    def draw(self, dest_surface):
        super().draw(dest_surface)
        dest_surface.blit(self.surface,(0,0))
        pygame.draw.rect(dest_surface, (250, 250, 250), self.backRect)
        for button in self.buttonsDir:
            button.draw(self.juego.getWindow())
        self.buttonBack.draw(self.juego.getWindow())
        self.btnVolver.draw(self.juego.getWindow())
        self.btnMoveUp.draw(self.juego.getWindow())
        self.btnMoveDown.draw(self.juego.getWindow())
