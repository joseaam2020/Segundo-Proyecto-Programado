import pygame
from pathlib import Path
from particulas import * 

pygame.init()

class Rooks(pygame.sprite.Sprite):
    def __init__(self,tipo,posicion_matriz,timer_ataque):
        super().__init__()
        self.tipo = tipo
        self.posicion_matriz = posicion_matriz
        self.posicion_matrizx = posicion_matriz[0]
        self.posicion_matrizy = posicion_matriz[1]
        self.ataque = None
        self.timer_ataque = timer_ataque
        
        if self.tipo.upper() == "FUEGO":
            self.image =  pygame.image.load('Rooks/fire_rook.png')
            self.rect = self.image.get_rect()
            self.resistencia =  16
        elif self.tipo.upper() == "AGUA":
            self.image = pygame.image.load('Rooks/water_rook.png')
            self.rect = self.image.get_rect()
            self.resistencia = 16
        elif self.tipo.upper() == "DESIERTO":
            self.image = pygame.image.load('Rooks/desierto_rook.png')
            self.rect = self.image.get_rect()
            self.resistencia = 1
        elif self.tipo.upper() == "ROCA":
            self.image = pygame.image.load('Rooks/rock_rook.png')
            self.rect = self.image.get_rect()
            self.resistencia = 14 

        self.rect.topleft = ((posicion_matriz[0]+1)*16,(posicion_matriz[1]+2)*16)

    def iniciar_ataque(self,grupo1,grupo2,imagen,frames,damage):
        if self.resistencia > 0:
            if self.ataque==None:
                for sprite in grupo1.sprites():
                    if sprite.posicion_matriz[0] == self.posicion_matrizx:
                        x,y = self.rect.topleft
                        x += self.rect.width//2
                        distancia = sprite.rect.y - y
                        if distancia >= 0:
                            self.ataque = Particula([x,y],distancia,imagen,frames,damage,self)
                            self.ataque.add(grupo2)
                        else:
                            self.ataque = None
                        #print(grupo2)
                    else:
                        pass
            else:
                if isinstance(self.ataque,int):
                    if self.ataque > 0:
                        self.ataque -= self.timer_ataque
                        #print(self.ataque)
                    else:
                        self.ataque = None
                else:
                    pass
        else:
            self.kil()
                
