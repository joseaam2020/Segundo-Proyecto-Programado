
import pygame
import player

pygame.init()


ancho_ventana = 640
alto_ventana = 480
screen = pygame.display.set_mode((ancho_ventana, alto_ventana))
pygame.display.set_caption("Prueba de Sprites")
clock = pygame.time.Clock()
player = player.Escudero((ancho_ventana/2, alto_ventana))
fin = False

while fin == False:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fin = True

    player.handle_event(event)
    screen.fill(pygame.Color('gray'))
    screen.blit(player.image, player.rect)

    pygame.display.flip()
    clock.tick(2)

pygame.quit ()
