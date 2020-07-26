import pygame
import random

pygame.init()


class Particula(pygame.sprite.Sprite):
    def __init__(self,posicion,distancia,imagen,frames,damage,rook):
        super().__init__()
        self.posicion = posicion
        self.distancia = distancia
        self.sheet = imagen
        self.frames = frames
        self.image = pygame.Surface((16,16))
        self.image.blit(self.sheet,(0,0))
        self.rect = self.image.get_rect()
        self.rect.midtop = posicion
        self.duracion_frames = self.distancia//self.frames
        self.damage = damage
        self.rook = rook
    
    def update(self,grupo):
        #print(pygame.sprite.spritecollide(self,grupo,False))
        if pygame.sprite.spritecollide(self,grupo,False) == []:
            self.rect.y += 1
            self.distancia -= 1
            self.num_frames =(self.frames - self.distancia//self.duracion_frames)
            self.altura_imagen = 16*self.num_frames
            self.image = pygame.Surface((16,self.altura_imagen))
            self.sheet_rect =self.sheet.get_rect()
            self.image.blit(self.sheet,(0,-self.sheet_rect.height+(16*self.num_frames)))
            pos_tmp = self.rect.midtop
            self.rect = self.image.get_rect()
            self.rect.midtop = pos_tmp
        else:
            self.kill()
            self.rook.ataque = 100
            #if self.altura_imagen <= 0:
             #   self.kill()
            #else:
             #   #print(self.altura_imagen)
              #  self.altura_imagen -= 1
               # self.rect.y += 1
                #if self.altura_imagen < 112 and self.altura_imagen % 16 == 0:
                #    self.num_frames -= 1
                #self.image = pygame.Surface((16,self.altura_imagen))
                #self.image.blit(self.sheet,(0,-self.sheet_rect.height+(16*self.num_frames)))
