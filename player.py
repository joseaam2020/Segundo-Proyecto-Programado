# -*- coding: utf-8 -*-

import pygame

class Escudero(pygame.sprite.Sprite):
    def __init__(self, position):
        self.position=position
        self.sheet = pygame.image.load('Avatares/Escudero/sprites_escudero.png')
        self.sheet.set_clip(pygame.Rect(0, 0, 30, 50))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = self.position
        self.frame = 0
        self.up_states = { 0: (0, 0, 30, 50), 1: (37, 0, 30, 50), 2: (77, 0, 30, 50), 3:(114,0,30,50) }
    def set_position(self,posicion):
        self.position=posicion
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
            self.rect.y -= 5
        if direction == 'stand_up':
            self.clip(self.up_states[0])


        self.image = self.sheet.subsurface(self.sheet.get_clip())

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            game_over = True

    
        self.update('up')

class Caníbal:
    def __init__(self, position):
        self.sheet = pygame.image.load('Avatares/Caníbal/caníbal_sprite.png')
        self.sheet.set_clip(pygame.Rect(0, 0, 28, 40))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.frame = 0
        self.up_states = { 0: (0, 0, 28, 40), 1: (29, 0, 28, 40), 2: (57, 0, 28, 40), 3:(86,0,28,40) }

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
            self.rect.y -= 5
        if direction == 'stand_up':
            self.clip(self.up_states[0])


        self.image = self.sheet.subsurface(self.sheet.get_clip())

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            game_over = True

    
        self.update('up')

class Flechador:
    def __init__(self, position):
        self.sheet = pygame.image.load('Avatares/Flechador/sprites_flechador.png')
        self.sheet.set_clip(pygame.Rect(0, 0, 26, 50))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.frame = 0
        self.up_states = { 0: (0, 0, 26, 50), 1: (34, 0, 26, 50), 2: (65, 0, 26, 50), 3:(100,0,26,50) }

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
            self.rect.y -= 5
        if direction == 'stand_up':
            self.clip(self.up_states[0])


        self.image = self.sheet.subsurface(self.sheet.get_clip())

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            game_over = True

    
        self.update('up')

class Leñador:
    def __init__(self, position):
        self.sheet = pygame.image.load('Avatares/Leñador/sprites_leñador.png')
        self.sheet.set_clip(pygame.Rect(0, 0, 20, 50))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.frame = 0
        self.up_states = { 0: (0, 0, 35, 50), 1: (42, 0, 35, 50), 2: (88, 0, 35, 50), 3:(132,0,35,50) }

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
            self.rect.y -= 5
        if direction == 'stand_up':
            self.clip(self.up_states[0])


        self.image = self.sheet.subsurface(self.sheet.get_clip())

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            game_over = True

    
        self.update('up')
        
