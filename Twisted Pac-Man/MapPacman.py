import pygame as pg
from GameSettings import *

map_list = [(7,13,13,13,13,13,13,13,13,13,13,13,13,13,6)
(12,45,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,12)
(12,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,12)
(12,-1,-1,8,3,3,3,3,3,3,3,11,-1,-1,12)
(12,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,2,-1,-1,12)
(12,-1,-1,9,1,1,6,-1,7,1,1,10,-1,-1,12)
(12,-1,-1,-1,-1,-1,0,-1,2,-1,-1,-1,-1,-1,12)
(12,-1,-1,-1,-1,-1,0,-1,2,-1,-1,-1,-1,-1,12)
(12,-1,-1,-1,-1,-1,0,-1,2,-1,-1,-1,-1,-1,12)
(12,-1,-1,-1,-1,-1,0,-1,2,-1,-1,-1,-1,-1,12)
(12,-1,-1,-1,-1,-1,9,1,10,-1,-1,-1,-1,-1,12)
(12,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,12)
(12,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,12)
(12,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,12)
(12,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,12)]

class Tile(pg.sprite.Sprite):
    def __init__(self, x, y, tile_id, sheet):
        pg.sprite.Sprite.__init__(self)
        self.w_h= 32
        self.tile_id = int(tile_id)
        self.sheet = sheet
        self.image = pg.Surface(brick_size, pg.RESIZABLE)
        self.get_image()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x * self.w_h ,y * self.w_h)

    def get_image(self):
        self.image = pg.Surface((self.w_h, self.w_h)).convert_alpha()
        self.image.blit(self.sheet, (0,0), ((self.tile_id*self.w_h),0,(self.tile_id*self.w_h) + self.w_h, self.w_h))
        self.image.set_colorkey('black')
    
    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

class tileMap:
    def __init__(self, spritesheet):
        self.tile_size = 32
        self.spritesheet = spritesheet
        self.tiles = self.load_tiles(map_list)
        self.map_surface = pg.Surface(screen_size)
        self.map_surface.set_colorkey((0,0,0))
        self.load_map()
    
    def draw_map(self, surface):
        surface.blit(self.map_surface, (0,0))

    def load_map(self):
        for tile in self.tiles:
            tile.draw(self.map_surface)

    def load_tiles(self, listoflist):
        tiles = []
        x,y = 0,0
        for row in listoflist:
            x = 0
            for tile_id in row:
                if tile_id == -1:
                    pass
                elif tile_id == 45:
                    (self.startx, self.starty) = (x,y)
                    pass
                else:
                    tiles.append(Tile(x, y, tile_id, self.spritesheet))
                
                x += 1
            y += 1
        return tiles
    
    def spawnpoint(self):
        return(self.startx * self.tile_size, self.starty * self.tile_size)