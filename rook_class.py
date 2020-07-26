import pygame
from pathlib import Path
from particulas import * 

pygame.init()

class Rooks(pygame.sprite.Sprite):
    def __init__(self,tipo,posicion_matriz):
        super().__init__()
        self.tipo = tipo
        self.posicion_matriz = posicion_matriz
        self.posicion_matrizx = posicion_matriz[0]
        self.posicion_matrizy = posicion_matriz[1]
        self.ataque = None

        
        if self.tipo.upper() == "FUEGO":
            self.image =  pygame.image.load('Rooks/fire_rook.png')
            self.rect = self.image.get_rect()
        elif self.tipo.upper() == "AGUA":
            self.image = pygame.image.load('Rooks/water_rook.png')
            self.rect = self.image.get_rect()
        elif self.tipo.upper() == "DESIERTO":
            self.image = pygame.image.load('Rooks/desierto_rook.png')
            self.rect = self.image.get_rect()
        elif self.tipo.upper() == "ROCA":
            self.image = pygame.image.load('Rooks/rock_rook.png')
            self.rect = self.image.get_rect()

        self.rect.topleft = ((posicion_matriz[0]+1)*16,(posicion_matriz[1]+2)*16)


    def iniciar_ataque(self,grupo1,grupo2,imagen,frames,damage):
        if self.ataque==None:
            for sprite in grupo1.sprites():
                if sprite.posicion_matriz[0] == self.posicion_matrizx:
                    x,y = self.rect.topleft
                    x += self.rect.width//2
                    distancia = sprite.rect.y - y
                    self.ataque = Particula([x,y],distancia,imagen,frames,damage,self)
                    self.ataque.add(grupo2)
                    #print(grupo2)
                else:
                    pass
