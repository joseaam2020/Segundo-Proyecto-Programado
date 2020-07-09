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

font = pygame.font.SysFont('berlinsansfbdemi', 20)#tipo de font que se va a utilizar para el menu

#text(texto, font, color, superficie,x,y)
#E: un text, un tipo de font, un color(RGB),una superficie, coordenadas xy
#S: se imprime en texto con el tipo de font y color en  la superficie, coordenadas(x,y)
#R: - 
def texto(texto, font, color, superficie,x,y):
    text = font.render(texto,1,color)
    textrect = text.get_rect()
    textrect.midtop = (x,y)
    superficie.blit(text,textrect)
    return textrect


def menu_principal():
    #Iniciando ciclo
    running = True
    
    #Iniciando ciclo de menu
    while running:

        #Reinciando pantalla
        screen.fill((0,0,0))

        #Creando Texto
        TowerDefense = texto("Tower Defense",font,(255,0,0),screen,200,0)
        Start = texto("Start",font,(255,0,0),screen,200,50)
        Oprit

        #Ciclo de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos_mouse = pygame.mouse.get_pos()
                if Start.collidepoint(pos_mouse):
                    juego()

        pygame.display.update()


#juego()
#E: -
#S: inicia el cliclo de juego
#R: - 
def juego():

    #Iniciando ciclo
    running = True
    
    #Ciclo de juego
    while running:

        mouse = False

        #Reiniciando superficie y pantalla
        screen.fill((0,0,0))
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
                if mouse == True:
                    running = False
                
  

        screen.blit(pygame.transform.scale(display,(window_size)),(0,0))#Tansformando superficie a la escala de la ventana
        pygame.display.update()#Cargando Pantalla
        clock.tick(60)

menu_principal()

pygame.display.quit()

