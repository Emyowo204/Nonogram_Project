import pygame

from src.main.classes.visuals.Panel import Panel

class PanelMenu(Panel):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)

    def draw(self, dest_surface):
        dest_surface.fill((0, 0, 0)) # panel en negro por mientras

