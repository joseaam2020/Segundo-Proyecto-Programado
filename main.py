import pygame

#Iniciando Pygame y Clock
clock = pygame.time.Clock()
pygame.init()

#Iniciando ventana
window_size = (360,450)
screen = pygame.display.set_mode(size=window_size)
pygame.display.set_caption("Proyecto Programado")

#Creando Superficie 
display = pygame.Surface((120,150))

#Iniciando ciclo
running = True

#Cargando Mapa
def mapa(archivo):
    copia = open(archivo+".txt")
    mapa = copia.read()
    copia.close
    return(mapa) 

#Cargando Imagenes 
casilla1 = pygame.image.load("Tiles1/frames/floor_1.png").convert()
casilla2 = pygame.image.load("Tiles1/frames/floor_1.png").convert()
pared_izquierda = pygame.image.load("Tiles1/frames/wall_side_front_left.png").convert()
pared_derecha = pygame.image.load("Tiles1/frames/wall_side_front_right.png").convert()

#pared_izquierda.set_colorkey(())

#Cargando Mapas
primer_escenario = mapa("mapa")
primer_escenario = primer_escenario.split()


#Ciclo de juego
while running:

    mouse = False

    #Reiniciando pantalla
    screen.fill((0,250,0))

    #Reiniciando escenario
    y = 0
    for fila in primer_escenario:
        x = 0
        for columna in fila:
            if columna == '0':
                display.blit(casilla1,(x*16,y*16))
            if columna == '1':
                display.blit(pared_izquierda,(x*16,y*16))
            if columna == '2':
                display.blit(pared_derecha,(x*16,y*16))
            x += 1
        y += 1
        
    #Ciclo de Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = True
            if mouse == True :
                running = False


    screen.blit(pygame.transform.scale(display,(window_size)),(0,0))#Tansformando superficie a la escala de la ventana
    pygame.display.update()#Cargando Pantalla
    clock.tick(60)

pygame.display.quit()
