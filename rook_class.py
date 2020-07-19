import pygame
from pathlib import Path

pygame.init()

clock=pygame.time.Clock()
class Rooks(pygame.sprite.Sprite):
    def __init__(self,tipo,posicion_matriz):
        super().__init__()
        self.tipo = tipo
        self.posicion_matriz = posicion_matriz
        self.posicion_matrizx = posicion_matriz[0]
        self.posicion_matrizy = posicion_matriz[1]

        if tipo.upper() == "FUEGO":
            self.image =  pygame.image.load('Rooks/fire_rook.png')
            self.rect = self.image.get_rect()
        elif tipo.upper() == "AGUA":
            self.image = pygame.image.load('Rooks/water_rook.png')
            self.rect = self.image.get_rect()
        elif tipo.upper() == "DESIERTO":
            self.image = pygame.image.load('Rooks/desierto_rook.png')
            self.rect = self.image.get_rect()
        elif tipo.upper() == "ROCA":
            self.image = pygame.image.load('Rooks/rock_rook.png')
            self.rect = self.image.get_rect()


