import pygame

pygame.init()

font15 = pygame.font.SysFont('berlinsansfbdemi', 15)

class InputBox():
    def __init__(self,font,color,posicion,maxlen):
        self.font = font
        self.color = color
        self.posicion = posicion
        self.contenido = ''
        self.maxlen = maxlen

    def render_box(self,superficie):
        superficie_texto = self.font.render(self.contenido,True,self.color)
        textorect = superficie_texto.get_rect()
        self.superficie = pygame.Surface((textorect.width,textorect.height))
        self.superficie.fill((0,0,0))
        self.superficie.blit(superficie_texto,(5,5))
        superficie.blit(superficie_texto,self.posicion)

    def escribir(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self.contenido = self.contenido[:-1]
                else:
                    if len(self.contenido) < self.maxlen:
                        self.contenido += event.unicode

#Iniciando ventana
ancho_ventana=400
alto_ventana=480
window_size = (400,480)
screen = pygame.display.set_mode(size=window_size)
pygame.display.set_caption("Proyecto Programado")

ib = InputBox(font15,(0,0,0),(100,100),10)

while True:

    screen.fill((255,255,255))

    
    ib.escribir()
    ib.render_box(screen)

    pygame.display.update()
