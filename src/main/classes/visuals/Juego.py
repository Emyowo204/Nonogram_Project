import pygame

from src.main.classes.models.Cuadrilla import Cuadrilla
from src.main.classes.visuals.ImageLoader import ImageLoader
from src.main.classes.visuals.Panel import Panel
from src.main.classes.visuals.PanelCuadrilla import PanelCuadrilla
from src.main.classes.visuals.PanelOpciones import PanelOpciones
from src.main.classes.visuals.Musica import Musica


class Juego:
    def start(self):
        pygame.init()
        pygame.mixer.init()
        self.musica = Musica("../../sounds/cuadrillamusica.wav")
        self.panelActual = None
        grid_size = 10
        cell_size = 30
        window_size = 720
        window = pygame.display.set_mode((window_size,window_size))
        clock = pygame.time.Clock()

        cuadrilla = Cuadrilla(None, None, 'test.txt')
        self.panelCuadrilla = PanelCuadrilla(cuadrilla, 26, 26, 300, 300)
        ## self.panelOpciones = PanelOpciones(self.musica, 0, 0, window_size, window_size)

        self.mostrarPanelCuadrilla()

        botonOpciones = pygame.Rect(600, 650, 100, 50)

        running = True
        while running:
            deltatime =  clock.tick(60)/1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                # elif event.type == pygame.MOUSEBUTTONDOWN:
                #    if botonOpciones.collidepoint(event.pos): # presiona boton
                #        self.mostrarPanelOpciones()
                # elif event.type == pygame.MOUSEMOTION:
                #    if isinstance(self.panelActual, PanelOpciones):
                #        self.panelActual.evento(event) # si es panel opciones, usa la funcion evento para administrar los eventos de este

            panel = Panel(0,0,25,25)
            image = ImageLoader().getImage()
            panel.setImage(image)

            window.fill((0,0,0))
            self.panelActual.draw(window)
            # panel.draw(window)
            pygame.draw.rect(window, (0, 255, 0), botonOpciones)
            pygame.display.flip()

        pygame.quit()

    def mostrarPanelCuadrilla(self):
        self.panelActual = self.panelCuadrilla
        # self.musica.cambiarMusica("src/main/sounds/cuadrillamusica.wav")
        # self.musica.play()

    #def mostrarPanelOpciones(self):
    #    self.panelActual = self.panelOpciones
    #    self.musica.cambiarMusica("src/main/sounds/opcionesmusica.wav")
    #    self.musica.play()

