# -*- coding: utf-8 -*-

import pygame
import rook_class
#Todas las clases funcionan de la misma forma, por lo que solo se definira la primera, en este caso Escudero
'''
Clase:Escudero
Atributos:
          self.sheet; Es la imagen a utilizar
          self.sheet.set_clip(pygame.Rect(x,y,x1,y1)); Define la hitbox del objeto, la x e y definen la posicion inicial
                                                      y la x1 e y1 dictan cuanto va a medir la hitbox
          self.image; es el recuadro de la imagen que se esta utilizando
          self.rect; Es el rectangulo en el que se muestra la imagen, distinto a la hitbox
          self.rect.topleft; Indica la posicion inicial
          self.frame; selecciona la imagen de la lista de estados
          self.up_states; es la lista de imagenes(estados)  entre las que se cambia la imagen del avatar
          self.speed; es la velocida de movimiento del avatar
          self.time_attack;es el tiempo que se toma entre atques
          self.posicion_matriz; Le dice al personaje en que posición debe aparecer
          self.matriz; Dice en que matriz(Por nombre) existe el avatar ej:matriz_avatares
          self.life; Es la cantidad de daño que soporta el avatar
          self.posiciciony_real; Es su posicion en números reales
          self.posicionrecty_anterior;Sirve para saber si la posicion se esta repitiendo
          self.weapon; carga la imagen del arma
          self.weapon.set
          
'''       
class Escudero(pygame.sprite.Sprite):
    def __init__(self, position,velocidad,lapso_entre_ataques,posicion_matriz,matriz):
        self.sheet = pygame.image.load('Avatares/Escudero/sprites_escudero.png')
        self.sheet.set_clip(pygame.Rect(0, 0, 10, 50))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft=position
        self.frame = 0
        self.up_states = { 0: (0, 0, 30, 50),1: (0, 0, 30, 50),2: (0, 0, 30, 50),3: (0, 0, 30, 50),4: (0, 0, 30, 50),5: (0, 0, 30, 50),6: (37, 0, 30, 50),7:(37, 0, 30, 50),8:(37, 0, 30, 50),9:(37, 0, 30, 50),10:(37, 0, 30, 50),11:(37, 0, 30, 50), 12: (77, 0, 30, 50),13:(77, 0, 30, 50),13:(77, 0, 30, 50),14:(77, 0, 30, 50),15:(77, 0, 30, 50),16:(77, 0, 30, 50),17:(77, 0, 30, 50),18:(114,0,30,50),19:(114,0,30,50),20:(114,0,30,50),21:(114,0,30,50),22:(114,0,30,50) }
        self.speed = velocidad
        self.timeattack=lapso_entre_ataques
        pygame.sprite.Sprite.__init__(self)
        self.posicion_matriz = posicion_matriz
        self.matriz = matriz
        self.life=10
        self.posiciony_real = position[1]
        self.posicionrecty_anterior = 0
        #self.weapon= pygame.image.load('Avatares/Escudero/atacando.png')
        #self.weapon.set_clip(pygame.Rect(0,0,10,50))
        #self.attack=self.weapon.subsurface(self.weapon.get_clip())
        #self.attack_states={0:(0,0,30,55)}
        #self.weaponrect =self.weapon.get_rect()
    def set_position(self,posicion):
        position=posicion
        print ('Lo hice')
        
    def get_position(self):
        print(self.position())
        
    def get_frame(self, frame_set):
        self.frame += 1
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        return frame_set[self.frame]

    def clip(self, clipped_rect):
        if type(clipped_rect) is dict:
            self.sheet.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
        else:
            self.sheet.set_clip(pygame.Rect(clipped_rect))
        return clipped_rect

    def update(self, direction):
        if direction == 'up':
            self.clip(self.up_states)
            if self.rect.y % 16 == 0 and self.posicionrecty_anterior != self.rect.y:
                self.posicionrecty_anterior = self.rect.y
                #print(self.rect.y,self.posiciony_real,self.posicion_matriz[1])
                self.posicion_matriz[1] -= 1
                self.matriz[self.posicion_matriz[1]][self.posicion_matriz[0]] = "1"
                #print(self.posicion_matriz)
                if self.posicion_matriz[1] == 9:
                    pass
                else:
                    self.matriz[self.posicion_matriz[1]+1][self.posicion_matriz[0]] = 0
                    #print(self.matriz)
            self.posiciony_real -= self.speed
            self.rect.y = round(self.posiciony_real)
           
        if direction == 'stand_up':
            self.clip(self.up_states[0])
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        
    def handle_event(self,rooks,atq_rooks):
        if self.life>0:
            #print(self.posicion_matriz[1])
            if pygame.sprite.spritecollide(self,rooks,False) or self.posicion_matriz[1]<=0:
<<<<<<< HEAD
                print("Hecho")
                self.update('stand_up')
            for i in pygame.sprite.spritecollide(self,atq_rooks,False):
                print(self.life)
                self.life-=i.damage              
=======
                self.update('stand_up')               
>>>>>>> refs/remotes/origin/desarrollo
            else:
                self.update('up')
                for i in pygame.sprite.spritecollide(self,atq_rooks,False):
                    print(self.life)
                    self.life-=i.damage  
        else:
            self.kill()
            
class Caníbal(pygame.sprite.Sprite):
    def __init__(self, position,velocidad,lapso_entre_ataques,posicion_matriz,matriz):
        self.sheet = pygame.image.load('Avatares/Caníbal/caníbal_sprite.png')
        self.sheet.set_clip(pygame.Rect(0, 0, 10, 40))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.frame = 0
        self.speed = velocidad
        self.life=20
        pygame.sprite.Sprite.__init__(self)
        self.up_states = { 0: (0, 0, 28, 40),1:(0, 0, 28, 40),2:(0, 0, 28, 40),3:(0, 0, 28, 40),4:(0, 0, 28, 40),5:(0, 0, 28, 40), 6: (29, 0, 28, 40),7:(29, 0, 28, 40),8:(29, 0, 28, 40),9:(29, 0, 28, 40),10:(29, 0, 28, 40),11:(29, 0, 28, 40), 12: (57, 0, 28, 40),13:(57, 0, 28, 40),14:(57, 0, 28, 40),15:(57, 0, 28, 40),16:(57, 0, 28, 40),17:(57, 0, 28, 40),18:(86,0,28,40),19:(86,0,28,40),20:(86,0,28,40),21:(86,0,28,40),22:(86,0,28,40), 23:(86,0,28,40) }
        self.posicion_matriz = posicion_matriz
        self.control_matriz = 0
        self.matriz = matriz
        self.posiciony_real = position[1]
        self.posicionrecty_anterior = 0
    def set_position(self,posicion):
        position=posicion
        print ('Lo hice')
        
    def get_position(self):
        print(self.position())
        
    def get_frame(self, frame_set):
        self.frame += 1
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        return frame_set[self.frame]

    def clip(self, clipped_rect):
        if type(clipped_rect) is dict:
            self.sheet.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
        else:
            self.sheet.set_clip(pygame.Rect(clipped_rect))
        return clipped_rect

    def update(self, direction):
        if direction == 'up':
            self.clip(self.up_states)
            if self.rect.y % 16 == 0 and self.posicionrecty_anterior != self.rect.y:
                self.posicionrecty_anterior = self.rect.y
                #print(self.rect.y,self.posiciony_real,self.posicion_matriz[1])
                self.posicion_matriz[1] -= 1
                self.matriz[self.posicion_matriz[1]][self.posicion_matriz[0]] = "3"
                #print(self.posicion_matriz)
                if self.posicion_matriz[1] == 9:
                    pass
                else:
                    self.matriz[self.posicion_matriz[1]+1][self.posicion_matriz[0]] = 0
                    #print(self.matriz)
            self.posiciony_real -= self.speed
            self.rect.y = round(self.posiciony_real)
           
        if direction == 'stand_up':
            self.clip(self.up_states[0])
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        
    def handle_event(self,rooks,atq_rooks):
        if self.life>0:
            if pygame.sprite.spritecollide(self,rooks,False) or self.posicion_matriz[1]<=0:
                self.update('stand_up')           
            else:
                self.update('up')
                for i in pygame.sprite.spritecollide(self,atq_rooks,False):
                    print(self.life)
                    self.life-=i.damage  
        else:
            self.kill()

class Flechador(pygame.sprite.Sprite):
    def __init__(self, position,velocidad,lapso_entre_ataques,posicion_matriz,matriz):
        self.sheet = pygame.image.load('Avatares/Flechador/sprites_flechador.png')
        self.sheet.set_clip(pygame.Rect(0, 0, 10, 50))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        pygame.sprite.Sprite.__init__(self)
        self.frame = 0
        self.life=5
        self.speed = velocidad
        self.up_states = { 0: (0, 0, 26, 50),1:(0, 0, 26, 50),2:(0, 0, 26, 50),3:(0, 0, 26, 50),4:(0, 0, 26, 50),5:(0, 0, 26, 50), 6: (34, 0, 26, 50),7:(34, 0, 26, 50),8:(34, 0, 26, 50),9:(34, 0, 26, 50),10:(34, 0, 26, 50),11:(34, 0, 26, 50), 12: (65, 0, 26, 50),13:(65, 0, 26, 50),14:(65, 0, 26, 50),15:(65, 0, 26, 50),16:(65, 0, 26, 50),17:(65, 0, 26, 50), 18:(100,0,26,50),19:(100,0,26,50),20:(100,0,26,50),21:(100,0,26,50),22:(100,0,26,50),23:(100,0,26,50) }
        self.posicion_matriz = posicion_matriz
        self.control_matriz = 0
        self.matriz = matriz
        self.posiciony_real = position[1]
        self.posicionrecty_anterior = 0
    def set_position(self,posicion):
        position=posicion
        print ('Lo hice')
        
    def get_position(self):
        print(self.position())
        
    def get_frame(self, frame_set):
        self.frame += 1
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        return frame_set[self.frame]

    def clip(self, clipped_rect):
        if type(clipped_rect) is dict:
            self.sheet.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
        else:
            self.sheet.set_clip(pygame.Rect(clipped_rect))
        return clipped_rect

    def update(self, direction):
        if direction == 'up':
            self.clip(self.up_states)
            if self.rect.y % 16 == 0 and self.posicionrecty_anterior != self.rect.y:
                self.posicionrecty_anterior = self.rect.y
                #print(self.rect.y,self.posiciony_real,self.posicion_matriz[1])
                self.posicion_matriz[1] -= 1
                self.matriz[self.posicion_matriz[1]][self.posicion_matriz[0]] = "2"
                #print(self.posicion_matriz)
                if self.posicion_matriz[1] == 9:
                    pass
                else:
                    self.matriz[self.posicion_matriz[1]+1][self.posicion_matriz[0]] = 0
                    #print(self.matriz)
            self.posiciony_real -= self.speed
            self.rect.y = round(self.posiciony_real)
           
        if direction == 'stand_up':
            self.clip(self.up_states[0])
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        
    def handle_event(self,rooks,atq_rooks):
        if self.life>0:
            if pygame.sprite.spritecollide(self,rooks,False) or self.posicion_matriz[1]<=0:
                self.update('stand_up')            
            else:
                self.update('up')
                for i in pygame.sprite.spritecollide(self,atq_rooks,False):
                    print(self.life)
                    self.life-=i.damage  
        else:
            self.kill()

class Leñador(pygame.sprite.Sprite):
    def __init__(self, position,velocidad,lapso_entre_ataques,posicion_matriz,matriz):
        self.sheet = pygame.image.load('Avatares/Leñador/sprites_leñador.png')
        self.sheet.set_clip(pygame.Rect(0, 0, 10, 50))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        pygame.sprite.Sprite.__init__(self)
        self.frame = 0
        self.life=25
        self.speed = velocidad
        self.up_states = { 0: (0, 0, 35, 50),1:(0, 0, 35, 50),2:(0, 0, 35, 50),3:(0, 0, 35, 50),4:(0, 0, 35, 50),5:(0, 0, 35, 50),6:(42, 0, 35, 50),7:(42, 0, 35, 50),8:(42, 0, 35, 50),9:(42, 0, 35, 50),10:(42, 0, 35, 50),11:(42, 0, 35, 50), 12: (88, 0, 35, 50),13:(88, 0, 35, 50),14:(88, 0, 35, 50),15:(88, 0, 35, 50),16:(88, 0, 35, 50),17:(88, 0, 35, 50), 18:(132,0,35,50),19:(132,0,35,50),20:(132,0,35,50),21:(132,0,35,50),22:(132,0,35,50),23:(132,0,35,50) }
        self.posicion_matriz = posicion_matriz
        self.control_matriz = 0
        self.matriz = matriz
        self.posiciony_real = position[1]
        self.posicionrecty_anterior = 0
    def set_position(self,posicion):
        position=posicion
        print ('Lo hice')
        
    def get_position(self):
        print(self.position())
        
    def get_frame(self, frame_set):
        self.frame += 1
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        return frame_set[self.frame]

    def clip(self, clipped_rect):
        if type(clipped_rect) is dict:
            self.sheet.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
        else:
            self.sheet.set_clip(pygame.Rect(clipped_rect))
        return clipped_rect

    def update(self, direction):
        if direction == 'up':
            self.clip(self.up_states)
            if self.rect.y % 16 == 0 and self.posicionrecty_anterior != self.rect.y:
                self.posicionrecty_anterior = self.rect.y
                #print(self.rect.y,self.posiciony_real,self.posicion_matriz[1])
                self.posicion_matriz[1] -= 1
                self.matriz[self.posicion_matriz[1]][self.posicion_matriz[0]] = "4"
                #print(self.posicion_matriz)
                if self.posicion_matriz[1] == 9:
                    pass
                else:
                    self.matriz[self.posicion_matriz[1]+1][self.posicion_matriz[0]] = 0
                    #print(self.matriz)
            self.posiciony_real -= self.speed
            self.rect.y = round(self.posiciony_real)
           
        if direction == 'stand_up':
            self.clip(self.up_states[0])
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        
    def handle_event(self,rooks,atq_rooks):
        if self.life>0:
            if pygame.sprite.spritecollide(self,rooks,False) or self.posicion_matriz[1]<=0:
                self.update('stand_up')           
            else:
                self.update('up')
                for i in pygame.sprite.spritecollide(self,atq_rooks,False):
                    print(self.life)
                    self.life-=i.damage  
        else:
            self.kill()
        
