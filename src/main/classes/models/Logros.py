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
            self.achievements = []
            for i in range(10):
                self.achievements.append(0)
            Logros._inicializado = True

    def completeAchievement(self, index):
        """
        Completa un logro indicado.
        :param index: índice del logro completado.
        """
        self.achievements[index] = 1
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
        for i in range(len(saveAchiv)):
            self.achievements[i] = int(saveAchiv[i])

    def saveInfoGame(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        fulldirectory = os.path.join(current_dir, '..','..','info_game.txt')
        try:
            archivo = open(fulldirectory,'w')
        except OSError:
            return False
        for i in range(len(self.achievements)):
            archivo.write(f"{int(self.achievements[i])} ")
        archivo.close()

    def getAchievements(self):
        return self.achievements

    def getAchievement(self, index):
        return self.achievements[index]