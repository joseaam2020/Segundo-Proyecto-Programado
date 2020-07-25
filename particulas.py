import pygame
import random

pygame.init()

clock = pygame.time.Clock()
class Particula(pygame.sprite.Sprite):
    def __init__(self,posicion,velocidad_y,time,tipo):
        super().__init__()
        self.posicion = posicion
        self.velocidad = velocidad_y
        self.time = time
        self.tipo = tipo
        if self.tipo == "Fuego":
            self.sheet = pygame.image.load('Effects/Explosion_Poof.png').convert()
            self.sheet.set_colorkey((0,0,0))
            self.duracion = self.time/7
        elif self.tipo == "Agua":
            self.sheet = pygame.image.load('Effects/Bright_Sparkle.png').convert()
            self.sheet.set_colorkey((0,0,0))
            self.duracion = self.time/4
        elif self.tipo == "Roca":
            self.sheet = pygame.image.load('Effects/Cloud_Poof.png').convert()
            self.sheet.set_colorkey((0,0,0))
            self.duracion = self.time/7
        else:
            self.sheet = pygame.image.load('Effects/Yellow_sparkle.png').convert()
            self.sheet.set_colorkey((0,0,0))
            self.duracion = self.time/4
            
        self.image = pygame.Surface((16,16))
        self.image.blit(self.sheet,(0,0))
        self.rect = self.image.get_rect()
        self.rect.midtop = posicion
    
    def update(self):
        if self.time != 0:
            self.rect.y -= self.velocidad
            self.time -= self.velocidad
            if self.tipo == "Fuego" or self.tipo == "Roca":
                nuevo_frame = int((7-(self.time//self.duracion))*-16)
                self.image.fill((0,0,0))
                self.image.blit(self.sheet,(nuevo_frame,0))
            else:
                nuevo_frame = int((4-(self.time//self.duracion))*-16)
                self.image.fill((0,0,0))
                self.image.blit(self.sheet,(nuevo_frame,0))
        else:
            self.kill()

class CreadorParticulas(pygame.sprite.Sprite):
    def __init__(self,posicion,velocidad_y,time,tipo):
        super().__init__()
        self.posicion = posicion
        self.velocidad = velocidad_y
        self.time = time
        self.tipo = tipo
        if self.tipo == "Fuego":
            self.sheet = pygame.image.load('Effects/Explosion_Poof.png').convert()
            self.sheet.set_colorkey((0,0,0))
        elif self.tipo == "Agua":
            self.sheet = pygame.image.load('Effects/Bright_Sparkle.png').convert()
            self.sheet.set_colorkey((0,0,0))
        elif self.tipo == "Roca":
            self.sheet = pygame.image.load('Effects/Cloud_Poof.png').convert()
            self.sheet.set_colorkey((0,0,0))
        else:
            self.sheet = pygame.image.load('Effects/Yellow_sparkle.png').convert()
            self.sheet.set_colorkey((0,0,0))

        self.image = pygame.Surface((16,16))
        self.image.blit(self.sheet,(0,0))
        self.rect = self.image.get_rect()
        self.rect.midtop = posicion
        
    def update(self):
        if self.time != 0:
            self.rect.y += self.velocidad
            self.time -= self.velocidad
            choice = random.choices(["y","n"],[1,6],k=1)
            #print(choice)
            if choice[0] =="y":
                time = random.randint(0,self.time)
                #print(choice,time,[self.rect.x,self.rect.y])
                particula = Particula(self.rect.midtop,self.velocidad,self.time,self.tipo)
                particula.add(self.groups())
            else:
                pass
        else:
            self.kill()
        
#Iniciando ventana
ancho_ventana=400
alto_ventana=480
window_size = (400,480)
screen = pygame.display.set_mode(size=window_size)
pygame.display.set_caption("Particulas")
screen.fill((255,255,255))

grupo_particulas = pygame.sprite.Group()
particula = CreadorParticulas([150,0],1,200,"Fuego")
particula.add(grupo_particulas)
particula = CreadorParticulas([200,0],1,200,"Roca")
particula.add(grupo_particulas)
particula = CreadorParticulas([300,0],1,200,"Agua")
particula.add(grupo_particulas)
particula = CreadorParticulas([350,0],1,200,"Arena")
particula.add(grupo_particulas)
#particula = Particula([200,400],2,60,"yes")

running = True

    
while running:
    
    grupo_particulas.draw(screen)
    for particula in grupo_particulas.sprites():
        particula.update()
        pass
    
    clock.tick(60)
    pygame.display.update()
