
import pygame
import player
import rook_class
from random import *
pygame.init()

ancho_ventana = 640
alto_ventana = 480
screen = pygame.display.set_mode((ancho_ventana, alto_ventana))
pygame.display.set_caption("Prueba de Sprites")
clock = pygame.time.Clock()
Escudero = player.Escudero((ancho_ventana/2, alto_ventana/2),0.6,5)
canibal=player.Caníbal(((ancho_ventana/2), alto_ventana))
arquero= player.Flechador(((ancho_ventana/2), alto_ventana/2))
leñador= player.Leñador(((ancho_ventana/2), (alto_ventana/2)+80))
Avatar=[Escudero,canibal,arquero,leñador]
avatar=pygame.sprite.Group()
avatar.add(canibal,leñador)
avatar1=pygame.sprite.Group()
avatar1.add(Escudero)
a=range(0,3)
#shuffle(Avatar)
fin = False

while fin == False:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fin = True

    screen.fill(pygame.Color('gray'))
    Avatar[0].handle_event(event,avatar)
    screen.blit(Avatar[0].image, Avatar[0].rect)
    Avatar[3].handle_event(event,avatar1)
    screen.blit(Avatar[3].image, Avatar[3].rect)
    pygame.display.flip()
    clock.tick(60)

pygame.quit ()
