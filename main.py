import pygame
from pathlib import Path
import random
from rook_class import *
import player

#Iniciando Pygame y Clock
clock = pygame.time.Clock()
pygame.init()

#Variable que se encarga de si la musica suena o se mutea
musica=True


#Iniciando ventana
ancho_ventana=400
alto_ventana=480
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
y_escenario = 0

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

#Iniciando Sprite Groups
allsprites = pygame.sprite.Group()
grupo_avatares=pygame.sprite.Group()
grupo_rooks = pygame.sprite.Group()
grupo_particulas = pygame.sprite.Group()
            
#Iniciando monedas
monedas =  0
moneda_oro = pygame.image.load("Tiles2/moneda_oro.png").convert()
moneda_plata = pygame.image.load("Tiles2/moneda_plata.png").convert()
moneda_bronce = pygame.image.load("Tiles2/moneda_bronce.png").convert()
moneda_oro.set_colorkey((255,255,255))
moneda_plata.set_colorkey((255,255,255))
moneda_bronce.set_colorkey((255,255,255))
sonido_moneda = pygame.mixer.Sound("SFX/sonido_moneda.wav")
sonido_moneda.set_volume(500)
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

    copia_oro = pygame.transform.scale(moneda_oro,(10,10))
    copia_bronce = pygame.transform.scale(moneda_bronce,(10,10))

    for fila in range(0,n):
        for columna in range(0,m):
            if matriz_rooks[fila][columna] != 0:
                pass
            else:
                ele = str(matriz_monedas[fila][columna])
                if ele == "1":
                    superficie.blit(copia_bronce,((columna+1)*16+2,(fila+2)*16+2))
                elif ele == "2":
                    superficie.blit(moneda_plata,((columna+1)*16,(fila+2)*16))
                elif ele == "3":
                    superficie.blit(copia_oro,((columna+1)*16+2,(fila+2)*16+2))
                else:
                    pass

#Cargando Imagenes del menu
scroll = pygame.image.load("Tiles2/scroll.png").convert()
triangulo_seleccion = pygame.image.load("Tiles2/triangulo_seleccion.png").convert()
scroll.set_colorkey((255,255,255))
triangulo_seleccion.set_colorkey((255,255,255))

#Cargando Imagenes del escenario1
casilla1= pygame.image.load("Tiles2/casilla1.png").convert()
casilla2= pygame.image.load("Tiles2/casilla2.png").convert()

#Cargando Imagenes del escenario2
casilla4= pygame.image.load("Tiles2/casilla4.png").convert()

#Creando matriz de avatares
matriz_avatares=crear_matriz(10,5)
matriz_de_spawn= crear_matriz(1,5)
colocar_aleatorio(matriz_de_spawn,[0,"1","2","3","4"],[1000,50,100,10,5])
print(matriz_avatares,matriz_de_spawn)
matriz_avatares[-1] = matriz_de_spawn[0]
print(matriz_avatares)

def leer_matriz_avatar(dificultad):
    global allsprites
    global grupo_avatares
    
    spawn = matriz_avatares[-1]

    for i in range(0,len(spawn)):
        if dificultad=='Facil':
            if spawn[i] == '1':
                avatar= player.Escudero(((i+1)*16,(len(matriz_avatares)+1)*16),0.03,5,[i,len(matriz_avatares)],matriz_avatares)
                avatar.add(allsprites,grupo_avatares)
            if spawn[i] == '3':
                avatar= player.Caníbal(((i+1)*16,(len(matriz_avatares)+1)*16),0.03,5,[i,len(matriz_avatares)],matriz_avatares)
                avatar.add(allsprites,grupo_avatares) 
            if spawn[i] == '2':
                avatar= player.Flechador(((i+1)*16,(len(matriz_avatares)+1)*16),0.03,5,[i,len(matriz_avatares)],matriz_avatares)
                avatar.add(allsprites,grupo_avatares)
            if spawn[i] == '4':
                avatar= player.Leñador(((i+1)*16,(len(matriz_avatares)+1)*16),0.03,5,[i,len(matriz_avatares)],matriz_avatares)
                avatar.add(allsprites,grupo_avatares)
            else:
                pass
        if dificultad=='Normal':
            if spawn[i] == '1':
                avatar= player.Escudero(((i+1)*16,(len(matriz_avatares)+1)*16),0.03,5,[i,len(matriz_avatares)],matriz_avatares)
                avatar.add(allsprites,grupo_avatares)
            if spawn[i] == '3':
                avatar= player.Caníbal(((i+1)*16,(len(matriz_avatares)+1)*16),0.03,5,[i,len(matriz_avatares)],matriz_avatares)
                avatar.add(allsprites,grupo_avatares) 
            if spawn[i] == '2':
                avatar= player.Flechador(((i+1)*16,(len(matriz_avatares)+1)*16),0.03,5,[i,len(matriz_avatares)],matriz_avatares)
                avatar.add(allsprites,grupo_avatares)
            if spawn[i] == '4':
                avatar= player.Leñador(((i+1)*16,(len(matriz_avatares)+1)*16),0.03,5,[i,len(matriz_avatares)],matriz_avatares)
                avatar.add(allsprites,grupo_avatares)
            else:
                pass
        if dificultad=='Dificil':
            if spawn[i] == '1':
                avatar= player.Escudero(((i+1)*16,(len(matriz_avatares)+1)*16),0.3,5,[i,len(matriz_avatares)],matriz_avatares)
                avatar.add(allsprites,grupo_avatares)
            if spawn[i] == '3':
                avatar= player.Caníbal(((i+1)*16,(len(matriz_avatares)+1)*16),0.3,5,[i,len(matriz_avatares)],matriz_avatares)
                avatar.add(allsprites,grupo_avatares) 
            if spawn[i] == '2':
                avatar= player.Flechador(((i+1)*16,(len(matriz_avatares)+1)*16),0.3,5,[i,len(matriz_avatares)],matriz_avatares)
                avatar.add(allsprites,grupo_avatares)
            if spawn[i] == '4':
                avatar= player.Leñador(((i+1)*16,(len(matriz_avatares)+1)*16),0.3,5,[i,len(matriz_avatares)],matriz_avatares)
                avatar.add(allsprites,grupo_avatares)
            else:
                pass

            
#Cargando imagenes de avatares
aparicion=[70,300,130,190,250]
#Escudero = player.Escudero(((i+1)*16,(len(matriz_avatar)+2)*16),0.2,5,[i,len(matriz_avatar-1)],matriz_avatares)
#canibal=player.Caníbal(((ancho_ventana/2)-10, alto_ventana))
#arquero= player.Flechador(((ancho_ventana/2), alto_ventana/2))
#leñador= player.Leñador(((ancho_ventana/2), alto_ventana/2))

#Cargando imagenes de rooks
seleccionador1 = pygame.image.load("Tiles2/seleccionador1.png").convert()
seleccionador2 = pygame.image.load("Tiles2/seleccionador2.png").convert()
seleccionador_rook = pygame.image.load("Tiles2/seleccionador_rook.png").convert()
seleccionador1.set_colorkey((255,255,255))
seleccionador2.set_colorkey((255,255,255))
seleccionador_rook.set_colorkey((255,255,255))

#Cargando imagenes particula
particulas_fuego = pygame.image.load('Effects/Explosion_Poof.png').convert()
particulas_agua =pygame.image.load('Effects/Bright_Sparkle.png').convert()
particulas_roca =pygame.image.load('Effects/Cloud_Poof.png').convert()
particulas_desierto =pygame.image.load('Effects/Yellow_sparkle.png').convert()

particulas_fuego.set_colorkey((255,255,255))
particulas_agua.set_colorkey((255,255,255))
particulas_roca.set_colorkey((255,255,255))
particulas_desierto.set_colorkey((255,255,255))

particulas_fuego = pygame.transform.rotate(particulas_fuego,90)
particulas_agua = pygame.transform.rotate(particulas_agua,90)
particulas_roca = pygame.transform.rotate(particulas_roca,90)
particulas_desierto = pygame.transform.rotate(particulas_desierto,90)

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
    global musica
    #Cargado musica del menu e iniciandola
    if musica==True:
        pygame.mixer.music.load('Musica/003 - A Hint of Things to Come.mp3')
        pygame.mixer.music.play(1000)

    global y_escenario
    
    #Iniciando ciclo de menu
    while running:
       
        #Reiniciando pantalla
        screen.fill((0,0,0))

        #Inciando Escenario de fondo
        escenario(y_escenario)

        #Creando Texto
        TowerDefense = texto("Tower Defense",font40,(255,255,255),screen,200,50,"centro")
        Iniciar = texto("Iniciar",font35,(255,255,255),screen,200,100,"centro")
        Opciones = texto("Opciones",font35,(255,255,255),screen,200,150,"centro")
        Creditos = texto("Creditos",font35,(255,255,255),screen,200,200,"centro")
        Instrucciones = texto("Instrucciones",font35,(255,255,255),screen,200,250,"centro")

        #Ciclo de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type==pygame.KEYDOWN:
                if event.key== pygame.K_1:
                    musica=False
                    pygame.mixer.music.fadeout(2000)
                if event.key== pygame.K_2:
                    musica=True
                    pygame.mixer.music.play()
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
                if Instrucciones.collidepoint(pos_mouse):
                    instrucciones()
                
                
        pygame.display.update()

    pygame.mixer.music.stop()
        
#Opciones()
#E: -
#S: inicia el menu de opciones
#R: -
def opciones():
    #Iniciando ciclo
    running = True
    global y_escenario
    
    #Iniciando ciclo de menu
    while running:

        #Reinciando pantalla
        screen.fill((0,0,0))

        #Inciando Escenario de fondo
        escenario(y_escenario)

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
    global y_escenario

    #Cargando Creditos
    creditos = open("Creditos.txt")
    creditos_lista = creditos.read()
    creditos.close()
    creditos_lista = creditos_lista.split('\n')
    print(creditos_lista)

    #Iniciando Valor y de display_creditos
    creditos_y = 0

    #Cargando Imagen triangulo_seleccion
    global triangulo_seleccion

    #Cargando fotos
    foto_jose = pygame.image.load("Tiles2/foto_jose.jpg").convert()
    foto_jordy = pygame.image.load("Tiles2/foto_jordy.jpg").convert()
    
    #Iniciando ciclo de menu
    while running:

        #Reinciando pantalla
        screen.fill((0,0,0))

        #Inciando Escenario de fondo
        escenario(y_escenario)

        #Creando Texto
        TowerDefense = texto("Tower Defense",font40,(255,255,255),screen,200,50,"centro")

        #Cargando imagen del menu
        scrollrect = scroll.get_rect()
        scrollrect.topleft = (0,0)
        tsrect = triangulo_seleccion.get_rect()
        tsrect.midtop= (125,300)
        
        creditos = pygame.Surface((scrollrect.width,scrollrect.height))
        creditos.set_colorkey((0,0,0))
        creditosrect = creditos.get_rect()
        creditosrect.midtop= (150,100)
        
        frame =  pygame.Surface((150,240))
        framerect = frame.get_rect()
        framerect.topleft = (55,50)
        frame.fill((255,255,255))
        
        #Agregando Texto de Creditos
        texto_creditos = pygame.Surface((150,800))
        texto_creditos.fill((255,255,255))
        texto_creditos.set_colorkey((255,255,255))
        texto_creditosrect = texto_creditos.get_rect()
    
        y = 0
        for ele in creditos_lista:
            texto(ele,font15,(0,0,0),texto_creditos,0,y,"topleft")
            y += 15
            
        frame.blit(texto_creditos,(0,creditos_y))
        frame.set_colorkey((255,255,255))
        creditos.blit(scroll,scrollrect)
        creditos.blit(frame,framerect)
        creditos.blit(triangulo_seleccion,tsrect)
        if creditos_y < 0:
            triangulo_seleccion2 = pygame.transform.rotate(triangulo_seleccion,180)
            ts2rect = triangulo_seleccion2.get_rect()
            ts2rect.midtop = (125,10)
            creditos.blit(triangulo_seleccion2,ts2rect)
        
        screen.blit(creditos,creditosrect)
        screen.blit(foto_jordy,(280,150))
        screen.blit(foto_jose,(280,300))

        #Ciclo de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                x,y = mouse_pos
                x,y=[x-creditosrect.x,y-creditosrect.y]
                if tsrect.collidepoint((x,y)):
                    creditos_y -= frame.get_height()
                elif creditos_y < 0 :
                    if  ts2rect.collidepoint((x,y)):
                        creditos_y += frame.get_height()
                    
                
                
        pygame.display.update()

#Creditos()
#E: -
#S: inicia el menu de opciones
#R: -
def instrucciones():
    #Iniciando ciclo
    running = True
    global y_escenario

    #Cargando instrucciones
    instrucciones = open("Instrucciones.txt")
    instrucciones_lista = instrucciones.read()
    instrucciones.close()
    instrucciones_lista = instrucciones_lista.split('\n')
    print(instrucciones_lista)

    #Iniciando Valor y de display_instrucciones
    instrucciones_y = 0

    #Cargando Imagen triangulo_seleccion
    global triangulo_seleccion

    #Cargando fotos
    foto_jose = pygame.image.load("Tiles2/foto_jose.jpg").convert()
    foto_jordy = pygame.image.load("Tiles2/foto_jordy.jpg").convert()
    
    #Iniciando ciclo de menu
    while running:

        #Reinciando pantalla
        screen.fill((0,0,0))

        #Inciando Escenario de fondo
        escenario(y_escenario)

        #Creando Texto
        TowerDefense = texto("Tower Defense",font40,(255,255,255),screen,200,50,"centro")

        #Cargando imagen del menu
        scrollrect = scroll.get_rect()
        scrollrect.topleft = (0,0)
        tsrect = triangulo_seleccion.get_rect()
        tsrect.midtop= (125,300)
        
        instrucciones = pygame.Surface((scrollrect.width,scrollrect.height))
        instrucciones.set_colorkey((0,0,0))
        instruccionesrect = instrucciones.get_rect()
        instruccionesrect.midtop= (150,100)
        
        frame =  pygame.Surface((150,240))
        framerect = frame.get_rect()
        framerect.topleft = (55,50)
        frame.fill((255,255,255))
        
        #Agregando Texto de instrucciones
        texto_instrucciones = pygame.Surface((150,800))
        texto_instrucciones.fill((255,255,255))
        texto_instrucciones.set_colorkey((255,255,255))
        texto_instruccionesrect = texto_instrucciones.get_rect()
    
        y = 0
        for ele in instrucciones_lista:
            texto(ele,font15,(0,0,0),texto_instrucciones,0,y,"topleft")
            y += 15
            
        frame.blit(texto_instrucciones,(0,instrucciones_y))
        frame.set_colorkey((255,255,255))
        instrucciones.blit(scroll,scrollrect)
        instrucciones.blit(frame,framerect)
        instrucciones.blit(triangulo_seleccion,tsrect)
        if instrucciones_y < 0:
            triangulo_seleccion2 = pygame.transform.rotate(triangulo_seleccion,180)
            ts2rect = triangulo_seleccion2.get_rect()
            ts2rect.midtop = (125,10)
            instrucciones.blit(triangulo_seleccion2,ts2rect)
        
        screen.blit(instrucciones,instruccionesrect)

        #Ciclo de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                x,y = mouse_pos
                x,y=[x-instruccionesrect.x,y-instruccionesrect.y]
                if tsrect.collidepoint((x,y)):
                    instrucciones_y -= frame.get_height()
                elif instrucciones_y < 0 :
                    if  ts2rect.collidepoint((x,y)):
                        instrucciones_y += frame.get_height()
                    
                
                
        pygame.display.update()


        
appear=0
#escenario()
#E: -
#S: se crea el escenario en la pantalla
#R: - 
def escenario(y_actual):
    global appear
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


    for avatar in grupo_avatares.sprites():
        #print(avatar,avatar.rect.y)
        avatar.handle_event(grupo_rooks,grupo_particulas)
        avatar.image = pygame.transform.scale(avatar.image,(14,20))
    

    for rook in grupo_rooks.sprites():
        if rook.tipo.upper() == "FUEGO":
            rook.iniciar_ataque(grupo_avatares,grupo_particulas,particulas_fuego,7,8)
        elif rook.tipo.upper() == "AGUA":
            rook.iniciar_ataque(grupo_avatares,grupo_particulas,particulas_agua,4,8)
        elif rook.tipo.upper() == "DESIERTO":
            rook.iniciar_ataque(grupo_avatares,grupo_particulas,particulas_desierto,4,2)
        elif rook.tipo.upper() == "ROCA":
            rook.iniciar_ataque(grupo_avatares,grupo_particulas,particulas_roca,7,4)
            
    for particula in grupo_particulas.sprites():
        particula.update(grupo_avatares)
        particula.image.set_colorkey((0,0,0))
        if grupo_particulas.has(particula):
            particula.add(allsprites)
    leer_matriz_monedas(display)
    allsprites.draw(display)

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
    global appear
    global musica
    global aparicion
    global matriz_avatares
    #Iniciando ciclo
    running = True
    
    #Se detiene la musica del menu e inicia la musica del juego
    if musica==True:
        pygame.mixer.music.load('Musica/018 - Enemies Appear.mp3')
        pygame.mixer.music.play(1000)
    
    #Inciando Scrolling
    global y_escenario

    #Inciando Seleccionador
    seleccionador = pygame.transform.scale(seleccionador1,(53,43))
    casilla_seleccionada = False

    #Cargando monedas
    global monedas
    global moneda_oro
    global sonido_moneda

    monedas = 500

    #Definiendo Velocidad de ataque rooks
    velocidad_ataque = 0.9
    print (allsprites.sprites(),grupo_avatares.sprites())
    
    #Ciclo de juego
    while running:
        appear+=1
        if appear == 1000:
            colocar_aleatorio(matriz_de_spawn,[0,"1","2","3","4"],[1,50,100,10,5])
            matriz_avatares[-1] = matriz_de_spawn[0]
            leer_matriz_avatar('Normal')
            appear=0
        mouse = False

        #Reiniciando superficie y pantalla
        screen.fill((0,0,0))

        #Reiniciando escenario
        escenario(y_escenario)

        #Colocando monedas
        monedas_x = screen.get_width()-moneda_oro.get_width()
        moneda_oro = pygame.transform.scale(moneda_oro,(25,20))
        screen.blit(moneda_oro,(monedas_x,0))
        texto_moneda = texto(str(monedas),font15,(255,255,255),screen,monedas_x,0,"derecha")
        colocar_aleatorio(matriz_monedas,[0,"1","2","3"],[100000,10,1,0.1])
        
        #Posicionando seleccionador
        mouse_pos = pygame.mouse.get_pos()
        pos_x = mouse_pos[0]//58
        pos_y = mouse_pos[1]//43

        #print(pos_x,pos_y)

        if pos_x > 0 and pos_x < 6 and pos_y > 1 and pos_y < 11 and not casilla_seleccionada:
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
        #De momento esto funciona
       
        
        #Ciclo de Eventos
        for event in pygame.event.get():
            
            
            #canibal.handle_event(event,allsprites)
            #screen.blit(canibal.image, canibal.rect)
            #random.shuffle(aparicion)
            if event.type == pygame.QUIT:
                running = False
                #guarda=str(matriz_avatares)
                #with open('Guardado.txt','w') as g:
                    #g.write(guarda)
                #Se carga el menu principal otra vez
                menu_principal()
                
            if event.type==pygame.KEYDOWN:
                if event.key== pygame.K_1:
                    musica=False
                    pygame.mixer.music.fadeout(2000)
                if event.key== pygame.K_2:
                    musica=True
                    pygame.mixer.music.play()
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == pygame.BUTTON_LEFT:    
                    if seleccionando_casilla:
                        if matriz_monedas[pos_y-2][pos_x-1]!= 0:
                            ele = matriz_monedas[pos_y-2][pos_x-1]
                            if ele == "1":
                                monedas += 25
                            elif ele == "2":
                                monedas += 50
                            elif ele == "3":
                                monedas += 100
                            sonido_moneda.play(0)
                            colocar_matriz(matriz_monedas,0,pos_y-2,pos_x-1)
                        else:
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
                                columna = copia_posx-1
                                fila = copia_posy-2
                                if seleccion_x < rook_rect.width/2:
                                    if monedas>=50:
                                        if seleccion_y < rook_rect.height/2:
                                            print("Rook sand")
                                            rook = Rooks("desierto",[columna,fila],velocidad_ataque)
                                            rook.image = rook.image.convert()
                                            rook.image.set_colorkey((255,255,255))
                                            rook.add(allsprites,grupo_rooks)
                                            colocar_matriz(matriz_rooks,1,copia_posy-2,copia_posx-1)
                                        monedas-=50
                                    elif monedas>=100:
                                        if seleccion_y > rook_rect.height/2:
                                            print("Rook rock")
                                            rook = Rooks("roca",[columna,fila],velocidad_ataque)
                                            rook.image = rook.image.convert()
                                            rook.image.set_colorkey((255,255,255))
                                            rook.add(allsprites,grupo_rooks)
                                            colocar_matriz(matriz_rooks,2,copia_posy-2,copia_posx-1)
                                        monedas-=100
                                else:
                                    if monedas>=150:
                                        if seleccion_y < rook_rect.height/2:
                                            print("Rook water")
                                            rook = Rooks("agua",[columna,fila],velocidad_ataque)
                                            rook.image = rook.image.convert()
                                            rook.image.set_colorkey((255,255,255))
                                            rook.add(allsprites,grupo_rooks)
                                            colocar_matriz(matriz_rooks,3,copia_posy-2,copia_posx-1)
                                        else:
                                            print("Rook fire")
                                            rook = Rooks("fuego",[columna,fila],velocidad_ataque)
                                            rook.image = rook.image.convert()
                                            rook.image.set_colorkey((255,255,255))
                                            rook.add(allsprites,grupo_rooks)
                                            colocar_matriz(matriz_rooks,4,copia_posy-2,copia_posx-1)
                                        monedas-=150
                                print(matriz_rooks)
                                print(allsprites.sprites())
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

