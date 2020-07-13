import pygame
from pathlib import Path

#Iniciando Pygame y Clock
clock = pygame.time.Clock()
pygame.init()
#Iniciando ventana
window_size = (400,500)
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
        print(nombre_img)
        path = (lista[0] + '/' + lista[1])
        print(path)
        img = pygame.image.load(path).convert()
        print(img)
        img.set_colorkey((255,255,255))
        lista_tiles.append([nombre_img,img])
    return lista_tiles

#print(mapa("mapa-prueba"))
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
#pared_izquierda.set_colorkey(())

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
def texto(texto, font, color, superficie,x,y):
    text = font.render(texto,1,color)
    textrect = text.get_rect()
    textrect.midtop = (x,y)
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
                    pygame.mixer.music.stop()
                if Opciones.collidepoint(pos_mouse):
                    opciones()
                if Creditos.collidepoint(pos_mouse):
                    creditos()
                
        pygame.display.update()
    #Cerrando el ciclo de musica del menu principal
    if pygame.quit():
        pygame.mixer.music.stop
        
        
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
        escenario(-33)

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
                #print(columna)
                imagen = buscar_tile(columna,tiles)
                #print(imagen)
                display.blit(imagen,(x*16,y*16))
            x += 1
        y += 1

    screen.blit(pygame.transform.scale(display,(window_size)),(0,0))#Tansformando superficie a la escala de la ventana

#buscar_tiles(tile,tiles)
#E: El nombre del tile que se busca y la lista de tiles
#S: la superficie de esa tile
#R: - 
def buscar_tile(tile,tiles):
    #print(tiles)
    for y in tiles:
        #print(y[0],tile)
        if y[0] == tile:
            #print(y[1])
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
    pygame.mixer.music.load('Musica/pokemon-opening.mp3')
    pygame.mixer.music.play(1000)
    #Inciando Scrolling
    y = -33

    #Ciclo de juego
    while running:

        mouse = False

        #Reiniciando superficie y pantalla
        screen.fill((0,0,0))
        display.fill((0,0,0))


        #Reiniciando escenario
        escenario(y)
        
        #Ciclo de Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                #Se carga el menu principal otra vez
                menu_principal()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if y < 0:
                    meta = y + 11
                    while y != meta:
                        escenario(int(y))
                        y += 0.25
                        pygame.display.update()
                    y = int(y)
                else:
                    pass

        pygame.display.update()

menu_principal()

pygame.display.quit()

