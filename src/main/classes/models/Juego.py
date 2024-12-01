import os

import pygame

from src.main.classes.models.FileManager import FileManager
from src.main.classes.visuals.PanelFileManager import PanelFileManager
from src.main.classes.visuals.PanelPartida import PanelPartida
from src.main.classes.visuals.PanelPartidaColored import PanelPartidaColored
from src.main.classes.visuals.ImageLoader import ImageLoader
from src.main.classes.visuals.Panel import Panel
from src.main.classes.visuals.PanelOpciones import PanelOpciones
from src.main.classes.visuals.PanelMenu import PanelMenu
from src.main.classes.visuals.PanelNiveles import PanelNiveles
from src.main.classes.models.Musica import Musica
from src.main.classes.visuals.Ventana import Ventana


class Juego:
    def __init__(self):
        
        self.panelPartidaColor = None
        self.filemanager = None
        self.window = None
        self.window_size = [None, None]
        self.panelActual = None
        self.panelAnterior = None
        self.musica = None
        self.panelPartida = None
        self.panelNiveles = None
        self.panelOpciones = None
        self.panelMenu = None
        self.panelFileManager = None
        self.custom_puzzles = []
        self.color_puzzles = []
        self.levelsCount = [0, 0, 0, 0, 0]
        self.difficultyList = ["Easy", "Medium", "Hard", "Custom", "Colored"]
        self.gameDifficulty = 0

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
        self.panelPartida = PanelPartida(0, 0, self.window_size[0], self.window_size[1], self)
        self.panelPartidaColor = PanelPartidaColored(0, 0, self.window_size[0], self.window_size[1], self)
        self.panelOpciones = PanelOpciones( 0, 0, self.window_size[0], self.window_size[1], self)
        self.panelNiveles = PanelNiveles( 0, 0, self.window_size[0], self.window_size[1], self)
        self.panelFileManager = PanelFileManager(0,0,self.window_size[0], 1080,self)
        self.mostrarPanelMenu()
        self.panelFileManager.updateButtons()

        pos = (0,0)
        is_pressed = False
        running = True
        new_size = (720,720)
        self.panelPartida.fitWindow(new_size[0],new_size[1])
        self.panelFileManager.updateButtons()
        while running:
            deltatime = clock.tick(60) / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.VIDEORESIZE:
                        new_size = (event.w,event.h)
                        self.panelActual.fitWindow(new_size[0], new_size[1])
                        self.window_size = new_size
                elif event.type == pygame.MOUSEMOTION:
                    pos = event.pos

                if self.panelActual == self.panelPartida:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            is_pressed = True
                    elif event.type == pygame.MOUSEBUTTONUP:
                        if event.button == 1:
                            is_pressed = False

                    if is_pressed:
                        self.panelPartida.handleClick(pos)

                    if event.type == pygame.MOUSEWHEEL:
                        self.panelPartida.handleZoom(event, pos)
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
        for i in range(3):
            self.filemanager.changeDir(os.path.join(os.getcwd(), "../puzzles/"+self.difficultyList[i]))
            self.filemanager.updateDir()
            self.levelsCount[i] = len(self.filemanager.getPuzzles())

    def mostrarPanelMenu(self):
        self.panelAnterior = self.panelActual
        self.panelActual = self.panelMenu
        self.panelMenu.fitWindow(self.window_size[0], self.window_size[1])
        self.musica.cambiarMusica(None)

    def mostrarPanelNiveles(self, difficulty_index):
        if difficulty_index == 3:
            self.filemanager.changeDir(os.path.join(os.getcwd(), "../puzzles/" + self.difficultyList[3]))
            self.filemanager.updateDir()
            self.custom_puzzles = self.filemanager.getPuzzles()
            self.levelsCount[3] = len(self.custom_puzzles)
            self.panelNiveles.setLoadEnable(True)
        elif difficulty_index == 4:
            self.filemanager.changeDir(os.path.join(os.getcwd(), "../puzzles/" + self.difficultyList[4]))
            self.filemanager.updateDir()
            self.color_puzzles = self.filemanager.getPuzzles()
            self.levelsCount[4] = len(self.color_puzzles)
            self.panelNiveles.setLoadEnable(True)
        else:
            self.panelNiveles.setLoadEnable(False)
        quantity = self.levelsCount[difficulty_index]
        self.panelNiveles.setLevelButtons(quantity)
        self.panelAnterior = self.panelActual
        self.panelActual = self.panelNiveles
        self.panelNiveles.fitWindow(self.window_size[0], self.window_size[1])
        self.gameDifficulty = difficulty_index
        self.musica.cambiarMusica("../../sounds/opcionesmusica.wav")

    def mostrarPanelCuadrilla(self, game_index):
        self.panelAnterior = self.panelActual
        self.panelActual = self.panelPartida
        diff_name = self.difficultyList[self.gameDifficulty]
        if self.gameDifficulty == 3:
            self.panelPartida.setNonograma(diff_name+'/'+self.custom_puzzles[game_index-1])
        elif self.gameDifficulty == 4:
            self.panelActual = self.panelPartidaColor
            self.panelPartidaColor.setNonograma(diff_name + '/' + self.color_puzzles[game_index - 1])
        else:
            self.panelPartida.setNonograma(diff_name+'/'+diff_name+'_Nivel'+str(game_index)+'.txt')
        self.panelActual.defaultZoom()
        self.panelActual.fitWindow(self.window_size[0], self.window_size[1])
        self.panelActual.setVolverBoton(self.gameDifficulty)
        self.musica.cambiarMusica("../../sounds/cuadrillamusica.wav")

    def mostrarPanelOpciones(self):
        self.panelAnterior = self.panelActual
        self.panelActual = self.panelOpciones
        self.panelOpciones.fitWindow(self.window_size[0], self.window_size[1])
        self.musica.cambiarMusica("../../sounds/opcionesmusica.wav")

    def mostrarPanelFileManager(self):
        self.panelAnterior = self.panelActual
        self.panelActual = self.panelFileManager
        self.panelFileManager.fitWindow(self.window_size[0], self.window_size[1])

    def mostrarPanelAnterior(self):
        auxPanel = self.panelActual
        self.panelActual = self.panelAnterior
        self.panelAnterior = auxPanel
        self.panelActual.fitWindow(self.window_size[0], self.window_size[1])
        self.musica.cambiarMusicaPrevia()

    def updateFileManager(self):
        self.panelFileManager.updateButtons()

    def getMusica(self):
        return self.musica

    def getWindow(self):
        return self.window

    def getWindowSize(self):
        return self.window_size

