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
        self.botonJugar = BotonRect(width*1/4, height*2/8, 360, 90, self.juego.mostrarPanelCuadrilla)
        self.botonJugar.setImage(pygame.image.load('../images/botonJugar.png'),pygame.image.load('../images/botonJugarShaded.png'))
        self.botonOpciones = BotonRect(width*1/4, height*4/8, 360, 90, self.juego.mostrarPanelOpciones)
        self.botonOpciones.setImage(pygame.image.load('../images/botonOpciones.png'),pygame.image.load('../images/botonOpcionesShaded.png'))

    def evento(self, event):
        """
        Maneja los eventos mientras el panel está activo.
        :param event: Objeto de evento que contiene la información relacionada al evento a procesar.
        """
        self.botonJugar.evento(event)
        self.botonOpciones.evento(event)

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

        self.botonJugar.setSize(360*multi, 90*multi)
        self.botonJugar.setCoord((self.w-self.botonJugar.getSize()[0])/2, (self.h-self.botonJugar.getSize()[1])*2/7)
        self.botonOpciones.setSize(360*multi, 90*multi)
        self.botonOpciones.setCoord((self.w-self.botonOpciones.getSize()[0])/2, (self.h-self.botonOpciones.getSize()[1])*4/7)

    def draw(self, dest_surface):
        """
        Dibuja los componentes correspondientes en la ventana.
        :param dest_surface: Superficie en la que se dibujará el Panel.
        """
        dest_surface.blit(self.fondoImage, (0, 0)) # panel en negro por mientras
        self.botonJugar.draw(self.juego.getWindow())
        self.botonOpciones.draw(self.juego.getWindow())