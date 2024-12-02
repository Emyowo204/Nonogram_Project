import pygame

from src.main.classes.visuals.ImageLoader import ImageLoader
from src.main.classes.visuals.Panel import Panel
from src.main.classes.visuals.BotonRect import BotonRect

class PanelTutorial(Panel):
    """
    Una clase que representa el Panel de Tutorial que se presenta al presionar el botón del panel inicial.

    Variables:
        juego (juego): El juego asociado a este panel.
        tutorial (list): Lista de imágenes que conforman el tutorial.
        imagen_actual (int): Índice de la imagen actualmente visible en el tutorial.
        ancho (int): Ancho de la imagen del tutorial.
        alto (int): Alto de la imagen del tutorial.
        pos_X (int): Coordenada X donde se dibujará la imagen actual.
        pos_Y (int): Coordenada Y donde se dibujará la imagen actual.
        btnOpciones (BotonRect): Botón que permite cambiar al panel de opciones.
        btnVolver (BotonRect): Botón que permite volver al panel anterior.
        btnNext (BotonRect): Botón que permite avanzar a la siguiente imagen del tutorial.
        btnBack (BotonRect): Botón que permite retroceder a la imagen anterior del tutorial.

    Métodos:
        __init__(x, y, width, height, juego): Inicializa el PanelTutorial con las dimensiones y el juego asociado.
        evento(event): Maneja los eventos cuando el panel está activo.
        fitWindow(w, h): Ajusta el tamaño y la posición de los componentes del panel cuando la ventana cambia de tamaño.
        draw(dest_surface): Dibuja el contenido del PanelTutorial en la superficie de destino.
        fotoAnterior(): Cambia a la imagen anterior del tutorial.
        fotoSiguiente(): Cambia a la siguiente imagen del tutorial.
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

        self.tutorial = [
            pygame.image.load('../images/t1.png'),
            pygame.image.load('../images/t2.png'),
            pygame.image.load('../images/t3.png'),
            pygame.image.load('../images/t4.png'),
            pygame.image.load('../images/t5.png'),
            pygame.image.load('../images/t6.png'),
            pygame.image.load('../images/t7.png'),
        ]

        self.imagen_actual = 0
        self.ancho, self.alto = self.tutorial[0].get_size()
        self.pos_X = width // 2 - self.ancho // 2
        self.pos_Y = height // 2 - 3 * self.alto // 5

        # self.fondoImageOG = pygame.image.load('../images/fondoTutorial.png')
        # self.fondoImage = pygame.transform.scale(self.fondoImageOG, (width, height))
        self.btnOpciones = BotonRect(width-120, height-120, 80, 80, self.juego.mostrarPanelOpciones,None)
        self.btnOpciones.setImage(ImageLoader().getOpnNormal(), ImageLoader().getOpnShaded())
        self.btnVolver = BotonRect(40, height-120, 80, 80, self.juego.mostrarPanelMenu,None)
        self.btnVolver.setImage(ImageLoader().getVolNormal(), ImageLoader().getVolShaded())
        self.btnNext = BotonRect(width/2, height - 120, 80, 80, self.fotoSiguiente,None)
        self.btnNext.setImage(ImageLoader().getOpnNormal(), ImageLoader().getOpnShaded())
        self.btnBack = BotonRect(width/2 - 100, height - 120, 80, 80, self.fotoAnterior, None)
        self.btnBack.setImage(ImageLoader().getVolNormal(), ImageLoader().getVolShaded())

    def evento(self, event):
        """
        Maneja los eventos mientras el panel está activo.
        :param event: Objeto de evento que contiene la información relacionada al evento a procesar.
        """
        self.btnOpciones.evento(event)
        self.btnVolver.evento(event)
        self.btnNext.evento(event)
        self.btnBack.evento(event)

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

        for i in range(len(self.tutorial)):
            self.tutorial[i] = pygame.transform.scale(self.tutorial[i], (self.ancho*multi, self.alto*multi))

        self.pos_X = self.w // 2 - self.ancho*multi // 2
        self.pos_Y = self.h // 2 - 3 * self.alto*multi // 5

        # self.fondoImage = pygame.transform.scale(self.fondoImageOG, (self.w, self.h))
        self.btnOpciones.setValues(self.w-120*multi, self.h-120*multi, 80*multi, 80*multi)
        self.btnVolver.setValues(40*multi, self.h-120*multi, 80*multi, 80*multi)
        self.btnNext.setValues(w/2, h - 120*multi, 80 * multi, 80 * multi)
        self.btnBack.setValues(w/2 - 100*multi, h - 120*multi, 80 * multi, 80 * multi)

    def draw(self, dest_surface):
        """
        Dibuja los componentes correspondientes en la ventana.
        :param dest_surface: Superficie en la que se dibujará el Panel.
        """
        #self.fondoImage
        dest_surface.fill((0, 0, 0,)) # panel en negro por mientras

        dest_surface.blit(self.tutorial[self.imagen_actual],
                          (self.pos_X, self.pos_Y))

        self.btnOpciones.draw(self.juego.getWindow())
        self.btnVolver.draw(self.juego.getWindow())
        self.btnNext.draw(self.juego.getWindow())
        self.btnBack.draw(self.juego.getWindow())

    def fotoAnterior(self):
        """
         Cambia a la imagen anterior en el array.
         """
        if self.imagen_actual > 0:
            self.imagen_actual -= 1

    def fotoSiguiente(self):
        """
            Cambia a la siguiente imagen en el array.
        """
        if self.imagen_actual < len(self.tutorial) - 1:
            self.imagen_actual += 1
