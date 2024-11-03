import os

class FileManager:

    def __init__(self):
        self.currentdir = os.path.expanduser('~')
        self.file_list = []
        self.folder_list = []
        self.valid_images = {".jpg", ".jpeg", ".png", ".bmp", ".tiff", ".webp"}

    def enterPath(self, path):
        path = os.path.expanduser(path)
        if os.path.isdir(path):
            path = os.path.normpath(path)
            self.currentdir = path

    def getCurrentDir(self):
        return self.currentdir

    def updateFoldersAndImages(self):
        self.file_list = os.listdir(self.currentdir)
        valid_files = []
        valid_folders = []
        for file in self.file_list:
            full_path = os.path.join(self.currentdir, file)
            if not os.path.isdir(full_path):
                extension = os.path.splitext(file)[1]
                extension = extension.lower()
                if extension in self.valid_images:
                    valid_files.append(file)
            else:
                valid_folders.append(file)
        self.folder_list = valid_folders
        self.file_list = valid_files

    def getFolders(self):
        return self.folder_list

    def getImages(self):
        return self.file_list

    def print(self):
        print(self.currentdir,self.file_list)