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
            self.levelsCompleted = [0,0,0,0]
            self.allLevels = [0, 0, 0, 0]
            self.achivCount = 10
            Logros._inicializado = True

    def completeAchievement(self, bitNum):
        """
        Completa un logro indicado.
        :param bitNum: índice del logro completado.
        """
        if self.achievements & (1<<bitNum) == 0:
            self.readInfoGame()
            self.achievements = self.achievements | (1<<bitNum)
            self.saveInfoGame()

    def sumLevel(self, mode, level):
        if self.levelsCompleted[mode] & (1<<level) == 0:
            self.readInfoGame()
            self.levelsCompleted[mode] = self.levelsCompleted[mode] | (1<<level)
            if self.levelsCompleted[mode] == self.allLevels[mode]:
                self.completeAchievement(mode+2)
            self.saveInfoGame()

    def readInfoGame(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        fulldirectory = os.path.join(current_dir, '..','..','info_game.txt')
        try:
            archivo = open(fulldirectory,'r')
        except OSError:
            return False
        saveAchiv = archivo.readline().strip().split()
        archivo.close()
        self.achievements = int(saveAchiv[0])
        for i in range(4):
            self.levelsCompleted[i] = int(saveAchiv[i+1])

    def saveInfoGame(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        fulldirectory = os.path.join(current_dir, '..','..','info_game.txt')
        try:
            archivo = open(fulldirectory,'w')
        except OSError:
            return False
        archivo.write(f"{int(self.achievements)} ")
        for i in range(4):
            archivo.write(f"{int(self.levelsCompleted[i])} ")
        archivo.close()

    def getAchievements(self):
        return self.achievements

    def getAchievCount(self):
        return self.achivCount

    def setAllLevelsCount(self, num, index):
        for i in range(num):
            self.allLevels[index] = self.allLevels[index] | (1<<(i+1))
        print(f'{self.allLevels[index]}')


