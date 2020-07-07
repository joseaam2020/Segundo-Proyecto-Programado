import pygame

#Creating the game
pygame.init()

#Creating Screen
screen = pygame.display.set_mode((800,600))#Takes in Height and width
pygame.display.set_caption("Proyecto Programado")

#Icono icon = pygame.image.load("name of the image") and pygame.display.set_icon(icon)

#Game Loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0,255,0))
    pygame.display.update()

#Prueba 2
