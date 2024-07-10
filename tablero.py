import pygame # type: ignore
Ancho,Altura = 640, 640
Filas,Columnas = 6, 6 
Tamano_Cuadrado = Ancho//Columnas

Beige = "#FFE4C4"
Café = "#8c564b"
Azul = "#61c4ff"
Blanco = "#e1e1e1"
Negro = "#1e1e1e"

Corona = pygame.transform.scale(pygame.image.load("corona.png"),(45,25))

class piezas:
    Relleno = 15
    Borde = 2
    def __init__(self,fil,col,color):
        self.fil = fil
        self.col = col
        self.color = color
        self.king = False#Pieza reina que llega al otro extremo
        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = Tamano_Cuadrado * self.col + Tamano_Cuadrado // 2
        self.y = Tamano_Cuadrado * self.fil + Tamano_Cuadrado // 2

    def make_king(self):
        self.king = True
    def draw(self,win):
        radio = Tamano_Cuadrado//2 - self.Relleno
        pygame.draw.circle(win, Negro, (self.x, self.y), radio + self.Borde)
        pygame.draw.circle(win, self.color, (self.x, self.y), radio)
        if self.king:
            win.blit(Corona, (self.x - Corona.get_width()//2, self.y - Corona.get_height()//2))

    def move(self, fil, col):
        self.fil = fil
        self.col = col
        self.calc_pos()

    def __repr__(self):
        return str(self.color)

class tablero:
    def __init__(self):
        self.tablero = []
        self.Beige_left = self.Blanco_left = 9
        self.Beige_kings = self.Blanco_kings = 0
        self.crear_tablero()
    
    def draw_Cuadrado(self,win):
        win.fill(Café)
        for fil in range(Filas):
            for col in range(fil % 2, Columnas,2 ):
                pygame.draw.rect(win,Beige, (fil))