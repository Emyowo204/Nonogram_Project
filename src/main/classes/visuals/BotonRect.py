import pygame

from src.main.classes.visuals.ImageLoader import ImageLoader

class BotonRect:
    """
    Clase que representa un botón rectangular general. Puede ser reajustado según el
    tamaño de la ventana y al ser inicializado.

    Variables:
        coord (list): Lista que contiene las coordenadas (x, y)
        size (list): Lista que contiene el valor del ancho y largo del botón.
        rect (Rect): Rectángulo que representa el botón.
        OgNormalImage (image): Imagen original del botón, es decir, al no tener mouse sobre él y de tamaño original.
        OgShadedImage (image): Imagen original con el mouse sobre el botón, es decir, de tamaño original.
        normalImage (image): Imagen reajustada al tamaño del botón sin el mouse sobre este.
        shadedImage (image): Imagen reajustada al tamaño del botón con el mouse sobre este.
        currentImage (image): Imagen actual del botón según su estado.
        action (function): Acción el botón al ser presionado.
        pressed (boolean): Estado actual del botón, si está presionado o no.

    Métodos:
        __init__(x, y, width, height, action): Inicializa el Botón Rectangular.
        evento(event): Administra los eventos del botón.
        setSize(): Designa el nuevo tamaño del botón.
        serCoord(): Designa las coordenadas (x, y) de posición del botón.
        getSize(): Retorna el tamaño actual del botón.
        draw(dest_surface): Dibuja el botón.
    """
    def __init__(self, x, y, width, height, action, *arguments):
        self.coord = [x, y]
        self.size = [width, height]
        self.rect = pygame.Rect(x, y, width, height)
        self.OgNormalImage = ImageLoader().getDefaultImage()
        self.OgShadedImage = self.OgNormalImage
        self.normalImage = pygame.transform.scale(self.OgNormalImage, (width, height))
        self.shadedImage = pygame.transform.scale(self.OgShadedImage, (width, height))
        self.currentImage = self.normalImage
        self.action = action
        self.arguments = arguments
        self.pressed = False
        self.enabled = True


    def evento(self, event):
        """
        Maneja los eventos del botón.
        :param event: Objeto de evento que contiene la información relacionada al evento a procesar.
        """
        if self.enabled:
            if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos) and pygame.mouse.get_pressed()[0]:
                self.pressed = True
            elif event.type == pygame.MOUSEBUTTONUP and self.pressed:
                if self.action:
                    if self.arguments[0] is None:
                        self.action()
                    elif len(self.arguments) == 1:
                        self.action(self.arguments[0])  # Single argument call
                    else:
                        self.action(*self.arguments)
                    self.pressed = False
            elif event.type == pygame.MOUSEBUTTONUP and self.rect.collidepoint(event.pos):
                self.currentImage = self.shadedImage
                self.pressed = False
            elif not self.rect.collidepoint(pygame.mouse.get_pos()):
                self.currentImage = self.normalImage
                self.pressed = False

    def setImage(self, normalImage, shadedImage):
        """
        Designa las imagenes del botón cuando el mouse está fuera y adentro del mismo.
        :param normalImage: Imagen normal nueva del botón.
        :param shadedImage: Imagen opaca nueva del botón.
        """
        self.OgNormalImage = normalImage
        self.OgShadedImage = shadedImage
        self.normalImage = pygame.transform.scale(normalImage, (self.size[0], self.size[1]))
        self.shadedImage = pygame.transform.scale(shadedImage, (self.size[0], self.size[1]))

    def setAction(self,action, *arguments):
        self.action = action
        self.arguments = arguments

    def setSize(self,width, height):
        """
        Designa el tamaño del botón con los parámetros entregados.
        :param width: Ancho a modificar.
        :param height: Largo a modificar.
        """
        self.rect = pygame.Rect(self.coord[0], self.coord[1],width, height)
        self.normalImage = pygame.transform.scale(self.OgNormalImage, (width, height))
        self.shadedImage = pygame.transform.scale(self.OgShadedImage, (width, height))
        self.size = [width, height]

    def setCoord(self,x,y):
        """
        Designa las coordenadas de posición del botón con los parámetros entregados.
        :param x: Posición x nueva del botón.
        :param y: Posición y nueva del botón.
        """
        self.rect = pygame.Rect(x, y, self.size[0], self.size[1])
        self.coord = [x, y]

    def setValues(self,x,y,width,height):
        self.setSize(width,height)
        self.setCoord(x,y)

    def setEnable(self, bool):
        self.enabled = bool

    def isEnabled(self):
        return self.enabled

    def draw(self, screen):
        """
        Dibuja el botón.
        :param screen: Pantalla en donde se dibuja el botón.
        """
        mouse = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse):
            self.currentImage = self.shadedImage
        else:
            self.currentImage = self.normalImage
        screen.blit(self.currentImage, (self.rect.x, self.rect.y))