import os

import pygame

from src.main.classes.models.FileManager import FileManager
from src.main.classes.visuals.PanelFileManager import PanelFileManager
from src.main.classes.visuals.PanelPartida import PanelPartida
from src.main.classes.visuals.ImageLoader import ImageLoader
from src.main.classes.visuals.Panel import Panel
from src.main.classes.visuals.PanelOpciones import PanelOpciones
from src.main.classes.visuals.PanelMenu import PanelMenu
from src.main.classes.visuals.PanelNiveles import PanelNiveles
from src.main.classes.models.Musica import Musica
from src.main.classes.visuals.Ventana import Ventana


class Juego:
    def __init__(self):
        self.hard_count = 0
        self.medium_count = 0
        self.easy_count = 0
        self.custom_count = 0
        self.custom_puzzles = []
        self.window = None
        self.window_size = [None, None]
        self.panelActual = None
        self.musica = None
        self.partida = None
        self.panelNiveles = None
        self.panelOpciones = None
        self.panelMenu = None
        self.panelFileManager = None
        self.game_difficulty = "TEST"


    def start(self):
        self.filemanager = FileManager()
        self.contarPuzzles()
        self.window_size = [720, 720]
        ventana = Ventana(self.window_size[0], self.window_size[1])
        self.window = ventana.getWindow()
        pygame.mixer.init()
        self.musica = Musica("../../sounds/opcionesmusica.wav")

        clock = pygame.time.Clock()
        self.panelMenu = PanelMenu(0,0, self.window_size[0], self.window_size[1], self)
        self.partida = PanelPartida(0, 0, self.window_size[0], self.window_size[1], self)
        self.panelOpciones = PanelOpciones( 0, 0, self.window_size[0], self.window_size[1], self)
        self.panelNiveles = PanelNiveles( 0, 0, self.window_size[0], self.window_size[1], self)
        self.panelFileManager = PanelFileManager(0,0,self.window_size[0], 1080,self)
        self.mostrarPanelMenu()
        self.panelFileManager.updateButtons()

        resizing = False
        running = True
        new_size = (720,720)
        self.partida.fitWindow(new_size[0],new_size[1])
        self.panelFileManager.updateButtons()
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

    def contarPuzzles(self):
        self.filemanager.changeDir(os.path.join(os.getcwd(), "../puzzles/Easy"))
        self.filemanager.updateDir()
        self.easy_count = len(self.filemanager.getPuzzles())
        self.filemanager.changeDir(os.path.join(os.getcwd(), "../puzzles/Medium"))
        self.filemanager.updateDir()
        self.medium_count = len(self.filemanager.getPuzzles())
        self.filemanager.changeDir(os.path.join(os.getcwd(), "../puzzles/Hard"))
        self.filemanager.updateDir()
        self.hard_count = len(self.filemanager.getPuzzles())

    def readCustom(self):
        self.filemanager.changeDir(os.path.join(os.getcwd(), "../puzzles/Custom"))
        self.filemanager.updateDir()
        self.custom_puzzles = self.filemanager.getPuzzles()
        self.custom_count = len(self.custom_puzzles)

    def mostrarPanelMenu(self):
        self.panelActual = self.panelMenu
        self.panelMenu.fitWindow(self.window_size[0], self.window_size[1])
        self.musica.cambiarMusica(None)

    def mostrarPanelNiveles(self, game_difficulty):
        quantity = 0
        if game_difficulty == "Easy":
            quantity = self.easy_count
        elif game_difficulty == "Medium":
            quantity = self.medium_count
        elif game_difficulty == "Hard":
            quantity = self.hard_count
        elif game_difficulty == "Custom":
            self.readCustom()
            quantity = self.custom_count
        self.panelNiveles.setLevelButtons(quantity)
        self.panelActual = self.panelNiveles
        self.panelNiveles.fitWindow(self.window_size[0], self.window_size[1])
        self.game_difficulty = game_difficulty
        self.musica.cambiarMusica("../../sounds/opcionesmusica.wav")

    def mostrarPanelCuadrilla(self, game_index):
        self.panelActual = self.partida
        if self.game_difficulty == "Custom":
            self.partida.setNonograma(self.game_difficulty + '/' + self.custom_puzzles[game_index-1])
        else:
            self.partida.setNonograma(self.game_difficulty+'/'+self.game_difficulty+'_Nivel'+str(game_index)+'.txt')
        self.partida.fitWindow(self.window_size[0], self.window_size[1])
        self.partida.setVolverBoton(self.game_difficulty)
        self.musica.cambiarMusica("../../sounds/cuadrillamusica.wav")

    def mostrarPanelOpciones(self):
        self.panelActual = self.panelOpciones
        self.panelOpciones.fitWindow(self.window_size[0], self.window_size[1])
        self.musica.cambiarMusica("../../sounds/opcionesmusica.wav")

    def mostrarPanelFileManager(self):
        self.panelActual = self.panelFileManager
        self.panelFileManager.fitWindow(self.window_size[0], self.window_size[1])

    def updateFileManager(self):
        self.panelFileManager.updateButtons()

    def getMusica(self):
        return self.musica

    def getWindow(self):
        return self.window

    def getWindowSize(self):
        return self.window_size

