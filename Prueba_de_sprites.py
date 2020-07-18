
import pygame
import player
from random import *

pygame.init()

ancho_ventana = 640
alto_ventana = 480
screen = pygame.display.set_mode((ancho_ventana, alto_ventana))
pygame.display.set_caption("Prueba de Sprites")
clock = pygame.time.Clock()
Escudero = player.Escudero((ancho_ventana/2, alto_ventana))
canibal=player.Caníbal(((ancho_ventana/2), alto_ventana))
arquero= player.Flechador(((ancho_ventana/2), alto_ventana))
leñador= player.Leñador(((ancho_ventana/2), alto_ventana))
Avatar=[Escudero,canibal,arquero,leñador]
a=range(0,3)
shuffle(Avatar)
fin = False

while fin == False:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fin = True

    screen.fill(pygame.Color('gray'))
    Avatar[0].handle_event(event)
    screen.blit(Avatar[0].image, Avatar[0].rect)
    pygame.display.flip()
    clock.tick(5)

pygame.quit ()
