import os

class FileManager:

    def __init__(self):
        self.currentdir = os.path.expanduser('~')
        self.file_list = []
        self.folder_list = []
        self.valid_images = {".jpg", ".jpeg", ".png", ".bmp", ".tiff", ".webp"}
        self.puzzles = []

    def changeDir(self, path):
        path = os.path.expanduser(path)
        if os.path.isdir(path):
            path = os.path.normpath(path)
            self.currentdir = path

    def getCurrentDir(self):
        return self.currentdir

    def updateDir(self):
        self.file_list = os.listdir(self.currentdir)
        valid_files = []
        valid_folders = []
        valid_puzzles = []
        for file in self.file_list:
            full_path = os.path.join(self.currentdir, file)
            if not os.path.isdir(full_path):
                extension = os.path.splitext(file)[1]
                extension = extension.lower()
                if extension == ".txt":
                    valid_puzzles.append(file)
                elif extension in self.valid_images:
                    valid_files.append(file)
            else:
                valid_folders.append(file)
        self.folder_list = valid_folders
        self.file_list = valid_files
        self.puzzles = valid_puzzles

    def getFolders(self):
        return self.folder_list

    def getImages(self):
        return self.file_list

    def getPuzzles(self):
        return self.puzzles

    def print(self):
        print(self.currentdir,self.file_list)