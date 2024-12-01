import pygame
import pygame_gui

from src.main.classes.visuals.BotonRect import BotonRect
from src.main.classes.visuals.ImageLoader import ImageLoader
from src.main.classes.visuals.Panel import Panel

class PanelOpciones(Panel):
    """
    Una clase que representa el Panel de Opciones que se presenta al cambiar el panelActual en juego.

    Variables:
        juego (juego): El juego del cual toma referencia.
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
        
        self.rect = pygame.Rect(x, y, width, height)
        self.manager = pygame_gui.UIManager((width, height))

        self.slider_music = pygame_gui.elements.UIHorizontalSlider(
            relative_rect=pygame.Rect((width/2 - 200, height/2 - 50), (400, 50)),
            start_value=50,
            value_range=(0, 100),
            manager=self.manager,
        )
        self.slider_sound = pygame_gui.elements.UIHorizontalSlider(
            relative_rect=pygame.Rect((width/2 - 200, height/2 + 50), (400, 50)),
            start_value=50,
            value_range=(0, 100),
            manager=self.manager,
        )

        self.label_music = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((width/2 - 200, height/2 - 75), (400, 30)),
            text="Volumen Música: 50%",
            manager=self.manager,
        )

        self.label_sound = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((width/2 - 200, height/2 - 25), (400, 30)),
            text="Volumen Sonido: 50%",
            manager=self.manager,
        )
        self.botonVolver = BotonRect(40, height-120, 80, 80, self.juego.mostrarPanelAnterior,None)
        self.botonVolver.setImage(ImageLoader().getVolNormal(), ImageLoader().getVolShaded())

    def evento(self, event):
        """
        Maneja los eventos mientras el panel está activo.
        :param event: Objeto de evento que contiene la información relacionada al evento a procesar.
        """
        self.botonVolver.evento(event)

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:
                if event.ui_element == self.slider_music:
                    valor_musica = event.value
                    self.label_music.set_text(f"Volumen Música: {int(valor_musica)}%")
                    self.juego.musica.setVolumen(valor_musica / 100)
                elif event.ui_element == self.slider_sound:
                    valor_sonido = event.value
                    self.label_sound.set_text(f"Volumen Sonido: {int(valor_sonido)}%")

        self.manager.process_events(event)

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

        self.rect.size = (self.w, self.h)
        self.manager.set_window_resolution((self.w, self.h))

        self.slider_music.set_position((self.w/2 - 200*multi, self.h/2 - 50*multi))
        self.slider_music.set_dimensions((400*multi, 50*multi))
        self.slider_sound.set_position((self.w / 2 - 200*multi, self.h / 2 + 50*multi))
        self.slider_sound.set_dimensions((400*multi, 50*multi))

        self.label_music.set_position((self.w / 2 - 200*multi, self.h / 2 - 90*multi))
        self.label_music.set_dimensions((400 * multi, 50*multi))
        self.label_sound.set_position((self.w / 2 - 200*multi, self.h / 2 + 10*multi))
        self.label_sound.set_dimensions((400*multi, 50*multi))

    def draw(self, dest_surface):
        """
        Dibuja los componentes correspondientes en la ventana.
        :param dest_surface: Superficie en la que se dibujará el Panel.
        """
        dest_surface.fill((0, 0, 0,)) # panel en negro por mientras
        self.botonVolver.draw(self.juego.getWindow())
        self.manager.draw_ui(dest_surface)


    def actualizar(self, tiempo_delta):
        """
        Actualiza el estado del gestor de UI.
        :param tiempo_delta: Delta de tiempo entre frames.
        """
        self.manager.update(tiempo_delta)
