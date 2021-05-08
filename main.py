import os

import pygame

from constants import *
from grid import Grid

os.environ["SDL_VIDEO_CENTERED"] = '1'

pygame.init()
pygame.display.set_caption("CONWAY'S GAME OF LIFE")
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

grid = Grid(width, height, scale, offset)
grid.random2d_array()

run = True
while run:
    clock.tick(fps)
    screen.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    grid.render(screen)

pygame.quit()
