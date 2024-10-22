import pygame

from src.main.classes.visuals.BotonRect import BotonRect
from src.main.classes.visuals.ImageLoader import ImageLoader
from src.main.classes.visuals.Panel import Panel

class PanelOpciones(Panel):
    """
    Una clase que representa el Panel de Opciones que se presenta al cambiar el panelActual en juego.

    Variables:
        juego (juego): El juego del cual toma referencia.
        slider (Rect): Representación del thumb para arrastrar en un slider.
        slideando (boolean): Indica si está siendo arrastrado slider o no.
        sliderMinX (int): Valor de la posición mínima a la que puede estar el slider.
        sliderMaxX (int): Valor de la posición másxima a la que puede estar el slider.
        sliderBackWidth (int): Valor del ancho del fondo del slide.
        sliderBackHeight (int): Valor del largo del fondo del slide.
        volumenInicial (int): Valor del volumen inicial al comenzar la aplicación.
        slider.x (int): Valor de la posición x del slider al inicializar.
        normalImage (image): Variable que contiene la imagen de un botón al no estar presionado.
        shadedImage (image): Variable que contiene la imagen de un botón al tener el cursor sobre él.
        botonVolver (BotonRect): Botón que ejecuta la acción de volver al Panel Menu Principal.

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

        self.slider= pygame.Rect(x+50, y+50, 20, 50) # thumb para arrastrar
        self.slideando = False
        self.sliderMinX = x + 50
        self.sliderMaxX = x + 250
        self.sliderBackWidth = 250 # barra fondo
        self.sliderBackHeight = 20 # barra fondo
        volumenInicial = 0.5
        self.slider.x = int(self.sliderMinX + (self.sliderMaxX - self.sliderMinX) * volumenInicial)
        self.botonVolver = BotonRect(width * 12 / 16, height * 15 / 16, 170, 35, self.juego.mostrarPanelMenu)
        self.botonVolver.setImage(pygame.image.load('../images/botonNormal.png'),pygame.image.load('../images/botonShaded.png'))

    def evento(self, event):
        """
        Maneja los eventos mientras el panel está activo.
        :param event: Objeto de evento que contiene la información relacionada al evento a procesar.
        """
        if event.type == pygame.MOUSEBUTTONDOWN and self.slider.collidepoint(event.pos):
            self.slideando = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.slideando = False
        elif event.type == pygame.MOUSEMOTION and self.slideando:
            self.slider.x = max(self.sliderMinX, min(event.pos[0], self.sliderMaxX))
        self.botonVolver.evento(event)
        nuevoVolumen = (self.slider.x - (self.x +50)) / 200
        self.juego.getMusica().setVolumen(nuevoVolumen)

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
        self.botonVolver.setValues((self.w - 180 * multi), (self.h - 45 * multi), 170 * multi, 35 * multi)

    def draw(self, dest_surface):
        """
        Dibuja los componentes correspondientes en la ventana.
        :param dest_surface: Superficie en la que se dibujará el Panel.
        """
        dest_surface.fill((0, 0, 0,)) # panel en negro por mientras
        self.botonVolver.draw(self.juego.getWindow())

        pygame.draw.rect(dest_surface, (0, 255, 0), (self.sliderMinX, self.y+65, (self.slider.x - self.sliderMinX), self.sliderBackHeight))  # fondo slider

        pygame.draw.rect(dest_surface, (100, 100, 100), (self.slider.x, self.y+65, (self.sliderMaxX - self.slider.x + self.slider.width), self.sliderBackHeight))  # fondo slider

        pygame.draw.rect(dest_surface, (255, 0, 0), self.slider)  # dibujo thumb

        # texto prueba
        font = pygame.font.Font(None, 24)
        volumenTexto = font.render(f"Volumen: {int(self.juego.getMusica().getVolumen() * 100)}%", True, (255, 255, 255))
        dest_surface.blit(volumenTexto, (self.sliderMinX, self.y + 100))
