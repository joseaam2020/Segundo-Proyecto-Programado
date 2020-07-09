import pygame

#Iniciando Pygame y Clock
clock = pygame.time.Clock()
pygame.init()

#Iniciando ventana
window_size = (400,500)
screen = pygame.display.set_mode(size=window_size)
pygame.display.set_caption("Proyecto Programado")

#Creando Superficie 
display = pygame.Surface((112,180))

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
pared_izquierda = pygame.image.load("Tiles1/frames/wall_side_mid_left.png").convert()
pared_derecha = pygame.image.load("Tiles1/frames/wall_side_mid_right.png").convert()
pared_centro = pygame.image.load("Tiles1/frames/wall_mid.png").convert()
esquina_izquierda = pygame.image.load("Tiles1/frames/wall_inner_corner_mid_left.png").convert()
esquina_derecha = pygame.image.load("Tiles1/frames/wall_inner_corner_mid_rigth.png").convert()
pared_arriba = pygame.image.load("Tiles1/frames/wall_top_mid.png").convert()
esquina_izquierda_arriba = pygame.image.load("Tiles1/frames/wall_inner_corner_t_top_left.png").convert()
esquina_derecha_arriba = pygame.image.load("Tiles1/frames/wall_inner_corner_t_top_rigth.png").convert()

pared_izquierda.set_colorkey((255,255,255))
pared_derecha.set_colorkey((255,255,255))
esquina_izquierda_arriba.set_colorkey((255,255,255))
esquina_derecha_arriba.set_colorkey((255,255,255))
pared_arriba.set_colorkey((255,255,255))


#pared_izquierda.set_colorkey(())

#Cargando Mapas
primer_escenario = mapa("mapa")
primer_escenario = primer_escenario.split()


#Ciclo de juego
while running:

    mouse = False

    #Reiniciando pantalla
    display.fill((0,0,0))

    #Reiniciando escenario
    y = 0
    for fila in primer_escenario:
        x = 0
        for columna in fila:
            if y > 1: 
                display.blit(casilla1,(x*16,y*16))
            x += 1
        y += 1
    
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
            if columna == '3':
                display.blit(esquina_izquierda,(x*16,y*16))
            if columna == '4':
                display.blit(esquina_derecha,(x*16,y*16))
            if columna == '5':
                display.blit(pared_centro,(x*16,y*16))
            if columna == '6':
                display.blit(pared_arriba,(x*16,y*16))
            if columna == '7':
                display.blit(esquina_izquierda_arriba,(x*16,y*16))
            if columna == '8':
                display.blit(esquina_derecha_arriba,(x*16,y*16))

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
