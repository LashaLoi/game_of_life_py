from pygame import init, display, time

from constants import size, width, height, scale, offset
from grid import Grid

init()
display.set_caption("GAME OF LIFE")

screen = display.set_mode(size)
clock = time.Clock()

grid = Grid(width, height, scale, offset)
grid.random2d_array()


def get_config():
    return grid, screen, clock
