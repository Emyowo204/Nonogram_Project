import os

import pygame
import pygame_gui

from src.main.classes.models.FileManager import FileManager
from src.main.classes.models.Image2Nonogram import Image2Nonogram
from src.main.classes.visuals.BotonRect import BotonRect
from src.main.classes.visuals.ImageLoader import ImageLoader
from src.main.classes.visuals.Panel import Panel


class PanelFileManager(Panel):
    def __init__(self,x,y,width,height,juego):
        super().__init__(x,y,width,height)
        self.mode = None
        self.juego = juego
        self.filemanager = FileManager()
        self.font = pygame.font.Font(None, 20)
        self.setColor(50,50,50)

        self.btnOpciones = BotonRect(width-120, height-120, 80, 80, self.juego.mostrarPanelOpciones,None)
        self.btnOpciones.setImage(ImageLoader().getOpnNormal(), ImageLoader().getOpnShaded())
        self.btnVolver = BotonRect(40, height-120, 80, 80, juego.mostrarPanelNiveles,3)
        self.btnVolver.setImage(ImageLoader().getVolNormal(), ImageLoader().getVolShaded())

        self.firstButton = 1
        self.scaleButton = 720/18
        self.buttonsDir = []
        self.buttonsFiles = []
        self.buttonBack = None
        self.backRect = pygame.Rect(0, 0, 400, 720)

        self.manager = pygame_gui.UIManager((width, height))
        self.scrolling_container = pygame_gui.elements.UIScrollingContainer(
            relative_rect=pygame.Rect(20, 50, 0, 0), manager=self.manager
        )
        self.scrolling_container.allow_scroll_x = False

    def updateButtons(self):

        for button, _ in self.buttonsFiles:
            button.kill()
        for button, _ in self.buttonsDir:
            button.kill()
        if self.buttonBack:
            self.buttonBack.kill()

        self.buttonsDir = []
        self.buttonsFiles = []
        self.buttonBack = None

        currentdir = self.filemanager.getCurrentDir()
        y=0

        if currentdir != "/":
            button = pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect(0, y * self.scaleButton, self.scaleButton * 10, self.scaleButton),
                text="<< Back", container=self.scrolling_container, manager=self.manager
            )
            self.buttonBack = button
        y+=1
        self.filemanager.updateDir()
        folders = self.filemanager.getFolders()
        files = self.filemanager.getImages()

        for folder in folders:
            button = pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect(0, y * self.scaleButton, self.scaleButton * 10, self.scaleButton),
                text=folder, container=self.scrolling_container, manager=self.manager
            )

            self.buttonsDir.append((button, folder))
            y += 1

        for file in files:
            button = pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect(0, y * self.scaleButton, self.scaleButton * 10, self.scaleButton),
                text=file, container=self.scrolling_container, manager=self.manager
            )
            self.buttonsFiles.append((button, os.path.join(self.filemanager.getCurrentDir(),file)))
            y += 1

    def setSurface(self, surface, text, color):
        surface.fill((color, color, color))
        text_surface = self.font.render(text, False, (0, 0, 0))
        surface.blit(text_surface, (int(self.scaleButton/5), int(self.scaleButton*1/4)))
        return surface

    def setColorMode(self):
        self.mode = 'color'

    def setBinMode(self):
        self.mode = 'bin'

    def evento(self, event):
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            for button, data in self.buttonsDir:
                if event.ui_element == button:
                    self.changeDir(data)
                    self.scrolling_container.vert_scroll_bar.set_scroll_from_start_percentage(0)
            for button, data in self.buttonsFiles:
                if event.ui_element == button:
                    if self.mode == 'bin':
                        Image2Nonogram.convertImg2Bin(data,30,30)
                    elif self.mode == 'color':
                        Image2Nonogram.convertImg2Color(data, 30, 30,4)
            if event.ui_element == self.buttonBack:
                    self.changeDir("..")

        self.manager.process_events(event)
        self.btnVolver.evento(event)
        self.btnOpciones.evento(event)


    def changeDir(self, path):
        new_path = os.path.join(self.filemanager.getCurrentDir(),path)
        self.filemanager.changeDir(new_path)
        self.updateButtons()


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
        self.btnOpciones.setValues(self.w-120*multi, self.h-120*multi, 80*multi, 80*multi)
        self.btnVolver.setValues(40*multi, self.h-120*multi, 80*multi, 80*multi)
        self.manager.set_window_resolution((w,h))
        self.scrolling_container.set_dimensions((int(10*self.scaleButton+20),int(10*self.scaleButton)),True)
        self.updateButtons()

    def actualizar(self, tiempo_delta):
        """
        Actualiza el estado del gestor de UI.
        :param tiempo_delta: Delta de tiempo entre frames.
        """
        self.manager.update(tiempo_delta)

    def draw(self, dest_surface):
        super().draw(dest_surface)
        dest_surface.blit(self.surface,(0,0))
        self.btnVolver.draw(self.juego.getWindow())
        self.btnOpciones.draw(self.juego.getWindow())
        self.manager.draw_ui(dest_surface)
