import pygame

from src.main.classes.visuals.Partida import Partida
from src.main.classes.visuals.ImageLoader import ImageLoader
from src.main.classes.visuals.Panel import Panel
from src.main.classes.visuals.PanelOpciones import PanelOpciones
from src.main.classes.visuals.Musica import Musica
from src.main.classes.visuals.Ventana import Ventana


class Juego:
    def __init__(self):
        self.panelActual = None
        self.musica = None
        self.partida = None

    def start(self):
        window_size = 720
        ventana = Ventana(window_size,window_size)
        window = ventana.getWindow()
        pygame.mixer.init()
        self.musica = Musica("../../sounds/opcionesmusica.wav")
        self.panelActual = None
        clock = pygame.time.Clock()
        self.partida = Partida((720-400)/2,(720-630)/2,600,630,'TEST',1)
        self.panelOpciones = PanelOpciones( 0, 0, window_size, window_size, self)

        self.mostrarPanelCuadrilla()

        botonOpcionesSurface = pygame.Surface((100, 50))
        botonOpciones = pygame.Rect(600, 650, 100, 50)

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
                        new_size = (event.h,event.w)
                        self.partida.fitWindow(new_size[1], new_size[0])

                elif event.type == pygame.MOUSEBUTTONUP:
                    if resizing:

                        resizing=False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if botonOpciones.collidepoint(event.pos):  # presiona boton
                        if self.panelActual == self.partida:
                            self.mostrarPanelOpciones()
                        elif self.panelActual == self.panelOpciones:
                            self.mostrarPanelCuadrilla()


                if self.panelActual == self.partida:
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        self.partida.handleClick(event.pos)
                        self.partida.checkAssumtion(event.pos)
                elif self.panelActual == self.panelOpciones:
                    self.panelActual.evento(event)  # si es panel opciones, usa la funcion evento para administrar los eventos de este

            panel = Panel(0,0,25,25)
            image = ImageLoader().getImage()
            panel.setImage(image)

            window.fill((255,255,255))
            self.panelActual.draw(window)

            pygame.draw.rect(window, (0, 255, 0), botonOpciones)
            pygame.display.flip()

        pygame.quit()

    def mostrarPanelCuadrilla(self):
        self.panelActual = self.partida
        self.musica.cambiarMusica("../../sounds/cuadrillamusica.wav")

    def mostrarPanelOpciones(self):
        self.panelActual = self.panelOpciones
        self.musica.cambiarMusica("../../sounds/opcionesmusica.wav")
    def getMusica(self):
        return self.musica
