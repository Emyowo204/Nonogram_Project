import pygame

from src.main.classes.models.Partida import Partida
from src.main.classes.visuals.ImageLoader import ImageLoader
from src.main.classes.visuals.Panel import Panel
from src.main.classes.visuals.PanelOpciones import PanelOpciones
from src.main.classes.visuals.PanelMenu import PanelMenu
from src.main.classes.visuals.Musica import Musica


class Juego:
    def __init__(self):
        self.panelActual = None
        self.musica = None
        self.partida = None

    def start(self):
        pygame.init()
        pygame.mixer.init()
        program_icon = ImageLoader().getIcon()
        pygame.display.set_icon(program_icon)
        self.musica = Musica("../../sounds/opcionesmusica.wav")
        self.panelActual = None
        grid_size = 10
        cell_size = 30
        window_size = 720
        window = pygame.display.set_mode((window_size,window_size))
        clock = pygame.time.Clock()

        self.partida = Partida(26,26,400,630,'TEST',0)


        self.panelOpciones = PanelOpciones( 0, 0, window_size, window_size, self)

        self.mostrarPanelCuadrilla()

        botonOpcionesSurface = pygame.Surface((100, 50))
        botonOpciones = pygame.Rect(600, 650, 100, 50)

        running = True
        while running:
            deltatime = clock.tick(60) / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif self.panelActual == self.partida:
                    if event.type == pygame.MOUSEBUTTONDOWN and botonOpciones.collidepoint(event.pos):
                        self.mostrarPanelOpciones()
                    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        self.partida.handleClick(event.pos)
                        self.partida.checkAssumtion(event.pos)
                elif self.panelActual == self.panelOpciones:
                    if event.type == pygame.MOUSEBUTTONDOWN and botonOpciones.collidepoint(event.pos):
                        self.mostrarPanelCuadrilla()
                    elif self.panelActual == self.panelOpciones:
                        self.panelActual.evento(event)  # si es panel opciones, usa la funcion evento para administrar los eventos de este

            panel = Panel(0,0,25,25)
            image = ImageLoader().getImage()
            panel.setImage(image)

            window.fill((0,0,0))
            self.panelActual.draw(window)

            # panel.draw(window)
            pygame.draw.rect(window, (0, 255, 0), botonOpciones)
            pygame.display.flip()

        pygame.quit()

    def mostrarPanelMenu(self):
        self.panelActual = self.panelMenu
        self.musica.cambiarMusica(None)
    def mostrarPanelCuadrilla(self):
        self.panelActual = self.partida
        self.musica.cambiarMusica("../../sounds/cuadrillamusica.wav")

    def mostrarPanelOpciones(self):
        self.panelActual = self.panelOpciones
        self.musica.cambiarMusica("../../sounds/opcionesmusica.wav")

    def getMusica(self):
        return self.musica
