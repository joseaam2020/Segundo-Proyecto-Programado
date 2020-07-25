# -*- coding: utf-8 -*-

import pygame

class Escudero(pygame.sprite.Sprite):
    def __init__(self, position,velocidad,lapso_entre_ataques,posicion_matriz,matriz):
        self.sheet = pygame.image.load('Avatares/Escudero/sprites_escudero.png')
        self.sheet.set_clip(pygame.Rect(0, 0, 30, 50))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft=position[1]
        self.frame = 0
        self.up_states = { 0: (0, 0, 30, 50),1: (0, 0, 30, 50),2: (0, 0, 30, 50),3: (0, 0, 30, 50),4: (0, 0, 30, 50),5: (0, 0, 30, 50),6: (37, 0, 30, 50),7:(37, 0, 30, 50),8:(37, 0, 30, 50),9:(37, 0, 30, 50),10:(37, 0, 30, 50),11:(37, 0, 30, 50), 12: (77, 0, 30, 50),13:(77, 0, 30, 50),13:(77, 0, 30, 50),14:(77, 0, 30, 50),15:(77, 0, 30, 50),16:(77, 0, 30, 50),17:(77, 0, 30, 50),18:(114,0,30,50),19:(114,0,30,50),20:(114,0,30,50),21:(114,0,30,50),22:(114,0,30,50),23:(114,0,30,50) }
        self.speed = velocidad
        self.timeattack=lapso_entre_ataques
        pygame.sprite.Sprite.__init__(self)
        self.posicion_matriz = posicion_matriz
        control_matriz = 0
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
            control_matriz += self.speed
            if control_matriz >= 16:
                self.posicion_matriz[1] -= 1 
                matriz[self.posicion_matriz[0]][self.posicion_matriz[1]] = "1"
                control_matiz = 0 
            self.rect.y -= self.speed
            
        if direction == 'stand_up':
            self.clip(self.up_states[0])
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        
    def handle_event(self,grupo):
        if pygame.sprite.spritecollide(self,grupo,False):
            self.update('stand_up')
        else:
            self.update('up')  

class Caníbal(pygame.sprite.Sprite):
    def __init__(self, position):
        self.sheet = pygame.image.load('Avatares/Caníbal/caníbal_sprite.png')
        self.sheet.set_clip(pygame.Rect(0, 0, 28, 40))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.frame = 0
        pygame.sprite.Sprite.__init__(self)
        self.up_states = { 0: (0, 0, 28, 40),1:(0, 0, 28, 40),2:(0, 0, 28, 40),3:(0, 0, 28, 40),4:(0, 0, 28, 40),5:(0, 0, 28, 40), 6: (29, 0, 28, 40),7:(29, 0, 28, 40),8:(29, 0, 28, 40),9:(29, 0, 28, 40),10:(29, 0, 28, 40),11:(29, 0, 28, 40), 12: (57, 0, 28, 40),13:(57, 0, 28, 40),14:(57, 0, 28, 40),15:(57, 0, 28, 40),16:(57, 0, 28, 40),17:(57, 0, 28, 40),18:(86,0,28,40),19:(86,0,28,40),20:(86,0,28,40),21:(86,0,28,40),22:(86,0,28,40), 23:(86,0,28,40) }
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
            self.rect.y -= 0.2
        if direction == 'stand_up':
            self.clip(self.up_states[0])


        self.image = self.sheet.subsurface(self.sheet.get_clip())

    def handle_event(self, event,grupo):
        if pygame.sprite.spritecollide(self,grupo,False):
            self.update('stand_up')
        else:
            self.update('up')

class Flechador(pygame.sprite.Sprite):
    def __init__(self, position):
        self.sheet = pygame.image.load('Avatares/Flechador/sprites_flechador.png')
        self.sheet.set_clip(pygame.Rect(0, 0, 26, 50))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        pygame.sprite.Sprite.__init__(self)
        self.frame = 0
        self.up_states = { 0: (0, 0, 26, 50),1:(0, 0, 26, 50),2:(0, 0, 26, 50),3:(0, 0, 26, 50),4:(0, 0, 26, 50),5:(0, 0, 26, 50), 6: (34, 0, 26, 50),7:(34, 0, 26, 50),8:(34, 0, 26, 50),9:(34, 0, 26, 50),10:(34, 0, 26, 50),11:(34, 0, 26, 50), 12: (65, 0, 26, 50),13:(65, 0, 26, 50),14:(65, 0, 26, 50),15:(65, 0, 26, 50),16:(65, 0, 26, 50),17:(65, 0, 26, 50), 18:(100,0,26,50),19:(100,0,26,50),20:(100,0,26,50),21:(100,0,26,50),22:(100,0,26,50),23:(100,0,26,50) }
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
            self.rect.y -= 0.6
        if direction == 'stand_up':
            self.clip(self.up_states[0])


        self.image = self.sheet.subsurface(self.sheet.get_clip())

    def handle_event(self, event,grupo):
        if pygame.sprite.spritecollide(self,grupo,False):
            self.update('stand_up')
        else:
            self.update('up')

class Leñador(pygame.sprite.Sprite):
    def __init__(self, position):
        self.sheet = pygame.image.load('Avatares/Leñador/sprites_leñador.png')
        self.sheet.set_clip(pygame.Rect(0, 0, 20, 50))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        pygame.sprite.Sprite.__init__(self)
        self.frame = 0
        self.up_states = { 0: (0, 0, 35, 50),1:(0, 0, 35, 50),2:(0, 0, 35, 50),3:(0, 0, 35, 50),4:(0, 0, 35, 50),5:(0, 0, 35, 50),6:(42, 0, 35, 50),7:(42, 0, 35, 50),8:(42, 0, 35, 50),9:(42, 0, 35, 50),10:(42, 0, 35, 50),11:(42, 0, 35, 50), 12: (88, 0, 35, 50),13:(88, 0, 35, 50),14:(88, 0, 35, 50),15:(88, 0, 35, 50),16:(88, 0, 35, 50),17:(88, 0, 35, 50), 18:(132,0,35,50),19:(132,0,35,50),20:(132,0,35,50),21:(132,0,35,50),22:(132,0,35,50),23:(132,0,35,50) }
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
            self.rect.y -= 0.6
        if direction == 'stand_up':
            self.clip(self.up_states[0])


        self.image = self.sheet.subsurface(self.sheet.get_clip())

    def handle_event(self, event,grupo):
        if pygame.sprite.spritecollide(self,grupo,False):
            self.update('stand_up')
        else:
            self.update('up')
        
