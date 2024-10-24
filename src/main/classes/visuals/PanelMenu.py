import pygame

from src.main.classes.visuals.Panel import Panel
from src.main.classes.visuals.BotonRect import BotonRect

class PanelMenu(Panel):
    """
    Una clase que representa el Panel de Menu Principal que se presenta al iniciar la aplicación.

    Variables:
        juego (juego): El juego del cual toma referencia.
        fondoImageOG (image): Imagen original del Panel.
        fondoImage (image): Imagen del Panel con tamaño reajustado al Panel.
        normalImage (image): Variable que contiene la imagen de un botón al no estar presionado.
        shadedImage (image): Variable que contiene la imagen de un botón al tener el cursor sobre él.
        botonJugar (BotonRect): Botón que ejecuta la acción de cambiar al panel de juego.
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
        self.fondoImageOG = pygame.image.load('../images/fondoMenuTest.png')
        self.fondoImage = pygame.transform.scale(self.fondoImageOG, (width, height))
        self.btnJugar = BotonRect(width*1/4, height*2/8, 360, 90, self.toggleMainMenu,None)
        self.btnJugar.setImage(pygame.image.load('../images/botonJugar.png'),pygame.image.load('../images/botonJugarShaded.png'))
        self.btnOpciones = BotonRect(width*1/4, height*4/8, 360, 90, self.juego.mostrarPanelOpciones,None)
        self.btnOpciones.setImage(pygame.image.load('../images/botonOpciones.png'),pygame.image.load('../images/botonOpcionesShaded.png'))
        self.btnNonoEasy = BotonRect(width * 1 / 10, height * 2 / 8, 180, 90, self.juego.mostrarPanelNiveles,"Easy")
        self.btnNonoEasy.setImage(pygame.image.load('../images/btnEasyNormal.png'),pygame.image.load('../images/btnEasyShaded.png'))
        self.btnNonoMedium = BotonRect(width * 4 / 10, height * 2 / 8, 180, 90, self.juego.mostrarPanelNiveles,"Medium")
        self.btnNonoMedium.setImage(pygame.image.load('../images/btnMediumNormal.png'),pygame.image.load('../images/btnMediumShaded.png'))
        self.btnNonoHard = BotonRect(width * 7 / 10, height * 2 / 8, 180, 90, self.juego.mostrarPanelNiveles,"Hard")
        self.btnNonoHard.setImage(pygame.image.load('../images/btnHardNormal.png'),pygame.image.load('../images/btnHardShaded.png'))
        self.btnVolver = BotonRect(width * 12 / 16, height * 15 / 16, 170, 35, self.toggleMainMenu,None)
        self.btnVolver.setImage(pygame.image.load('../images/botonNormal.png'), pygame.image.load('../images/botonShaded.png'))
        self.mainMenu = False
        self.toggleMainMenu()

    def evento(self, event):
        """
        Maneja los eventos mientras el panel está activo.
        :param event: Objeto de evento que contiene la información relacionada al evento a procesar.
        """
        self.btnJugar.evento(event)
        self.btnOpciones.evento(event)
        self.btnNonoEasy.evento(event)
        self.btnNonoMedium.evento(event)
        self.btnNonoHard.evento(event)
        self.btnVolver.evento(event)

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
        self.fondoImage = pygame.transform.scale(self.fondoImageOG, (self.w, self.h))
        self.surface = pygame.Surface((self.w,self.h))
        self.surface.fill((self.red,self.green,self.blue))

        self.btnJugar.setValues((self.w-360*multi)/2, (self.h-90*multi)*2/7, 360*multi, 90*multi)
        self.btnOpciones.setValues((self.w-360*multi)/2, (self.h-90*multi)*4/7, 360*multi, 90*multi)
        self.btnNonoEasy.setValues((self.w-90*multi)*1/9, (self.h-90*multi)*2/7, 180*multi, 90*multi)
        self.btnNonoMedium.setValues((self.w-90*multi)*4/9, (self.h-90*multi)*2/7, 180*multi, 90*multi)
        self.btnNonoHard.setValues((self.w-90*multi)*7/9, (self.h-90*multi)*2/7, 180*multi, 90*multi)
        self.btnVolver.setValues((self.w-180*multi), (self.h-45*multi), 170*multi, 35*multi)

    def toggleMainMenu(self):
        self.mainMenu = not self.mainMenu
        self.btnJugar.setEnable(self.mainMenu)
        self.btnOpciones.setEnable(self.mainMenu)
        self.btnNonoEasy.setEnable(not self.mainMenu)
        self.btnNonoMedium.setEnable(not self.mainMenu)
        self.btnNonoHard.setEnable(not self.mainMenu)
        self.btnVolver.setEnable(not self.mainMenu)

    def getMainMenu(self):
        return self.mainMenu

    def draw(self, dest_surface):
        """
        Dibuja los componentes correspondientes en la ventana.
        :param dest_surface: Superficie en la que se dibujará el Panel.
        """
        dest_surface.blit(self.fondoImage, (0, 0)) # panel en negro por mientras
        if self.mainMenu :
            self.btnJugar.draw(self.juego.getWindow())
            self.btnOpciones.draw(self.juego.getWindow())
        else :
            self.btnNonoEasy.draw(self.juego.getWindow())
            self.btnNonoMedium.draw(self.juego.getWindow())
            self.btnNonoHard.draw(self.juego.getWindow())
            self.btnVolver.draw(self.juego.getWindow())