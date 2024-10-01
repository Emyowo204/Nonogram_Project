import pygame
from src.main.classes.visuals.ImageLoader import ImageLoader
from src.main.classes.visuals.Panel import Panel


class Juego:


    def start(self):
        pygame.init()
        grid_size = 10
        cell_size = 30
        window_size = grid_size * cell_size
        window = pygame.display.set_mode((window_size,window_size))
        clock = pygame.time.Clock()

        running = True
        while running:
            deltatime =  clock.tick(60)/1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            panel = Panel(0,0,25,25)
            image = ImageLoader().getImage()
            panel.setImage(image)

            window.fill((0,0,0))
            panel.draw(window)
            pygame.display.flip()
        pygame.quit()