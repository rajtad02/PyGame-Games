import pygame as pg
from GameSettings import *

class pacman(pg.sprite.Sprite):
    def __init__(self, pos, sheet, blaze_sheet, screensize):
        pg.sprite.Sprite.__init__(self)
        self.w_h = 16
        self.image = pg.Surface(character_size, pg.RESIZABLE)
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.pastx = 0
        self.pasty = 0
        self.movex = 0
        self.movey = 0
        self.speed = character_speed
        self.dir = 'x'
        self.frame_num = 0
        self.frame_cap = 0
        self.chr_sht = sheet
    
    def control(self, dir):
        self.dir = dir
        if dir == "x":
            self.movex = self.speed
            self.movey = 0
        if dir == "-x":
            self.movex = -self.speed
            self.movey = 0
        if dir == "y":
            self.movey = -self.speed
            self.movex = 0
        if dir == "-y":
            self.movey = self.speed
            self.movex = 0
        
    def update(self): 
        self.rect.x += self.movex
        self.rect.y += self.movey

    def get_image(self):
        row = self.dir2row()
        frame = self.frame2column()
        placeholder_image = pg.Surface((self.w_h, self.w_h)).convert_alpha()
        placeholder_image.blit(self.chr_sht, (0,0), ((frame*self.w_h),(row*self.w_h),(frame*self.w_h) + self.w_h, (row*self.w_h)+ self.w_h))
        placeholder_image.set_colorkey('black')
        self.image = pg.transform.scale(placeholder_image, character_size)

    def dir2row(self):
        if self.dir == 'x': return 0
        if self.dir == 'y': return 1
        if self.dir == '-x': return 2
        if self.dir == '-y': return 3

    def frame2column(self):
        self.frame_cap += 1
        if self.frame_cap == 2:
            self.frame_num += 1
            self.frame_cap = 0
        return self.frame_num%4

    #this bunch of code checks for collisions
    def get_hits(self, tiles): #helper class
        hits = []
        for tile in tiles:
            if self.rect.colliderect(tile) == True:
                hits.append(tile)
        return hits
    
    def checkCollisions(self, tiles):
        collisions = self.get_hits(tiles)
        for tile in collisions:
            if self.movex > 0: #hit tile from the right
                self.rect.left = tile.rect.left - self.rect.w
                self.rect.x = self.rect.left
                self.movex = 0
            elif self.movex < 0:
                self.rect.left = tile.rect.right
                self.rect.x = self.rect.left
            elif self.movey > 0:
                self.rect.top = tile.rect.top - self.rect.h
                self.rect.x = self.rect.left
            elif self.movey < 0:
                self.rect.top = tile.rect.bottom
                self.rect.y = self.rect.top
                self.movey = 0
                