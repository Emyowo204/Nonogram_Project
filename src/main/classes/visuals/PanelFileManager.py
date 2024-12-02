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

        self.fondoImageOG = pygame.image.load('../images/fondoopciones.jpg')
        self.fondoImage = pygame.transform.scale(self.fondoImageOG, (width, height))

        self.btnOpciones = BotonRect(width-120, height-120, 80, 80, self.juego.mostrarPanelOpciones,None)
        self.btnOpciones.setImage(ImageLoader().getOpnNormal(), ImageLoader().getOpnShaded())
        self.btnVolver = BotonRect(40, height-120, 80, 80, juego.mostrarPanelNiveles,3)
        self.btnVolver.setImage(ImageLoader().getVolNormal(), ImageLoader().getVolShaded())

        self.firstButton = 1
        self.scaleButton = 720/18
        self.buttonsDir = []
        self.buttonsFiles = []
        self.buttonBack = None

        self.current_imgbtn = None
        self.current_img = None
        self.scaled_img = None
        self.img_size = None
        self.scaled_size = None

        self.manager = pygame_gui.UIManager((width, height))
        self.scrolling_container = pygame_gui.elements.UIScrollingContainer(
            relative_rect=pygame.Rect(20, 50, 0, 0), manager=self.manager
        )
        self.scrolling_container.allow_scroll_x = False

        self.entry_w = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect((self.w/2-200, self.h-50-50), (200, 50)),
            manager=self.manager
        )
        self.entry_w.set_allowed_characters(["0","1","2","3","4","5","6","7","8","9"])
        self.entry_w.placeholder_text = "Width"
        self.entry_w.unfocus()

        self.entry_h = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect((self.w / 2, self.h - 50 - 50), (200, 50)),
            manager=self.manager
        )
        self.entry_h.set_allowed_characters(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
        self.entry_h.placeholder_text = "Height"
        self.entry_h.unfocus()

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
                w_text = self.entry_w.get_text()
                h_text = self.entry_h.get_text()
                if event.ui_element == button and h_text.isdigit() and w_text.isdigit():
                    if int(w_text) > 4 and int(h_text) > 4:
                        if self.mode == 'bin':
                            Image2Nonogram.convertImg2Bin(data,int(w_text),int(h_text))
                        elif self.mode == 'color':
                            Image2Nonogram.convertImg2Color(data, int(w_text),int(h_text),4)
            if event.ui_element == self.buttonBack:
                    self.changeDir("..")

        if event.type == pygame_gui.UI_BUTTON_ON_HOVERED:
            for button, data in self.buttonsFiles:
                if event.ui_element == button and button != self.current_imgbtn:
                    try:
                        self.current_imgbtn = button
                        self.current_img = pygame.image.load(data)
                        self.img_size = self.current_img.get_size()
                        scale = abs((int(12*self.scaleButton)-(self.h - 50 - 50))/self.img_size[1])
                        self.scaled_size = (scale*self.img_size[0],scale*self.img_size[1])
                        self.scaled_img = pygame.transform.scale(self.current_img,self.scaled_size)
                    except pygame.error:
                        self.current_img = None

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
        self.fondoImage = pygame.transform.scale(self.fondoImageOG, (self.w, self.h))
        self.scaleButton = int(h / 18)
        self.btnOpciones.setValues(self.w-120*multi, self.h-120*multi, 80*multi, 80*multi)
        self.btnVolver.setValues(40*multi, self.h-120*multi, 80*multi, 80*multi)
        self.manager.set_window_resolution((w,h))
        if 10*self.scaleButton >= 10:
            self.scrolling_container.set_dimensions((int(10*self.scaleButton+20),int(10*self.scaleButton)),True)
            self.scrolling_container.set_position((self.w/2 - int(10*self.scaleButton+20)/2, self.scaleButton))
            self.entry_w.set_position((self.w/2-5 * self.scaleButton, self.h-50-50))
            self.entry_w.set_dimensions((5 * self.scaleButton,self.scaleButton))
            self.entry_h.set_position((self.w / 2 , self.h - 50 - 50))
            self.entry_h.set_dimensions((5 * self.scaleButton, self.scaleButton))
            if self.current_img is not None:
                try:
                    scale = abs((int(12 * self.scaleButton) - (self.h - 50 - 50)) / self.img_size[1])
                    self.scaled_size = (scale * self.img_size[0], scale * self.img_size[1])
                    self.scaled_img = pygame.transform.scale(self.current_img, self.scaled_size)
                except pygame.error:
                    self.current_img = None
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
        if self.scaled_img is not None:
            dest_surface.blit(self.scaled_img,(self.w/2-self.scaled_size[0]/2,int(11*self.scaleButton)))
        self.btnVolver.draw(self.juego.getWindow())
        self.btnOpciones.draw(self.juego.getWindow())
        self.manager.draw_ui(dest_surface)