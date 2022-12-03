import pygame as pg
import PlayerPacman, MapPacman
from GameSettings import *

#pygame essentials
pg.init()
clock = pg.time.Clock()
dis_surf = pg.display.set_mode(screen_size)
fps = framesPerSecond

#sprite sheets
pacman_sheet = pg.image.load('ManPac-pacman.png').convert_alpha()
pacmanBlaze_sheet = pg.image.load('ManPac-pacmanBlaze.png').convert_alpha()
map_sheet = pg.image.load('BoardSection1.png')

#load levels
map = MapPacman.tileMap(map_sheet)

#main player
player = PlayerPacman.pacman(player_start, pacman_sheet, pacmanBlaze_sheet, screen_size)
good_guys = pg.sprite.Group()
good_guys.add(player)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            quit()

        #controls
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_w:
                player.control('y')
            if event.key == pg.K_s:
                player.control('-y')
            if event.key == pg.K_d:
                player.control('x')
            if event.key == pg.K_a:
                player.control('-x')
            if event.key == pg.K_ESCAPE:
                quit()

    #drawings
    player.get_image()
    dis_surf.fill("black")
    player.update()
    good_guys.draw(dis_surf)
    # dis_surf.blit(image, DEFAULT_IMAGE_POSITION)
    #essentials for pygames
    pg.display.update()
    clock.tick(fps)
