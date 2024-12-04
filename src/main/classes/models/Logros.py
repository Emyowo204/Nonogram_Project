import os

class Logros:

    _instancia = None
    _inicializado = False
    def __new__(cls, *args, **kwargs):
        if cls._instancia is None:
            cls._instancia = super(Logros, cls).__new__(cls)
        return cls._instancia

    def __init__(self):
        if not self._inicializado:
            self.achievements = 0
            self.levelsCompleted = [[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
            self.allLevels = [[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
            self.achivCount = 8
            Logros._inicializado = True
            self.juego = None

    def completeAchievement(self, bitNum):
        """
        Completa un logro indicado.
        :param bitNum: índice del logro completado.
        """
        if self.achievements & (1<<bitNum) == 0:
            self.readInfoGame()
            self.achievements = self.achievements | (1<<bitNum)
            self.saveInfoGame()
            self.juego.sonido.play("main/sounds/logrosound.wav")

    def sumLevel(self, mode, difficulty, level):
        if self.levelsCompleted[mode][difficulty] & (1<<level) == 0:
            self.readInfoGame()
            self.levelsCompleted[mode][difficulty] = self.levelsCompleted[mode][difficulty] | (1<<level)
            count = 0
            for i in range(3):
                if self.levelsCompleted[mode][i] == self.allLevels[mode][i]:
                    count += 1
            if count==3:
                self.completeAchievement(mode+2)
            self.saveInfoGame()

    def readInfoGame(self):
        fulldirectory = 'main/info_game.txt'
        try:
            archivo = open(fulldirectory,'r')
        except OSError:
            return False
        saveAchiv = archivo.readline().strip().split()
        archivo.close()
        if len(saveAchiv) != 13:
            archivo = open(fulldirectory, 'w')
            for j in range(13):
                archivo.write(f"{0} ")
            archivo.close()
            saveAchiv = [0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.achievements = int(saveAchiv[0])
        index = 1
        for i in range(4):
            for j in range(3):
                self.levelsCompleted[i][j] = int(saveAchiv[index])
                index += 1

    def saveInfoGame(self):
        fulldirectory = 'main/info_game.txt'
        try:
            archivo = open(fulldirectory,'w')
        except OSError:
            return False
        archivo.write(f"{int(self.achievements)} ")
        for i in range(4):
            for j in range(3):
                archivo.write(f"{int(self.levelsCompleted[i][j])} ")
        archivo.close()

    def getAchievements(self):
        return self.achievements

    def getAchievCount(self):
        return self.achivCount

    def setAllLevelsCount(self, num, mode, difficulty):
        for i in range(num):
            self.allLevels[mode][difficulty] = self.allLevels[mode][difficulty] | (1<<i)

    def setJuego(self, juego):
        self.juego = juego

