import pygame

from src.main.classes.visuals.ImageLoader import ImageLoader
from src.main.classes.visuals.Panel import Panel
from src.main.classes.visuals.BotonRect import BotonRect

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
        # self.fondoImageOG = pygame.image.load('../images/fondoLogros.png')
        # self.fondoImage = pygame.transform.scale(self.fondoImageOG, (width, height))
        self.btnOpciones = BotonRect(width-120, height-120, 80, 80, self.juego.mostrarPanelOpciones,None)
        self.btnOpciones.setImage(ImageLoader().getOpnNormal(), ImageLoader().getOpnShaded())
        self.btnVolver = BotonRect(40, height-120, 80, 80, self.toggleMainMenu,None)
        self.btnVolver.setImage(ImageLoader().getVolNormal(), ImageLoader().getVolShaded())

    def evento(self, event):
        """
        Maneja los eventos mientras el panel está activo.
        :param event: Objeto de evento que contiene la información relacionada al evento a procesar.
        """
        self.btnOpciones.evento(event)
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
        # self.fondoImage = pygame.transform.scale(self.fondoImageOG, (self.w, self.h))
        self.btnOpciones.setValues(self.w-120*multi, self.h-120*multi, 80*multi, 80*multi)
        self.btnVolver.setValues(40*multi, self.h-120*multi, 80*multi, 80*multi)

    def draw(self, dest_surface):
        """
        Dibuja los componentes correspondientes en la ventana.
        :param dest_surface: Superficie en la que se dibujará el Panel.
        """
        #self.fondoImage
        dest_surface.fill((0, 0, 0,)) # panel en negro por mientras
        self.btnOpciones.draw(self.juego.getWindow())
        self.btnVolver.draw(self.juego.getWindow())


    #Ideas de logros:
    #- 1er nonograma
    #- 10 nonogramas
    #- completar nonograma con tiempo en menos de x tiempo
    #- completar nonograma con vida sin perder ninguna
    #- perder todas las vidas por primera vez
    #- llegar a 10 min en un nonograma


