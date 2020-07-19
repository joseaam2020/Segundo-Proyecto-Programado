import pygame
from pathlib import Path
import random

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
    copia.close()
    mapa_lista = mapa_lista.split('\n')
    for y in range(len(mapa_lista)):
        mapa_lista[y] = mapa_lista[y].split()
    return(mapa_lista)

#cargar_img
#E: nombre de la caprpeta donde se encuentran las imagenes
#S: lista de la forma [[nombre de la imagen(string), superficie]]
#R: -
def cargar_img(carpeta):
    path = Path(".")/carpeta
    lista_archivos = list(path.iterdir())
    lista_img = []
    for file in lista_archivos:
        lista= str(file).split()[0].split('\\')
        nombre_img= lista[1].strip(".png")
        if nombre_img == "desktop.ini":
            pass
        else:
            path = (lista[0] + '/' + lista[1])
            img = pygame.image.load(path).convert()
            img.set_colorkey((255,255,255))
            lista_img.append([nombre_img,img])
    return lista_img

#Cargando Imagenes del Mapa
tiles = cargar_img("Tiles2")

#Cargando Mapas
mapa = mapa("mapa")

#crear_matriz
#E: numero de filas n y numero de columnas m
#S: matriz nxm llena con ceros
#R: - 
def crear_matriz(n,m):
    matriz = []
    for fila in range(0,n):
        intermedio = []
        matriz.append(intermedio)
        for columna in range(0,m):
            intermedio.append(0)
    return matriz
        
#Colorcar en matriz
#E: matriz en la que se quiere colocar,elemento,donde se quiere colorcar (nxm)
#S: matriz con el elemento en posicion dad
#R: -
def colocar_matriz(matriz,ele,n,m):
    matriz[n][m] = ele

#Colocar aleatorio en matriz
#E: matriz en la que se quiere colocar,lista de elementos,peso de los elementoss(reduce probabilidad)
#S: matriz con elementos de la lista en posiciones aleatorias 
#R: -
def colocar_aleatorio(matriz, lista,lista_pesos):
    probabilidades = crear_matriz(1,len(lista))[0]
    for i in range(0,len(lista_pesos)):
        probabilidades[i] = lista_pesos[i]
        
    for fila in range(0,len(matriz)):
        for columna in range(0,len(matriz[0])):
            if matriz[fila][columna] != 0 :
                pass
            else:
                choice = random.choices(lista,probabilidades,k=1)
                matriz[fila][columna] = choice[0]

#Cargando Rooks
matriz_rooks = crear_matriz(9,5)
img_rooks = cargar_img("Rooks")

#Leer matriz rooks
#E: una superficie
#S: blit de los elementos de la matriz_rooks
def leer_matriz_rooks(superficie):
    global matriz_rooks
    global img_rooks
    n= len(matriz_rooks)
    m= len(matriz_rooks[0])

    for fila in range(0,n):
        for columna in range(0,m):
            ele = str(matriz_rooks[fila][columna])
            if ele == "1":
                superficie.blit(buscar_img("desierto_rook",img_rooks),((columna+1)*16,(fila+2)*16))
            elif ele == "2":
                superficie.blit(buscar_img("rock_rook",img_rooks),((columna+1)*16,(fila+2)*16))
            elif ele == "3":
                superficie.blit(buscar_img("water_rook",img_rooks),((columna+1)*16,(fila+2)*16))
            elif ele == "4":
                superficie.blit(buscar_img("fire_rook",img_rooks),((columna+1)*16,(fila+2)*16))
            else:
                pass

#Iniciando monedas
monedas =  0
moneda_pantalla = pygame.image.load("Tiles2/moneda.png").convert()
moneda_pantalla.set_colorkey((255,255,255))
matriz_monedas = crear_matriz(9,5)

#Leer matriz monedas
#E: superficie 
#S: blit de los elementos de la matriz_monedas
def leer_matriz_monedas(superficie):
    global matriz_monedas
    global matriz_rooks
    global moneda_pantalla
    n = len(matriz_monedas)
    m = len(matriz_monedas[0])

    copia = pygame.transform.scale(moneda_pantalla,(10,10))

    for fila in range(0,n):
        for columna in range(0,m):
            if matriz_rooks[fila][columna] != 0:
                pass
            else:
                ele = str(matriz_monedas[fila][columna])
                if ele == "1":
                    superficie.blit(copia,((columna+1)*16+2,(fila+2)*16+2))
                elif ele == "2":
                    superficie.blit(copia,((columna+1)*16+2,(fila+2)*16+2))
                elif ele == "3":
                    superficie.blit(copia,((columna+1)*16+2,(fila+2)*16+2))
                else:
                    pass

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

#Creando fonts 
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
    elif posicion.upper() == "DERECHA":
        textrect.topright = (x,y)
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
                    running=False
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
                imagen = buscar_img(columna,tiles)
                display.blit(imagen,(x*16,y*16))
            x += 1
        y += 1

    leer_matriz_rooks(display)
    leer_matriz_monedas(display)

    screen.blit(pygame.transform.scale(display,(window_size)),(0,0))#Tansformando superficie a la escala de la ventana

#buscar_tiles(tile,tiles)
#E: El nombre del tile que se busca y la lista de tiles
#S: la superficie de esa tile
#R: - 
def buscar_img(nombre,lista):
    for y in lista:
        if y[0] == nombre:
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
    casilla_seleccionada = False

    #Cargando monedas
    global monedas
    global moneda_pantalla

    monedas = 4000
    
    #Ciclo de juego
    while running:

        mouse = False

        #Reiniciando superficie y pantalla
        screen.fill((0,0,0))

        #Reiniciando escenario
        escenario(y)

        #Colocando monedas
        monedas_x = screen.get_width()-moneda_pantalla.get_width()
        moneda_pantalla = pygame.transform.scale(moneda_pantalla,(25,20))
        screen.blit(moneda_pantalla,(monedas_x,0))
        texto_moneda = texto(str(monedas),font15,(255,255,255),screen,monedas_x,0,"derecha")
        colocar_aleatorio(matriz_monedas,[0,"1","2","3"],[70000,1,1,1])
        
        #Posicionando seleccionador
        mouse_pos = pygame.mouse.get_pos()
        pos_x = mouse_pos[0]//58
        pos_y = mouse_pos[1]//43

        #print(pos_x,pos_y)

        if pos_x > 0 and pos_x < 6 and pos_y > 1 and not casilla_seleccionada:
            screen.blit(seleccionador,(pos_x*58,pos_y*43))
            seleccionando_casilla = True
        elif casilla_seleccionada:
            seleccionando_casilla = False
            screen.blit(seleccionador,(copia_posx*58,copia_posy*43))
            rook_rect = seleccionador_rook.get_rect()
            rook_rect.topleft = (copia_posx*58-5,copia_posy*43-70)
            screen.blit(seleccionador_rook,rook_rect)
        else:
            seleccionando_casilla = False
        
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
                    casilla_seleccionada = True
                    seleccionador = pygame.transform.scale(seleccionador2,(53,43))
                else:
                    if casilla_seleccionada:
                        if rook_rect.collidepoint(mouse_pos):
                            seleccion_x = mouse_pos[0] - rook_rect.x
                            seleccion_y = mouse_pos[1] - rook_rect.y
                            #Id de los diferentes rooks en la matriz
                            #Sand = 1
                            #Rock = 2
                            #Water = 3
                            #Fire = 4
                            if seleccion_x < rook_rect.width/2:
                                if seleccion_y < rook_rect.height/2:
                                    print("Rook sand")
                                    colocar_matriz(matriz_rooks,1,copia_posy-2,copia_posx-1)
                                else:
                                    print("Rook rock")
                                    colocar_matriz(matriz_rooks,2,copia_posy-2,copia_posx-1)
                            else:
                                if seleccion_y < rook_rect.height/2:
                                    print("Rook water")
                                    colocar_matriz(matriz_rooks,3,copia_posy-2,copia_posx-1)
                                else:
                                    print("Rook fire")
                                    colocar_matriz(matriz_rooks,4,copia_posy-2,copia_posx-1)
                            print(matriz_rooks)
                                
                        else:
                            pass
                        
                    seleccionador = pygame.transform.scale(seleccionador1,(53,43))
                    seleccionando_casilla = True
                    casilla_seleccionada = False
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

