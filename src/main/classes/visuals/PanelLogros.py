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
        self.Og_achievements_uncompleted = []
        self.Og_achievements_completed = []
        self.achievements_uncompleted_images = []
        self.achievements_completed_images = []
        self.achievements = []
        for i in range(6):
            self.Og_achievements_uncompleted.append(pygame.image.load('../images/logros/nologro'+str(i+1)+'.png'))
            self.achievements_uncompleted_images.append(self.Og_achievements_uncompleted[i])
            self.Og_achievements_completed.append(pygame.image.load('../images/logros/nologro'+str(i+1)+'.png'))
            self.achievements_completed_images.append(self.Og_achievements_completed[i])
            self.achievements.append(False)

        self.ancho, self.alto = self.Og_achievements_completed[0].get_size()
        self.pos_X = []
        for i in range(6):
            if i%2 == 0:
                self.pos_X.append(40)
            else:
                self.pos_X.append(width - (self.ancho+40))

        self.pos_Y = [
            40,
            40,
            height // 3 + 20,
            height // 3 + 20,
            2 * height // 3 + 20,
            2 * height // 3 + 20,
        ]


        self.setColor(150,250,220)
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

    def completeAchievement(self, index):
        """
        Completa un logro indicado.
        :param index: índice del logro completado.
        """
        self.achievements[index] = True

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

        for i in range(len(self.achievements)):
            self.achievements_completed_images[i] = pygame.transform.scale(self.Og_achievements_completed[i],
                                                                           (self.ancho*multi, self.alto*multi))
            self.achievements_uncompleted_images[i] = pygame.transform.scale(self.Og_achievements_uncompleted[i],
                                                                           (self.ancho * multi, self.alto * multi))

        for i in range(6):
            if i%2 == 0:
                self.pos_X[i] = (40*multi)
            else:
                self.pos_X[i] = (w - (self.ancho+40)*multi)

        self.pos_Y = [
            40*multi,
            40*multi,
            h // 3 + 40*multi,
            h // 3 + 40*multi,
            2 * h // 3 + 40*multi,
            2 * h // 3 + 40*multi,
        ]

        # self.fondoImage = pygame.transform.scale(self.fondoImageOG, (self.w, self.h))
        self.btnOpciones.setValues(self.w-120*multi, self.h-120*multi, 80*multi, 80*multi)
        self.btnVolver.setValues(40*multi, self.h-120*multi, 80*multi, 80*multi)


    def draw(self, dest_surface):
        """
        Dibuja los componentes correspondientes en la ventana.
        :param dest_surface: Superficie en la que se dibujará el Panel.
        """
        super().draw(dest_surface)
        for i in range(len(self.achievements)):
            if self.achievements[i] == True:
                dest_surface.blit(self.achievements_completed_images[i],(self.pos_X[i], self.pos_Y[i]))
            else:
                dest_surface.blit(self.achievements_completed_images[i], (self.pos_X[i], self.pos_Y[i]))

        self.btnOpciones.draw(self.juego.getWindow())
        self.btnVolver.draw(self.juego.getWindow())

