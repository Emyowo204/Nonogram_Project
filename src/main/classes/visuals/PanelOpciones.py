import pygame

from src.main.classes.visuals.BotonRect import BotonRect
from src.main.classes.visuals.ImageLoader import ImageLoader
from src.main.classes.visuals.Panel import Panel

class PanelOpciones(Panel):
    """
    Una clase que representa el Panel de Opciones que se presenta al cambiar el panelActual en juego.

    Variables:
        juego (juego): El juego del cual toma referencia.
        sliderMusic (Rect): Representación del thumb para arrastrar en el slider de música.
        sliderSounds (Rect): Representación del thumb para arrastrar en el slider de sonidos.
        slideando_music (boolean): Indica si está siendo arrastrado slider de música o no.
        slideando_sound (boolean): Indica si está siendo arrastrado slider de sonido o no.
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
        volumenInicial = 0.5
        self.slider_w = 20
        self.slider_h = 50
        self.sliderMinX = width / 2 - 100
        self.sliderMaxX = width / 2 + 100 - self.slider_w
        self.slider_music_x = self.sliderMinX + (self.sliderMaxX - self.sliderMinX) * volumenInicial
        self.slider_sound_x = self.sliderMinX + (self.sliderMaxX - self.sliderMinX) * volumenInicial
        self.slider_music= pygame.Rect(self.slider_music_x, height/2 - 30, self.slider_w, self.slider_h)
        self.slider_sound = pygame.Rect(self.slider_sound_x, height/2 + 75, self.slider_w, self.slider_h)
        self.slideando_music = False
        self.slideando_sound =  False
        self.sliderBackWidth = self.sliderMaxX-self.sliderMinX
        self.sliderBackHeight = 20
        self.botonVolver = BotonRect(40, height-120, 80, 80, self.juego.mostrarPanelAnterior,None)
        self.botonVolver.setImage(ImageLoader().getVolNormal(), ImageLoader().getVolShaded())

    def evento(self, event):
        """
        Maneja los eventos mientras el panel está activo.
        :param event: Objeto de evento que contiene la información relacionada al evento a procesar.
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.slider_music.collidepoint(event.pos):
                self.slideando_music = True
            elif self.slider_sound.collidepoint(event.pos):
                self.slideando_sound = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.slideando_music = False
            self.slideando_sound = False
        elif event.type == pygame.MOUSEMOTION:
            if self.slideando_music == True:
                self.slider_music.x = max(self.sliderMinX, min(event.pos[0], self.sliderMaxX))
            elif self.slideando_sound == True:
                self.slider_sound.x = max(self.sliderMinX, min(event.pos[0], self.sliderMaxX))

        self.botonVolver.evento(event)
        nuevoVolumenMusic = (self.sliderMaxX - self.slider_music.x - (self.x +50)) / 200
        self.juego.getMusica().setVolumen(nuevoVolumenMusic)

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
        self.botonVolver.setValues(40*multi, self.h-120*multi, 80*multi, 80*multi)

        self.slider_w = 20 * multi
        self.slider_h = 50 * multi
        self.slider_music.x = (w/2) - 100 * multi
        self.slider_sound.x = (w/2) - 100 * multi
        self.slider_music.y = h/2 - 75 * multi
        self.slider_sound.y = h/2 + 75 * multi
        self.sliderMinX = (w/2) - 100 * multi + self.slider_w
        self.sliderMaxX = (w/2) + 100 * multi
        self.sliderBackWidth = self.sliderMaxX-self.sliderMinX
        self.sliderBackHeight = 20 * multi

    def draw(self, dest_surface):
        """
        Dibuja los componentes correspondientes en la ventana.
        :param dest_surface: Superficie en la que se dibujará el Panel.
        """
        dest_surface.fill((0, 0, 0,)) # panel en negro por mientras
        self.botonVolver.draw(self.juego.getWindow())

        # Dibuja el fondo de los sliders
        pygame.draw.rect(dest_surface, (0, 255, 0),
                         (self.sliderMinX, self.slider_music.y, self.sliderBackWidth, self.sliderBackHeight))
        pygame.draw.rect(dest_surface, (0, 255, 0),
                         (self.sliderMinX, self.slider_sound.y, self.sliderBackWidth, self.sliderBackHeight))

        # Dibuja las partes restantes de los sliders
        pygame.draw.rect(dest_surface, (100, 100, 100), (
        self.slider_music.x, self.slider_music.y, self.sliderMaxX - self.slider_music.x, self.sliderBackHeight))
        pygame.draw.rect(dest_surface, (100, 100, 100), (
        self.slider_sound.x, self.slider_sound.y, self.sliderMaxX - self.slider_sound.x, self.sliderBackHeight))

        # Dibuja los thumbs
        pygame.draw.rect(dest_surface, (255, 0, 0), (self.slider_music.x, self.slider_music.y, self.slider_w, self.slider_h))  # dibujo thumb slider1
        pygame.draw.rect(dest_surface, (255, 0, 0), (self.slider_sound.x, self.slider_sound.y, self.slider_w, self.slider_h))  # dibujo thumb slider2

        # texto de prueba para mostrar el volumen
        font = pygame.font.Font(None, 24)
        volumenTexto1 = font.render(f"Volumen Música: {int(self.juego.getMusica().getVolumen() * 100)}%", True,
                                    (255, 255, 255))
        volumenTexto2 = font.render(f"Volumen Sonido: {int(self.juego.getMusica().getVolumen() * 100)}%", True,
                                    (255, 255, 255))
        dest_surface.blit(volumenTexto1, (self.sliderMinX, self.slider_music.y + 10))
        dest_surface.blit(volumenTexto2, (self.sliderMinX, self.slider_sound.y + 10))
