import pygame

from src.main.classes.visuals.BotonRect import BotonRect
from src.main.classes.visuals.ImageLoader import ImageLoader
from src.main.classes.visuals.Panel import Panel

class PanelOpciones(Panel):
    def __init__(self, x, y, width, height, juego):
        super().__init__(x, y, width, height)
        self.juego = juego

        self.slider= pygame.Rect(x+50, y+50, 20, 50) # thumb para arrastrar
        self.slideando = False
        self.sliderMinX = x + 50
        self.sliderMaxX = x + 250
        self.sliderBackWidth = 250 # barra fondo
        self.sliderBackHeight = 20 # barra fondo
        volumenInicial = 0.5
        self.slider.x = int(self.sliderMinX + (self.sliderMaxX - self.sliderMinX) * volumenInicial)
        self.normalImage = pygame.image.load('../images/botonNormal.png')
        self.shadedImage = pygame.image.load('../images/botonShaded.png')
        self.botonVolver = BotonRect(300, 300, 40, 40, self.normalImage, self.shadedImage, self.juego.mostrarPanelMenu)

    def evento(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.slider.collidepoint(event.pos):
            self.slideando = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.slideando = False
        elif event.type == pygame.MOUSEMOTION and self.slideando:
            self.slider.x = max(self.sliderMinX, min(event.pos[0], self.sliderMaxX))
        self.botonVolver.evento(event)
        nuevoVolumen = (self.slider.x - (self.x +50)) / 200
        self.juego.getMusica().setVolumen(nuevoVolumen)

    def draw(self, dest_surface):
        dest_surface.fill((0, 0, 0,)) # panel en negro por mientras
        self.botonVolver.draw(self.juego.getWindow())

        pygame.draw.rect(dest_surface, (0, 255, 0), (self.sliderMinX, self.y+65, (self.slider.x - self.sliderMinX), self.sliderBackHeight))  # fondo slider

        pygame.draw.rect(dest_surface, (100, 100, 100), (self.slider.x, self.y+65, (self.sliderMaxX - self.slider.x + self.slider.width), self.sliderBackHeight))  # fondo slider

        pygame.draw.rect(dest_surface, (255, 0, 0), self.slider)  # dibujo thumb

        # texto prueba
        font = pygame.font.Font(None, 24)
        volumenTexto = font.render(f"Volumen: {int(self.juego.getMusica().getVolumen() * 100)}%", True, (255, 255, 255))
        dest_surface.blit(volumenTexto, (self.sliderMinX, self.y + 100))
