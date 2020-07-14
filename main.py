import pygame
from pathlib import Path

#Iniciando Pygame y Clock
clock = pygame.time.Clock()
pygame.init()

#Iniciando ventana
window_size = (400,480)
screen = pygame.display.set_mode(size=window_size)
pygame.display.set_caption("Proyecto Programado")

#Creando Superficie 
display = pygame.Surface((112,176))

#Cargando Mapa
def mapa(archivo):
    copia = open(archivo+".txt")
    mapa_lista = copia.read()
    copia.close
    mapa_lista = mapa_lista.split('\n')
    for y in range(len(mapa_lista)):
        mapa_lista[y] = mapa_lista[y].split()
    return(mapa_lista)

#Cargando Mapa
def cargar_img_mapa(carpeta):
    path = Path(".")/carpeta
    lista_archivos = list(path.iterdir())
    lista_tiles = []
    for file in lista_archivos:
        lista= str(file).split()[0].split('\\')
        nombre_img= lista[1].strip(".png")
        path = (lista[0] + '/' + lista[1])
        img = pygame.image.load(path).convert()
        img.set_colorkey((255,255,255))
        lista_tiles.append([nombre_img,img])
    return lista_tiles

tiles = cargar_img_mapa("Tiles2")

#Cargando Imagenes del menu
scroll = pygame.image.load("Tiles2/scroll.png").convert()
scroll.set_colorkey((255,255,255))

#Cargando Imagenes del escenario1
casilla1= pygame.image.load("Tiles2/casilla1.png").convert()
casilla2= pygame.image.load("Tiles2/casilla2.png").convert()

#Cargando Imagenes del escenario2
casilla4= pygame.image.load("Tiles2/casilla4.png").convert()

#Cargando imagenes de avatares
escudero=pygame.image.load('Tiles1/frames1/knight_m_idle_anim_f0.png')

#Cargando imagenes de rooks
seleccionador1 = pygame.image.load("Tiles2/seleccionador1.png").convert()
seleccionador2 = pygame.image.load("Tiles2/seleccionador2.png").convert()
seleccionador_rook = pygame.image.load("Tiles2/seleccionador_rook.png").convert()
seleccionador1.set_colorkey((255,255,255))
seleccionador2.set_colorkey((255,255,255))
seleccionador_rook.set_colorkey((255,255,255))

#Cargando Mapas
mapa = mapa("mapa")

#Creand fonts 
font40 = pygame.font.SysFont('berlinsansfbdemi', 40)
font35 = pygame.font.SysFont('berlinsansfbdemi', 35)
font30 = pygame.font.SysFont('berlinsansfbdemi', 30)
font15 = pygame.font.SysFont('berlinsansfbdemi', 15)

#text(texto, font, color, superficie,x,y)
#E: un text, un tipo de font, un color(RGB),una superficie, coordenadas xy
#S: se imprime en texto con el tipo de font y color en  la superficie, coordenadas(x,y)
#R: - 
def texto(texto, font, color, superficie,x,y,posicion):
    text = font.render(texto,1,color)
    textrect = text.get_rect()
    if posicion.upper() == "CENTRO":
        textrect.midtop = (x,y)
    else:
        textrect.topleft = (x,y)
    superficie.blit(text,textrect)
    return textrect

def menu_principal():
    #Iniciando ciclo
    running = True
    
    #Cargado musica del menu e iniciandola
    pygame.mixer.music.load('Musica/003 - A Hint of Things to Come.mp3')
    pygame.mixer.music.play(1000)
    
    #Iniciando ciclo de menu
    while running:
       
        #Reiniciando pantalla
        screen.fill((0,0,0))

        #Inciando Escenario de fondo
        escenario(-33)

        #Creando Texto
        TowerDefense = texto("Tower Defense",font40,(255,255,255),screen,200,50,"centro")
        Iniciar = texto("Iniciar",font35,(255,255,255),screen,200,100,"centro")
        Opciones = texto("Opciones",font35,(255,255,255),screen,200,150,"centro")
        Creditos = texto("Creditos",font35,(255,255,255),screen,200,200,"centro")

        #Ciclo de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos_mouse = pygame.mouse.get_pos()
                
                if Iniciar.collidepoint(pos_mouse):
                    juego()
                    pygame.mixer.music.stop()
                if Opciones.collidepoint(pos_mouse):
                    opciones()
                if Creditos.collidepoint(pos_mouse):
                    creditos()
                
        pygame.display.update()

    pygame.mixer.music.stop()
        
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
        escenario(-33)

        #Creando Texto
        TowerDefense = texto("Tower Defense",font40,(255,255,255),screen,200,50,"centro")

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

    creditos = open("Creditos.txt")
    creditos_lista = creditos.read()
    creditos.close()
    creditos_lista = creditos_lista.split('\n')
    print(creditos_lista)
    
    #Iniciando ciclo de menu
    while running:

        #Reinciando pantalla
        screen.fill((0,0,0))

        #Inciando Escenario de fondo
        escenario(-33)

        #Creando Texto
        TowerDefense = texto("Tower Defense",font40,(255,255,255),screen,200,50,"centro")

        #Cargando imagen del menu
        scrollrect = scroll.get_rect()
        scrollrect.midtop = (200,100)
        
        #Agregando Texto de Creditos
        display_creditos = pygame.Surface((150,200))
        display_creditos.fill((255,255,255))
        display_creditos.set_colorkey((255,255,255))
    
        y = 0
        for ele in creditos_lista:
            texto(ele,font15,(0,0,0),display_creditos,0,y,"topleft")
            y += 15

        scroll.blit(display_creditos,(55,50))

        screen.blit(scroll,scrollrect)

        #Ciclo de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        pygame.display.update()

#escenario()
#E: -
#S: se crea el escenario en la pantalla
#R: - 
def escenario(y_actual):

    global tiles
    y = y_actual
    y_display = 0 
    for fila in mapa:
        x = 0
        for columna in fila:
            if y_display <= 22:
                display.blit(casilla4,(x*16,y*16))
            elif y_display > 22 and y_display < 33:
                display.blit(casilla2,(x*16,y*16))
            else:
                display.blit(casilla1,(x*16,y*16))
            x += 1
        y += 1
        y_display += 1

    y = y_actual
    for fila in mapa:
        x = 0
        for columna in fila:
            if columna == '0':
                pass
            else:
                imagen = buscar_tile(columna,tiles)
                display.blit(imagen,(x*16,y*16))
            x += 1
        y += 1

    screen.blit(pygame.transform.scale(display,(window_size)),(0,0))#Tansformando superficie a la escala de la ventana

#buscar_tiles(tile,tiles)
#E: El nombre del tile que se busca y la lista de tiles
#S: la superficie de esa tile
#R: - 
def buscar_tile(tile,tiles):
    for y in tiles:
        if y[0] == tile:
            return y[1]

#juego()
#E: -
#S: inicia el cliclo de juego
#R: - 
def juego():

    #Iniciando ciclo
    running = True
    
    #Se detiene la musica del menu e inicia la musica del juego
    pygame.mixer.music.stop()
    pygame.mixer.music.load('Musica/018 - Enemies Appear.mp3')
    pygame.mixer.music.play(1000)
    
    #Inciando Scrolling
    y = -33

    #Inciando Seleccionador
    seleccionador = pygame.transform.scale(seleccionador1,(53,43))
    seleccionando_casilla= True
    
    #Ciclo de juego
    while running:

        mouse = False

        #Reiniciando superficie y pantalla
        screen.fill((0,0,0))

        #Reiniciando escenario
        escenario(y)

        #Posicionando seleccionador
        mouse_pos = pygame.mouse.get_pos()
        pos_x = mouse_pos[0]//58
        pos_y = mouse_pos[1]//43

        if pos_y >= 2 and pos_x >= 1 and pos_x <= 5 and seleccionando_casilla:
            screen.blit(seleccionador,(pos_x*58,pos_y*43))
        elif not seleccionando_casilla:
            screen.blit(seleccionador,(copia_posx*58,copia_posy*43))
            rook_rect = seleccionador_rook.get_rect()
            rook_rect.topleft = (copia_posx*58-5,copia_posy*43-70)
            screen.blit(seleccionador_rook,rook_rect)
        else:
            pass 
        
        #Ciclo de Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                #Se carga el menu principal otra vez
                menu_principal()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if seleccionando_casilla:
                    copia_posx = pos_x 
                    copia_posy = pos_y
                    seleccionador = pygame.transform.scale(seleccionador2,(53,43))
                    seleccionando_casilla = False
                else:
                    if rook_rect.collidepoint(mouse_pos):
                        seleccion_x = mouse_pos[0] - rook_rect.x
                        seleccion_y = mouse_pos[1] - rook_rect.y
                        if seleccion_x < rook_rect.width/2:
                            if seleccion_y < rook_rect.height/2:
                                print("Rook sand")
                            else:
                                print("Rook rock")
                        else:
                            if seleccion_y < rook_rect.height/2:
                                print("Rook water")
                            else:
                                print("Rook fire")
                    else:
                        pass
                    seleccionador = pygame.transform.scale(seleccionador1,(53,43))
                    seleccionando_casilla = True

                    
                    
                #if y < 0:
                 #   meta = y + 11
                  #  while y != meta:
                   #     escenario(int(y))
                   #     y += 0.25
                   #     pygame.display.update()
                    #y = int(y)
                #else:
                   #pass


        pygame.display.update()
        clock.tick(60)

menu_principal()

pygame.display.quit()

