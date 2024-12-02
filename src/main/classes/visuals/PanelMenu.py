import pygame

from src.main.classes.visuals.ImageLoader import ImageLoader
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
        self.btnModoList = []
        self.btnDifficulty = []
        for i in range(4):
            self.btnModoList.append(BotonRect(width*1/4, height*(2+i)/8, 400, 90, self.toggleMainMenu,i))
            self.btnModoList[i].setImage(pygame.image.load('../images/btnModo'+str(i)+'Normal.png'),pygame.image.load('../images/btnModo'+str(i)+'Shaded.png'))
            self.btnDifficulty.append(BotonRect(self.w/2-150, self.h*(2+3*i)/16, 300, 100, self.juego.mostrarPanelNiveles,i))
            self.btnDifficulty[i].setImage(pygame.image.load('../images/btnDiff'+str(i)+'Normal.png'),pygame.image.load('../images/btnDiff'+str(i)+'Shaded.png'))
        self.btnOpciones = BotonRect(width-120, height-120, 80, 80, self.juego.mostrarPanelOpciones,None)
        self.btnOpciones.setImage(ImageLoader().getOpnNormal(), ImageLoader().getOpnShaded())
        self.btnVolver = BotonRect(40, height-120, 80, 80, self.toggleMainMenu,0)
        self.btnVolver.setImage(ImageLoader().getVolNormal(), ImageLoader().getVolShaded())
        self.btnLogro = BotonRect(40, height-120, 80, 80, self.juego.mostrarPanelLogros,None)
        self.btnLogro.setImage(pygame.image.load('../images/botonLogroNormal.png'), pygame.image.load('../images/botonLogroShaded.png'))
        self.btnTutorial = BotonRect(width - 120, 40, 80, 80, self.juego.mostrarPanelTutorial, None)
        self.btnTutorial.setImage(pygame.image.load('../images/botonInfoNormal.png'), pygame.image.load('../images/botonInfoShaded.png'))
        self.mainMenu = False
        self.toggleMainMenu(0)

    def evento(self, event):
        """
        Maneja los eventos mientras el panel está activo.
        :param event: Objeto de evento que contiene la información relacionada al evento a procesar.
        """
        self.btnOpciones.evento(event)
        self.btnVolver.evento(event)
        self.btnLogro.evento(event)
        self.btnTutorial.evento(event)
        for i in range(4):
            self.btnModoList[i].evento(event)
            self.btnDifficulty[i].evento(event)

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
        for i in range(4):
            self.btnModoList[i].setValues(self.w/2-200*multi, self.h*(3+3*i)/20, 400*multi, 90*multi)
            self.btnDifficulty[i].setValues(self.w/2-150*multi, self.h*(2+3*i)/16, 300*multi, 100*multi)
        self.btnOpciones.setValues(self.w-120*multi, self.h-120*multi, 80*multi, 80*multi)
        self.btnVolver.setValues(40*multi, self.h-120*multi, 80*multi, 80*multi)
        self.btnLogro.setValues(40 * multi, self.h - 120 * multi, 80 * multi, 80 * multi)
        self.btnTutorial.setValues(self.w - 120 * multi, 40 * multi, 80 * multi, 80 * multi)

    def toggleMainMenu(self, mode):
        self.juego.setMode(mode)
        self.mainMenu = not self.mainMenu
        self.btnVolver.setEnable(not self.mainMenu)
        self.btnLogro.setEnable(self.mainMenu)
        self.btnTutorial.setEnable(self.mainMenu)
        for i in range(4):
            self.btnModoList[i].setEnable(self.mainMenu)
            self.btnDifficulty[i].setEnable(not self.mainMenu)

    def getMainMenu(self):
        return self.mainMenu

    def draw(self, dest_surface):
        """
        Dibuja los componentes correspondientes en la ventana.
        :param dest_surface: Superficie en la que se dibujará el Panel.
        """
        dest_surface.blit(self.fondoImage, (0, 0)) # panel en negro por mientras
        self.btnOpciones.draw(self.juego.getWindow())
        if self.mainMenu :
            self.btnLogro.draw(self.juego.getWindow())
            self.btnTutorial.draw(self.juego.getWindow())
            for i in range(len(self.btnModoList)):
                self.btnModoList[i].draw(self.juego.getWindow())
        else :
            self.btnVolver.draw(self.juego.getWindow())
            for i in range(len(self.btnDifficulty)):
                self.btnDifficulty[i].draw(self.juego.getWindow())

