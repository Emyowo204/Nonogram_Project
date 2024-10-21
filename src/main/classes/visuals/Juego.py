import pygame

from src.main.classes.visuals.PanelPartida import PanelPartida
from src.main.classes.visuals.ImageLoader import ImageLoader
from src.main.classes.visuals.Panel import Panel
from src.main.classes.visuals.PanelOpciones import PanelOpciones
from src.main.classes.visuals.PanelMenu import PanelMenu
from src.main.classes.visuals.Musica import Musica
from src.main.classes.visuals.Ventana import Ventana


class Juego:
    def __init__(self):
        self.window = None
        self.window_size = [None, None]
        self.panelActual = None
        self.musica = None
        self.partida = None
        self.panelOpciones = None
        self.panelMenu = None

    def start(self,mode,index):
        self.window_size = [720, 720]
        ventana = Ventana(self.window_size[0], self.window_size[1])
        self.window = ventana.getWindow()
        pygame.mixer.init()
        self.musica = Musica("../../sounds/opcionesmusica.wav")

        clock = pygame.time.Clock()
        self.panelMenu = PanelMenu(0,0, self.window_size[0], self.window_size[1], self)
        self.partida = PanelPartida(0, 0, self.window_size[0], self.window_size[1],mode,index, self)
        self.panelOpciones = PanelOpciones( 0, 0, self.window_size[0], self.window_size[1], self)
        self.mostrarPanelMenu()

        resizing = False
        running = True
        new_size = (720,720)
        self.partida.fitWindow(new_size[0],new_size[1])
        while running:
            deltatime = clock.tick(60) / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.VIDEORESIZE:
                        resizing = True
                        new_size = (event.w,event.h)
                        self.panelActual.fitWindow(new_size[0], new_size[1])
                        self.window_size = new_size

                elif event.type == pygame.MOUSEBUTTONUP:
                    if resizing:
                        resizing=False

                if self.panelActual == self.partida:
                    if pygame.mouse.get_pressed()[0]:
                        self.partida.handleClick(event.pos)
                self.panelActual.evento(event)

            panel = Panel(0,0,25,25)
            image = ImageLoader().getDefaultImage()
            panel.setImage(image)

            self.panelActual.draw(self.window)

            self.window.fill((255,255,255))
            self.panelActual.draw(self.window)

            pygame.display.flip()

        pygame.quit()


    def mostrarPanelMenu(self):
        self.panelActual = self.panelMenu
        self.panelMenu.fitWindow(self.window_size[0], self.window_size[1])
        self.musica.cambiarMusica(None)

    def mostrarPanelCuadrilla(self):
        self.panelActual = self.partida
        self.partida.fitWindow(self.window_size[0], self.window_size[1])
        self.musica.cambiarMusica("../../sounds/cuadrillamusica.wav")

    def mostrarPanelOpciones(self):
        self.panelActual = self.panelOpciones
        self.panelOpciones.fitWindow(self.window_size[0], self.window_size[1])
        self.musica.cambiarMusica("../../sounds/opcionesmusica.wav")

    def getMusica(self):
        return self.musica

    def getWindow(self):
        return self.window

    def getWindowSize(self):
        return self.window_size