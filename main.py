import pygame

#Iniciando Pygame
pygame.init()

#Iniciando ventana
screen = pygame.display.set_mode(size=(540,920))
pygame.display.set_caption("Proyecto Programado")

#Iniciando ciclo
running = True

while running:

    mouse = False

    screen.fill((0,250,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = True
            if mouse == True :
                screen.fill((0,0,0))
                running = False
                

    pygame.display.update()

pygame.display.quit()
