import pygame
import os

from main.classes.models.Logros import Logros
from main.classes.visuals.ImageLoader import ImageLoader
from main.classes.visuals.Panel import Panel
from main.classes.visuals.BotonRect import BotonRect

class PanelLogros(Panel):
    """
    Una clase que representa el Panel de Logros que se presenta al presionar el botón del panel inicial.

    Variables:
        juego (juego): El juego del cual toma referencia.
        fondoImageOG (image): Imagen original del Panel.
        fondoImage (image): Imagen del Panel con tamaño reajustado al Panel.
        normalImage (image): Variable que contiene la imagen de un botón al no estar presionado.
        shadedImage (image): Variable que contiene la imagen de un botón al tener el cursor sobre él.
        botonVolver (BotonRect): Botón que ejecuta la acción de cambiar al panel de juego.
        botonOpciones (BotonRect): Botón que ejecuta la acción de cambiar al panel de opciones.

    Métodos:
        __init__(x, y, width, height, juego): Inicializa el panel con las dimensiones dadas y el juego.
        evento(event): Administra los eventos cuando el Panel está activo (es el panel actual).
        fitWindow(w, h): Reajusta los componentes del Panel ante el cambio de tamaño de la ventana.
        draw(dest_surface): Dibuja el contenido del Panel.
    """
    def __init__(self, x, y, width, height, juego):
        """
        Inicializa el Panel.
        :param x: Posición x donde iniciará el Panel.
        :param y: Posición y donde iniciará el Panel.
        :param width: Ancho del Panel.
        :param height: Largo del Panel.
        :param juego: Juego referenciado al Panel.
        """
        super().__init__(x, y, width, height)
        self.juego = juego
        self.Og_achievements_uncompleted = []
        self.Og_achievements_completed = []
        self.achievements_uncompleted_images = []
        self.achievements_completed_images = []
        self.pos_X = []
        self.pos_Y = []
        self.ancho = 200
        self.achievements = 0
        self.achivCount = Logros().getAchievCount()

        for i in range(self.achivCount):
            self.Og_achievements_uncompleted.append(pygame.image.load('main/images/logros/nologro'+str(i+1)+'.png'))
            self.achievements_uncompleted_images.append(self.Og_achievements_uncompleted[i])
            self.Og_achievements_completed.append(pygame.image.load('main/images/logros/logro'+str(i+1)+'.png'))
            self.achievements_completed_images.append(self.Og_achievements_completed[i])
            self.pos_X.append([])
            self.pos_Y.append([])

        self.setColor(72,1,20)
        self.btnOpciones = BotonRect(width-120, height-120, 80, 80, self.juego.mostrarPanelOpciones,None)
        self.btnOpciones.setImage(ImageLoader().getOpnNormal(), ImageLoader().getOpnShaded())
        self.btnVolver = BotonRect(40, height-120, 80, 80, self.juego.mostrarPanelMenu,None)
        self.btnVolver.setImage(ImageLoader().getVolNormal(), ImageLoader().getVolShaded())

    def evento(self, event):
        """
        Maneja los eventos mientras el panel está activo.
        :param event: Objeto de evento que contiene la información relacionada al evento a procesar.
        """
        self.btnOpciones.evento(event)
        self.btnVolver.evento(event)

    def reloadAchievement(self):
        """
        Completa un logro indicado.
        :param index: índice del logro completado.
        """
        Logros().readInfoGame()
        self.achievements = Logros().getAchievements()

    def fitWindow(self, w, h):
        """
        Ajusta los componentes del Panel según el tamaño actual de la ventana.
        :param w: Nuevo ancho de la ventana.
        :param h: Nuevo largo de la ventana.
        """
        if w < h :
            multi = w / 720
        else :
            multi = h / 720

        self.w = w
        self.h = h
        self.surface = pygame.Surface((self.w,self.h))
        self.surface.fill((self.red,self.green,self.blue))

        self.ancho = 300*multi

        for i in range(self.achivCount):
            self.achievements_completed_images[i] = pygame.transform.scale(self.Og_achievements_completed[i], (self.ancho, self.ancho/3))
            self.achievements_uncompleted_images[i] = pygame.transform.scale(self.Og_achievements_uncompleted[i],(self.ancho, self.ancho/3))
            if i%2==0:
                self.pos_X[i]=(self.w/2-self.ancho-self.w/16)
            else:
                self.pos_X[i]=(self.w/2+self.w/16)
            if i < 2:
                self.pos_Y[i]=(self.h*1/20)
            elif i < 4:
                self.pos_Y[i]=(self.h*2/20+self.ancho/3)
            elif i < 6:
                self.pos_Y[i]=(self.h*3/20+self.ancho*2/3)
            elif i < 8:
                self.pos_Y[i]=(self.h*4/20+self.ancho*3/3)
            else:
                self.pos_Y[i]=(self.h*5/20+self.ancho*4/3)

        self.btnOpciones.setValues(self.w-120*multi, self.h-120*multi, 80*multi, 80*multi)
        self.btnVolver.setValues(40*multi, self.h-120*multi, 80*multi, 80*multi)


    def draw(self, dest_surface):
        """
        Dibuja los componentes correspondientes en la ventana.
        :param dest_surface: Superficie en la que se dibujará el Panel.
        """
        super().draw(dest_surface)
        for i in range(self.achivCount):
            if (self.achievements & (1<<i)) == 0:
                dest_surface.blit(self.achievements_uncompleted_images[i], (self.pos_X[i], self.pos_Y[i]))
            else:
                dest_surface.blit(self.achievements_completed_images[i],(self.pos_X[i], self.pos_Y[i]))


        self.btnOpciones.draw(self.juego.getWindow())
        self.btnVolver.draw(self.juego.getWindow())

