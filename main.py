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

#Cargando Imagenes del menu
scroll = pygame.image.load("Tiles1/frames1/scroll.png").convert()
scroll.set_colorkey((255,255,255))

#Cargando Imagenes del escenario1
casilla1 = pygame.image.load("Tiles1/frames1/floor_1.png").convert()
casilla2 = pygame.image.load("Tiles1/frames1/floor_1.png").convert()
pared_izquierda = pygame.image.load("Tiles1/frames1/wall_side_mid_left.png").convert()
pared_derecha = pygame.image.load("Tiles1/frames1/wall_side_mid_right.png").convert()
pared_centro = pygame.image.load("Tiles1/frames1/wall_mid.png").convert()
esquina_izquierda = pygame.image.load("Tiles1/frames1/wall_inner_corner_mid_left.png").convert()
esquina_derecha = pygame.image.load("Tiles1/frames1/wall_inner_corner_mid_rigth.png").convert()
pared_arriba = pygame.image.load("Tiles1/frames1/wall_top_mid.png").convert()
esquina_izquierda_arriba = pygame.image.load("Tiles1/frames1/wall_inner_corner_t_top_left.png").convert()
esquina_derecha_arriba = pygame.image.load("Tiles1/frames1/wall_inner_corner_t_top_rigth.png").convert()

pared_izquierda.set_colorkey((255,255,255))
pared_derecha.set_colorkey((255,255,255))
esquina_izquierda_arriba.set_colorkey((255,255,255))
esquina_derecha_arriba.set_colorkey((255,255,255))
pared_arriba.set_colorkey((255,255,255))

#Cargando Imagenes del escenario2
casilla3 = pygame.image.load("Tiles1/frames2/tile155.png").convert()
casilla4 = pygame.image.load("Tiles1/frames2/tile221.png").convert()
arbusto = pygame.image.load("Tiles1/frames2/tile69.png").convert()

arbusto.set_colorkey((255,255,255)) 

#Cargando imagenes de avatares
escudero=pygame.image.load('Tiles1/frames1/knight_m_idle_anim_f0.png')
#pared_izquierda.set_colorkey(())

#Cargando Mapas
primer_escenario = mapa("mapa")
primer_escenario = primer_escenario.split()

#Creand fonts 
font40 = pygame.font.SysFont('berlinsansfbdemi', 40)
font35 = pygame.font.SysFont('berlinsansfbdemi', 35)
font30 = pygame.font.SysFont('berlinsansfbdemi', 30)
font15 = pygame.font.SysFont('berlinsansfbdemi', 15)

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

        #Reiniciando pantalla
        screen.fill((0,0,0))

        #Inciando Escenario de fondo
        escenario()

        #Creando Texto
        TowerDefense = texto("Tower Defense",font40,(255,255,255),screen,200,50)
        Iniciar = texto("Iniciar",font35,(255,255,255),screen,200,100)
        Opciones = texto("Opciones",font35,(255,255,255),screen,200,150)
        Creditos = texto("Creditos",font35,(255,255,255),screen,200,200)

        #Ciclo de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos_mouse = pygame.mouse.get_pos()
                
                if Iniciar.collidepoint(pos_mouse):
                    juego()
                if Opciones.collidepoint(pos_mouse):
                    opciones()
                if Creditos.collidepoint(pos_mouse):
                    creditos()
                
        pygame.display.update()

#Opciones()
#E: -
#S: inicia el menu de opciones
#R: -
def opciones():
    #Iniciando ciclo
    running = True
    
    #Iniciando ciclo de menu
    while running:

        #Reinciando pantalla
        screen.fill((0,0,0))

        #Inciando Escenario de fondo
        escenario()

        #Creando Texto
        TowerDefense = texto("Tower Defense",font40,(255,255,255),screen,200,50)

        #Ciclo de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        pygame.display.update()
        
#Creditos()
#E: -
#S: inicia el menu de opciones
#R: -
def creditos():
    #Iniciando ciclo
    running = True
    
    #Iniciando ciclo de menu
    while running:

        #Reinciando pantalla
        screen.fill((0,0,0))

        #Inciando Escenario de fondo
        escenario()

        #Creando Texto
        TowerDefense = texto("Tower Defense",font40,(255,255,255),screen,200,50)

        #Cargando imagen del menu
        scrollrect = scroll.get_rect()
        scrollrect.midtop = (200,100)
        screen.blit(scroll,scrollrect)

        #Agregando Texto de Creditos
        texto(''' Hola''',font15,(0,0,0),scroll,75,50)
        
        #Ciclo de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        pygame.display.update()

#escenario()
#E: -
#S: se crea el escenario en la pantalla
#R: - 
def escenario():
    y = 0
    for fila in primer_escenario:
        x = 0
        for columna in fila:
            display.blit(casilla3,(x*16,y*16))
            x += 1
        y += 1
    
    y = 0
    for fila in primer_escenario:
        x = 0
        for columna in fila:
            if columna == '1':
                display.blit(arbusto,(x*16,y*16))
            if columna == '2':
                display.blit(arbusto,(x*16,y*16))
            if columna == '3':
                display.blit(arbusto,(x*16,y*16))
            if columna == '4':
                display.blit(arbusto,(x*16,y*16))
            if columna == '5':
                display.blit(arbusto,(x*16,y*16))
            if columna == '6':
                display.blit(arbusto,(x*16,y*16))
            if columna == '7':
                display.blit(arbusto,(x*16,y*16))
            if columna == '8':
                display.blit(arbusto,(x*16,y*16))

            x += 1
        y += 1

        screen.blit(pygame.transform.scale(display,(window_size)),(0,0))#Tansformando superficie a la escala de la ventana
    

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
        escenario()
        
        #Ciclo de Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = True
                if mouse == True:
                    running = False

        pygame.display.update()


menu_principal()

pygame.display.quit()

