# -*- coding: utf-8 -*-

import pygame

class Escudero(pygame.sprite.Sprite):
    def __init__(self, position):
        self.sheet = pygame.image.load('sprites_escudero.png')
        self.sheet.set_clip(pygame.Rect(0, 0, 16, 28))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.frame = 0
        self.up_states = { 0: (0, 0, 16, 28), 1: (21, 0, 16, 28), 2: (42, 0, 16, 28), 3:(63,0,16,28) }

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


