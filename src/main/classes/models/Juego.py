import os

import pygame

from src.main.classes.models.FileManager import FileManager
from src.main.classes.models.Logros import Logros
from src.main.classes.visuals.PanelFileManager import PanelFileManager
from src.main.classes.visuals.PanelNivelCustom import PanelNivelesCustom
from src.main.classes.visuals.PanelPartida import PanelPartida
from src.main.classes.visuals.ImageLoader import ImageLoader
from src.main.classes.visuals.Panel import Panel
from src.main.classes.visuals.PanelOpciones import PanelOpciones
from src.main.classes.visuals.PanelLogros import PanelLogros
from src.main.classes.visuals.PanelTutorial import PanelTutorial
from src.main.classes.visuals.PanelMenu import PanelMenu
from src.main.classes.visuals.PanelNiveles import PanelNiveles
from src.main.classes.models.Musica import Musica
from src.main.classes.models.Sonido import Sonido
from src.main.classes.visuals.Ventana import Ventana


class Juego:
    def __init__(self):

        Logros().setJuego(self)
        self.filemanager = None
        self.window = None
        self.window_size = [None, None]
        self.panelActual = None
        self.panelAnterior = None
        self.musica = None
        self.sonido = None
        self.panelPartida = None
        self.panelNiveles = None
        self.panelNivelesCustom = None
        self.panelOpciones = None
        self.panelLogros = None
        self.panelTutorial = None
        self.panelMenu = None
        self.panelFileManager = None
        self.custom_puzzles = []
        self.color_puzzles = []
        self.levelsCount = [[0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0]]
        self.difficultyList = ["Easy", "Medium", "Hard", "Custom"]
        self.gameDifficulty = 0
        self.gameMode = 0

    def start(self):
        self.filemanager = FileManager()
        self.contarPuzzles()
        self.window_size = [720, 720]
        ventana = Ventana(self.window_size[0], self.window_size[1])
        self.window = ventana.getWindow()
        pygame.mixer.init()
        self.musica = Musica("../../sounds/menumusica.wav")
        self.sonido = Sonido("../../sounds/sonidotest.wav")

        clock = pygame.time.Clock()
        self.panelMenu = PanelMenu(0,0, self.window_size[0], self.window_size[1], self)
        self.panelPartida = PanelPartida(0, 0, self.window_size[0], self.window_size[1], self)
        self.panelOpciones = PanelOpciones( 0, 0, self.window_size[0], self.window_size[1], self)
        self.panelLogros = PanelLogros(0, 0, self.window_size[0], self.window_size[1], self)
        self.panelTutorial = PanelTutorial(0, 0, self.window_size[0], self.window_size[1], self)
        self.panelNiveles = PanelNiveles( 0, 0, self.window_size[0], self.window_size[1], self)
        self.panelNivelesCustom = PanelNivelesCustom( 0, 0, self.window_size[0], self.window_size[1], self)
        self.panelFileManager = PanelFileManager(0,0,self.window_size[0], self.window_size[1],self)
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
                    Logros().readInfoGame()
                    Logros().saveInfoGame()
                    running = False

                elif event.type == pygame.VIDEORESIZE:
                        new_size = (event.w,event.h)
                        self.panelActual.fitWindow(new_size[0], new_size[1])
                        self.window_size = new_size
                elif event.type == pygame.MOUSEMOTION:
                    pos = event.pos

                if self.panelActual == self.panelPartida:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1 or event.button == 3:
                            is_pressed = True

                    elif event.type == pygame.MOUSEBUTTONUP:
                        if event.button == 1 or event.button == 3:
                            is_pressed = False
                            self.panelPartida.setIsPressed(is_pressed)

                    elif event.type == pygame.KEYDOWN and self.gameMode%2==1:
                        self.panelActual.handleKey(event)

                    if is_pressed:
                        self.panelActual.handleClick(pos, pygame.mouse.get_pressed()[2])
                    if event.type == pygame.MOUSEWHEEL:
                        self.panelActual.handleZoom(event, pos)
                self.panelActual.evento(event)

            panel = Panel(0,0,25,25)
            image = ImageLoader().getDefaultImage()
            panel.setImage(image)

            self.panelActual.draw(self.window)

            if self.panelActual == self.panelOpciones or self.panelActual == self.panelFileManager or self.panelActual == self.panelNivelesCustom:
                self.panelActual.actualizar(deltatime)

            self.window.fill((255,255,255))
            self.panelActual.draw(self.window)

            pygame.display.flip()

        pygame.quit()

    def contarPuzzles(self):
        for i in range(4):
            for j in range(3):
                self.filemanager.changeDir(os.path.join(os.getcwd(), "../puzzles"+str(i)+"/"+self.difficultyList[j]))
                self.filemanager.updateDir()
                self.levelsCount[i][j] = len(self.filemanager.getPuzzles())
                Logros().setAllLevelsCount(self.levelsCount[i][j], i, j)

    def mostrarPanelMenu(self):
        self.panelAnterior = self.panelActual
        self.panelActual = self.panelMenu
        self.panelMenu.fitWindow(self.window_size[0], self.window_size[1])
        self.musica.cambiarMusica("../../sounds/menumusica.wav")

    def mostrarPanelNiveles(self, difficulty_index):
        if difficulty_index == 3:
            self.panelAnterior = self.panelActual
            self.panelActual = self.panelNivelesCustom
            if self.gameMode == 0 or self.gameMode == 2:
                self.panelNivelesCustom.setBinMode()
                self.filemanager.changeDir(
                    os.path.join(os.getcwd(), "../puzzles_custom/" + self.difficultyList[3] + str(0)))
                self.filemanager.updateDir()
                self.custom_puzzles = self.filemanager.getPuzzles()
                self.levelsCount[0][3] = self.levelsCount[2][3] = len(self.custom_puzzles)
            elif self.gameMode == 1 or self.gameMode == 3:
                self.panelNivelesCustom.setColorMode()
                self.filemanager.changeDir(
                    os.path.join(os.getcwd(), "../puzzles_custom/" + self.difficultyList[3] + str(1)))
                self.filemanager.updateDir()
                self.color_puzzles = self.filemanager.getPuzzles()
                self.levelsCount[1][3] = self.levelsCount[3][3] = len(self.color_puzzles)
            self.panelNivelesCustom.fitWindow(self.window_size[0], self.window_size[1])
            self.panelNiveles.setLoadEnable(True)
        else:
            self.panelNiveles.setLoadEnable(False)

            quantity = self.levelsCount[self.gameMode][difficulty_index]
            self.panelNiveles.setLevelButtons(quantity)
            self.panelAnterior = self.panelActual
            self.panelActual = self.panelNiveles
            self.panelNiveles.fitWindow(self.window_size[0], self.window_size[1])
        self.gameDifficulty = difficulty_index
        self.musica.cambiarMusica("../../sounds/nivelesmusica.wav")

    def mostrarPanelCuadrilla(self, game_index):
        self.panelAnterior = self.panelActual
        self.panelActual = self.panelPartida
        diff_name = self.difficultyList[self.gameDifficulty]
        self.panelActual.setVolverBoton(self.gameDifficulty)
        self.panelActual.setLevel(game_index)
        if self.gameDifficulty == 3:
            if self.gameMode == 0 or self.gameMode == 2:
                self.panelPartida.setNonograma(diff_name+'0/'+self.custom_puzzles[game_index-1], self.gameMode, True)
            elif self.gameMode == 1 or self.gameMode == 3:
                self.panelPartida.setNonograma(diff_name + '1/' + self.color_puzzles[game_index - 1], self.gameMode, True)
        else:
            self.panelPartida.setNonograma(diff_name+'/'+diff_name+'_Nivel'+str(game_index)+'.txt', self.gameMode, False)
        self.panelActual.defaultZoom()
        self.panelActual.fitWindow(self.window_size[0], self.window_size[1])
        self.musica.cambiarMusica("../../sounds/cuadrillamusica.wav")

    def mostrarPanelOpciones(self):
        self.panelAnterior = self.panelActual
        self.panelActual = self.panelOpciones
        self.panelOpciones.fitWindow(self.window_size[0], self.window_size[1])
        self.musica.cambiarMusica("../../sounds/opcionesmusica.wav")

    def mostrarPanelLogros(self):
        self.panelAnterior = self.panelActual
        self.panelActual = self.panelLogros
        self.panelLogros.fitWindow(self.window_size[0], self.window_size[1])
        self.panelLogros.reloadAchievement()
        self.musica.cambiarMusica("../../sounds/logrosmusica.wav")

    def mostrarPanelTutorial(self):
        self.panelAnterior = self.panelActual
        self.panelActual = self.panelTutorial
        self.panelTutorial.fitWindow(self.window_size[0], self.window_size[1])
        self.musica.cambiarMusica("../../sounds/tutorialmusica.wav")

    def mostrarPanelFileManager(self):
        self.panelAnterior = self.panelActual
        self.panelActual = self.panelFileManager
        if self.gameMode == 0 or self.gameMode == 2:
            self.panelFileManager.setBinMode()
        elif self.gameMode == 1 or self.gameMode == 3:
            self.panelFileManager.setColorMode()
        self.panelFileManager.fitWindow(self.window_size[0], self.window_size[1])

    def mostrarPanelAnterior(self):
        auxPanel = self.panelActual
        self.panelActual = self.panelAnterior
        self.panelAnterior = auxPanel
        self.panelActual.fitWindow(self.window_size[0], self.window_size[1])
        self.musica.cambiarMusicaPrevia()

    def updateFileManager(self):
        self.panelFileManager.updateButtons()

    def setMode(self, mode):
        self.gameMode = mode

    def getMusica(self):
        return self.musica

    def getWindow(self):
        return self.window

    def getWindowSize(self):
        return self.window_size
