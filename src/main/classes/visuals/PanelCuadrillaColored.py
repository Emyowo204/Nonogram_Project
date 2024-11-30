import pygame

from src.main.classes.visuals.Panel import Panel

class PanelCuadrillaColored(Panel):
    """
        Clase que representa un panel para mostrar el tablero del nonograma colorido.
        Esta clase permite interactuar con el nonograma, realizando clicks y zoom.
        Hereda de la clase Panel para gestionar el panel gráfico y su métodos.

        Variables:
            cell_size (float): Tamaño de las celdas del tablero.
            size (tuple): Dimensiones del tablero (número de filas y columnas).
            board (list): El estado actual del tablero en formato de matriz.
            colors (list): Lista de los colores del nonograma.
            zoom_x (float): Zoom aplicado al tablero.
            draw_xoffset (float): Desplazamiento horizontal para el dibujado.
            draw_yoffset (float): Desplazamiento vertical para el dibujado.

        Métodos:
            __init__(cuadrilla, x, y, size): Inicializa el panel y le da sus configuraciones inciiales de tamaño.
            setNewCuadrilla(cuadrilla): Actualiza el tablero.
            positionClick(pos): Convierte las coordenadas de un clic en una posición (col, row) dentro del tablero.
            handleClick(pos): Gestiona el clic del usuario sobre el tablero y cambia el estado de la celda seleccionada.
            handleZoom(event, pos): Maneja el zoom sobre el tablero utilizando la rueda del mouse.
            defaultZoom(): Restaura el zoom al valor predeterminado.
            calculate_cellSize(size): Calcula el tamaño de las celdas en función del tamaño del panel.
            fitWindow(size): Ajusta el panel al tamaño proporcionado y calcula el tamaño de las celdas.
            draw(dest_surface): Dibuja el tablero, con colores dependiendo del estado de las celdas.
            getXOffset(): Getter del desplazamiento horizontal del tablero.
            getYOffset(): Getter del desplazamiento vertical del tablero.
            getZoom(): Getter  del nivel de zoom actual del tablero.
        """
    def __init__(self,cuadrilla_colored,x,y,size):
        """
            Inicializa un panel con una cuadrilla dada y la posición y tamaño especificados.

            Args:
                cuadrilla (Cuadrilla): Cuadrilla que contiene el estado del tablero.
                x (int): Coordenada X de la posición del panel en la ventana.
                y (int): Coordenada Y de la posición del panel en la ventana.
                size (int): Tamaño del panel (anchura y altura).
        """
        super().__init__(x, y, size, size)
        self.cell_size = 0
        self.size = cuadrilla_colored.getSize()
        self.board = cuadrilla_colored.getBoard()
        self.colors = cuadrilla_colored.getColors()
        self.selected_color = 1
        self.fitWindow(size)
        self.zoom_x = 1
        self.draw_xoffset = 0
        self.draw_yoffset = 0

    def setBoardColors(self,colors):
        self.colors =  colors

    def getBoardColors(self):
        return self.colors

    def setNewCuadrilla(self, cuadrilla_colored):
        """
            Actualiza el panel con una nueva cuadrilla.

            Args:
                cuadrilla_colored (Cuadrilla): Nueva cuadrilla para actualizar el panel.
        """
        self.size = cuadrilla_colored.getSize()
        self.board = cuadrilla_colored.getBoard()
        self.colors = cuadrilla_colored.getColors()

    def positionClick(self,pos):
        """
            Convierte una posición en la pantalla (pos) a una posición de fila y columna en el tablero.

            Args:
                pos (tuple): Coordenadas (x, y) del clic en la pantalla.

            Returns:
                tuple: (col, row) de la celda seleccionada en el tablero, o (-1, -1) si el clic está fuera del tablero.
        """
        row = int((pos[1] - self.y - self.draw_yoffset) // self.cell_size)
        col = int((pos[0] - self.x - self.draw_xoffset) // self.cell_size)
        if 0 <= col < self.size[0] and 0 <= row < self.size[1]:
            return col,row
        else:
            return -1,-1

    def handleClick(self, pos):
        """
            Maneja el clic del usuario sobre el tablero, cambiando el valor de la celda seleccionada.

            Args:
                pos (tuple): Coordenadas (x, y) del clic.
        """
        col,row = self.positionClick(pos)
        if col != -1 and row != -1:
            if 0 <= col < len(self.board) and 0 <= row < len(self.board[col]):
                current_value = self.board[col][row]
                if current_value != 0:
                    self.board[col][row] = self.selected_color

    def handleKey(self, event):
        """
            Maneja los eventos de presionar teclas del teclado.

            Args:
                event (event): Evento a manejar.
        """
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                self.selected_color = 0
            elif event.key == pygame.K_1:
                self.selected_color = 1
            elif event.key == pygame.K_2:
                self.selected_color = 1
            elif event.key == pygame.K_3:
                self.selected_color = 3

    def getSize(self):
        """
            Getter del tamaño de la cuadrilla.

            Return:
                size (int): Tamaño de la cuadrilla.
        """
        return self.size

    def getCellSize(self):
        """
            Getter del tamaño de lal celdas.

            Return:
                cell_size (int): Tamaño de la celda.
        """
        return self.cell_size

    def handleZoom(self, event, pos):
        """
            Maneja el zoom en el tablero al usar la rueda del mouse.

            Args:
                event (pygame.event): Evento generado por la interacción con la rueda del mouse.
                pos (tuple): Coordenadas (x, y) del evento para ajustar el desplazamiento.
        """
        self.surface = pygame.Surface((self.w,self.h))
        old_zoom_x = self.zoom_x

        if event.y > 0:
            if self.zoom_x < 4:
                self.zoom_x += 0.1

        elif event.y < 0:
            if self.zoom_x > 1:
                self.zoom_x -= 0.1

        if self.zoom_x < 1:
            self.zoom_x = 1
        if self.zoom_x > 4:
            self.zoom_x = 4
        if self.zoom_x == 1:
            self.draw_xoffset = 0
            self.draw_yoffset = 0
            self.calculate_cellSize(self.w)
        else:
            new_cell_size = self.cell_size * (self.zoom_x / old_zoom_x)

            self.draw_xoffset += (pos[0] - self.x - self.draw_xoffset) * (1 - (new_cell_size / self.cell_size))
            self.draw_yoffset += (pos[1] - self.y - self.draw_yoffset) * (1 - (new_cell_size / self.cell_size))

            if self.draw_xoffset > 0 and self.w > (self.size[0] * new_cell_size)/self.w * new_cell_size - self.draw_xoffset:
                self.draw_xoffset = 0
            elif self.draw_xoffset < 0 and self.draw_xoffset + (self.size[0] * new_cell_size) < self.w:
                self.draw_xoffset = -(self.size[0] * new_cell_size - self.w)

            if self.draw_yoffset > 0 and self.h > (self.size[1] * new_cell_size)/self.h * new_cell_size - self.draw_yoffset:
                self.draw_yoffset = 0
            elif self.draw_yoffset < 0 and self.draw_yoffset + (self.size[1] * new_cell_size) < self.h:
                self.draw_yoffset = -(self.size[1] * new_cell_size - self.h)

            self.cell_size = new_cell_size

    def defaultZoom(self):
        """
            Restaura el zoom al valor predeterminado (1x) y ajusta el desplazamiento.
        """
        self.zoom_x = 1
        self.draw_xoffset = 0
        self.draw_yoffset = 0

    def calculate_cellSize(self,size):
        """
            Calcula el tamaño de las celdas en función del tamaño del panel.

            Args:
                size (int): Tamaño total del panel.
        """
        if self.size[0] > self.size[1]:
            self.cell_size = size / self.size[0]
        else:
            self.cell_size = size / self.size[1]

    def fitWindow(self,size):
        """
            Ajusta el tamaño del panel al tamaño proporcionado.

            Args:
                size (int): Tamaño del panel.
        """
        self.w = size
        self.h = size
        self.surface = pygame.Surface((self.w,self.h))
        self.surface.fill((self.red, self.green, self.blue))
        self.calculate_cellSize(size)

    def draw(self, dest_surface):
        """
            Dibuja el tablero, utilizando los colores del nonograma.

        Args:
            dest_surface (pygame.Surface): Superficie sobre la que dibujar el tablero.
        """
        for col in range(self.size[0]):
            for row in range(self.size[1]):
                cell = self.board[col][row]
                color = self.colors[cell]
                if cell == 0:
                    color = [30,30,30]
                pygame.draw.rect(self.surface, color, (col * self.cell_size + self.draw_xoffset, row * self.cell_size + self.draw_yoffset, self.cell_size - 2, self.cell_size - 2))
        super().draw(dest_surface)

    def getXOffset(self):
        """
            Getter del desplazamiento horizontal de la cuadrilla en la ventana.

            Returns:
                float: El desplazamiento horizontal de la cuadrilla.
        """
        return self.draw_xoffset

    def getYOffset(self):
        """
            Getter del desplazamiento vertical de la cuadrilla en la ventana.

            Returns:
                float: El desplazamiento vertical de la cuadrilla.
        """
        return self.draw_yoffset

    def getZoom(self):
        """
            Getter del nivel de zooom actual.

            Returns:
                float: Nivel de zoom actual en la cuadrilla..
        """
        return self.zoom_x

