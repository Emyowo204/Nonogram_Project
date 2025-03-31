import os

import pygame
import pygame_gui

from main.classes.models.FileManager import FileManager
from main.classes.visuals.ImageLoader import ImageLoader
from main.classes.visuals.Panel import Panel
from main.classes.visuals.BotonRect import BotonRect

class PanelNivelesCustom(Panel):

    def __init__(self, x, y, width, height, juego):
        super().__init__(x, y, width, height)

        self.juego = juego
        self.filemanager = FileManager()
        self.font = pygame.font.Font(None, 20)
        self.setColor(50, 50, 50)

        self.fondoImageOG = pygame.image.load('main/images/fondoMenuTest.png')
        self.fondoImage = pygame.transform.scale(self.fondoImageOG, (width, height))

        self.scaleButton = 720 / 18
        self.buttonsFiles = []

        self.btnLoadImg = BotonRect(self.w/2-80, self.h-120, 160, 80, self.juego.mostrarPanelFileManager, None)
        self.btnLoadImg.setImage(pygame.image.load('main/images/btnImg2NonoNormal.png'), pygame.image.load('main/images/btnImg2NonoShaded.png'))

        self.btnOpciones = BotonRect(width-120, height-120, 80, 80, self.juego.mostrarPanelOpciones,None)
        self.btnOpciones.setImage(ImageLoader().getOpnNormal(), ImageLoader().getOpnShaded())
        self.btnVolver = BotonRect(40, height-120, 80, 80, self.juego.mostrarPanelMenu,None)
        self.btnVolver.setImage(ImageLoader().getVolNormal(), ImageLoader().getVolShaded())

        self.multi = 1

        self.manager = pygame_gui.UIManager((width, height))
        self.scrolling_container = pygame_gui.elements.UIScrollingContainer(
            relative_rect=pygame.Rect(20, 50, 0, 0), manager=self.manager
        )
        self.scrolling_container.allow_scroll_x = False


    def setLoadEnable(self, enabled):
        self.btnLoadImg.setEnable(enabled)

    def setColorMode(self):
        new_path = os.path.join(os.getcwd(),"main/puzzles_custom/Custom1")
        self.filemanager.changeDir(new_path)
        self.updateButtons()


    def setBinMode(self):
        new_path = os.path.join(os.getcwd(),"main/puzzles_custom/Custom0")
        self.filemanager.changeDir(new_path)
        self.updateButtons()


    def updateButtons(self):

        for button, _ in self.buttonsFiles:
            button.kill()

        self.buttonsFiles = []

        y=0
        self.filemanager.updateDir()
        files = self.filemanager.getPuzzles()

        for index, file in enumerate(files, start=1):
            button = pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect(0, y * self.scaleButton, self.scaleButton * 10, self.scaleButton),
                text=file, container=self.scrolling_container, manager=self.manager
            )
            self.buttonsFiles.append((button, index))
            y += 1

    def evento(self, event):

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            for button, data in self.buttonsFiles:
                if event.ui_element == button:
                    self.juego.mostrarPanelCuadrilla(data)

        self.btnLoadImg.evento(event)
        self.btnVolver.evento(event)
        self.btnOpciones.evento(event)
        self.manager.process_events(event)

    def fitWindow(self, w, h):
        if w < h :
            multi = w / 720
        else :
            multi = h / 720

        self.w = w
        self.h = h
        self.fondoImage = pygame.transform.scale(self.fondoImageOG, (self.w, self.h))
        self.scaleButton = int(h / 18)
        self.surface = pygame.Surface((self.w,self.h))
        self.surface.fill((self.red,self.green,self.blue))

        self.btnLoadImg.setValues(self.w/2-80*multi, self.h-120*multi, 160*multi, 80*multi)
        self.btnOpciones.setValues(self.w - 120 * multi, self.h - 120 * multi, 80 * multi, 80 * multi)
        self.btnVolver.setValues(40 * multi, self.h - 120 * multi, 80 * multi, 80 * multi)
        self.manager.set_window_resolution((w, h))

        if 10*self.scaleButton >= 10:
            self.scrolling_container.set_dimensions((int(10*self.scaleButton+20),int(10*self.scaleButton)),True)
            self.scrolling_container.set_position((self.w/2 - int(10*self.scaleButton+20)/2, self.scaleButton))

        self.multi = multi
        self.updateButtons()

    def actualizar(self, tiempo_delta):
        """
        Actualiza el estado del gestor de UI.
        :param tiempo_delta: Delta de tiempo entre frames.
        """
        self.manager.update(tiempo_delta)


    def draw(self, dest_surface):
        super().draw(dest_surface)
        dest_surface.blit(self.fondoImage, (0, 0))

        if self.btnLoadImg.isEnabled():
            self.btnLoadImg.draw(self.juego.getWindow())
        self.btnVolver.draw(self.juego.getWindow())
        self.btnOpciones.draw(self.juego.getWindow())
        self.manager.draw_ui(dest_surface)

